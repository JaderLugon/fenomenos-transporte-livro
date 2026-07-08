"""
qwen_client.py — Cliente Python para integração com a API do Qwen.

Este módulo fornece uma interface simplificada para acessar os modelos Qwen
(Qwen3.7, Qwen-Max, Qwen-Plus, etc.) através da API da Alibaba Cloud (DashScope)
ou de endpoints compatíveis com OpenAI.

Autor: Jader Lugon Junior
Livro: Fenômenos de Transporte: Fundamentos e Modelagem Computacional
Repositório: https://github.com/JaderLugon/fenomenos-transporte-livro

Licença: MIT
"""

import os
import json
import time
import logging
from pathlib import Path
from typing import Optional, List, Dict, Union, Any
from dataclasses import dataclass, field

# Tentativa de importação das dependências
try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# CONSTANTES E CONFIGURAÇÕES
# ============================================================================

# Modelos disponíveis
MODELOS_DISPONIVEIS = {
    'qwen3.7': 'qwen3.7',
    'qwen-max': 'qwen-max',
    'qwen-plus': 'qwen-plus',
    'qwen-turbo': 'qwen-turbo',
    'qwen-long': 'qwen-long',
}

# Endpoints padrão
ENDPOINTS = {
    'dashscope': 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    'openai': 'https://api.openai.com/v1',
}

# Caminho para templates de prompt
TEMPLATES_DIR = Path(__file__).parent / 'prompt_templates'


# ============================================================================
# CLASSES AUXILIARES
# ============================================================================

@dataclass
class Mensagem:
    """Representa uma mensagem em uma conversa."""
    role: str  # 'system', 'user', 'assistant'
    content: str
    timestamp: float = field(default_factory=time.time)
    
    def to_dict(self) -> Dict[str, str]:
        return {'role': self.role, 'content': self.content}


@dataclass
class RespostaQwen:
    """Representa uma resposta da API do Qwen."""
    content: str
    modelo: str
    tokens_usados: Dict[str, int]
    tempo_resposta: float
    finish_reason: str
    raw_response: Optional[Dict] = None
    
    def __str__(self) -> str:
        return self.content


# ============================================================================
# CLASSE PRINCIPAL: QwenClient
# ============================================================================

class QwenClient:
    """
    Cliente para interação com a API do Qwen.
    
    Suporta autenticação via:
    - Variável de ambiente: QWEN_API_KEY
    - Parâmetro direto no construtor
    
    Exemplos
    --------
    >>> client = QwenClient()
    >>> resposta = client.perguntar("Explique a Lei de Fourier")
    >>> print(resposta)
    
    >>> # Com contexto pedagógico
    >>> client = QwenClient(modelo='qwen3.7', temperatura=0.3)
    >>> resposta = client.explicar_conceito("Número de Reynolds", capitulo=4)
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        modelo: str = 'qwen3.7',
        temperatura: float = 0.7,
        max_tokens: int = 2048,
        endpoint: str = 'dashscope',
        timeout: int = 60,
        max_retries: int = 3
    ):
        """
        Inicializa o cliente Qwen.
        
        Parâmetros
        ----------
        api_key : str, opcional
            Chave de API. Se não fornecida, busca em QWEN_API_KEY.
        modelo : str
            Modelo a ser utilizado (ver MODELOS_DISPONIVEIS).
        temperatura : float
            Temperatura de amostragem (0.0 a 2.0). Valores baixos = mais determinístico.
        max_tokens : int
            Número máximo de tokens na resposta.
        endpoint : str
            Endpoint da API ('dashscope' ou 'openai').
        timeout : int
            Timeout em segundos para requisições.
        max_retries : int
            Número máximo de tentativas em caso de falha.
        """
        # Verificar dependências
        if not HAS_OPENAI and not HAS_REQUESTS:
            raise ImportError(
                "É necessário instalar 'openai' ou 'requests':\n"
                "  pip install openai\n"
                "  # ou\n"
                "  pip install requests"
            )
        
        # API Key
        self.api_key = api_key or os.getenv('QWEN_API_KEY')
        if not self.api_key:
            raise ValueError(
                "API Key não fornecida. Defina a variável de ambiente "
                "QWEN_API_KEY ou passe api_key no construtor."
            )
        
        # Modelo
        if modelo not in MODELOS_DISPONIVEIS:
            logger.warning(
                f"Modelo '{modelo}' não reconhecido. "
                f"Usando '{modelo}' mesmo assim."
            )
        self.modelo = modelo
        
        # Parâmetros
        self.temperatura = temperatura
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Endpoint
        self.base_url = ENDPOINTS.get(endpoint, endpoint)
        
        # Histórico de conversa
        self.historico: List[Mensagem] = []
        
        # Carregar templates
        self.templates = self._carregar_templates()
        
        logger.info(f"QwenClient inicializado com modelo '{modelo}'")
    
    # ------------------------------------------------------------------------
    # MÉTODOS PRIVADOS
    # ------------------------------------------------------------------------
    
    def _carregar_templates(self) -> Dict[str, str]:
        """Carrega os templates de prompt do diretório."""
        templates = {}
        if TEMPLATES_DIR.exists():
            for arquivo in TEMPLATES_DIR.glob('*.txt'):
                try:
                    templates[arquivo.stem] = arquivo.read_text(encoding='utf-8')
                except Exception as e:
                    logger.warning(f"Erro ao carregar template {arquivo}: {e}")
        else:
            logger.warning(f"Diretório de templates não encontrado: {TEMPLATES_DIR}")
        return templates
    
    def _fazer_requisicao(self, mensagens: List[Dict]) -> Dict:
        """
        Faz a requisição à API com tratamento de retries.
        
        Parâmetros
        ----------
        mensagens : list
            Lista de mensagens no formato OpenAI.
        
        Retorna
        -------
        dict
            Resposta bruta da API.
        """
        if HAS_OPENAI:
            return self._requisicao_openai(mensagens)
        else:
            return self._requisicao_requests(mensagens)
    
    def _requisicao_openai(self, mensagens: List[Dict]) -> Dict:
        """Requisição usando a biblioteca openai."""
        client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=self.timeout
        )
        
        for tentativa in range(self.max_retries):
            try:
                resposta = client.chat.completions.create(
                    model=self.modelo,
                    messages=mensagens,
                    temperature=self.temperatura,
                    max_tokens=self.max_tokens
                )
                return {
                    'content': resposta.choices[0].message.content,
                    'usage': {
                        'prompt_tokens': resposta.usage.prompt_tokens,
                        'completion_tokens': resposta.usage.completion_tokens,
                        'total_tokens': resposta.usage.total_tokens,
                    },
                    'finish_reason': resposta.choices[0].finish_reason,
                    'model': resposta.model
                }
            except Exception as e:
                logger.warning(f"Tentativa {tentativa + 1} falhou: {e}")
                if tentativa < self.max_retries - 1:
                    time.sleep(2 ** tentativa)  # Backoff exponencial
                else:
                    raise
    
    def _requisicao_requests(self, mensagens: List[Dict]) -> Dict:
        """Requisição usando a biblioteca requests."""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': self.modelo,
            'messages': mensagens,
            'temperature': self.temperatura,
            'max_tokens': self.max_tokens
        }
        
        for tentativa in range(self.max_retries):
            try:
                response = requests.post(
                    f'{self.base_url}/chat/completions',
                    headers=headers,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()
                data = response.json()
                
                return {
                    'content': data['choices'][0]['message']['content'],
                    'usage': data.get('usage', {}),
                    'finish_reason': data['choices'][0].get('finish_reason', 'stop'),
                    'model': data.get('model', self.modelo)
                }
            except Exception as e:
                logger.warning(f"Tentativa {tentativa + 1} falhou: {e}")
                if tentativa < self.max_retries - 1:
                    time.sleep(2 ** tentativa)
                else:
                    raise
    
    def _montar_mensagens(
        self,
        prompt_usuario: str,
        system_prompt: Optional[str] = None
    ) -> List[Dict]:
        """Monta a lista de mensagens para a API."""
        mensagens = []
        
        if system_prompt:
            mensagens.append({'role': 'system', 'content': system_prompt})
        
        mensagens.append({'role': 'user', 'content': prompt_usuario})
        
        return mensagens
    
    # ------------------------------------------------------------------------
    # MÉTODOS PÚBLICOS — INTERFACE BÁSICA
    # ------------------------------------------------------------------------
    
    def perguntar(
        self,
        pergunta: str,
        system_prompt: Optional[str] = None,
        salvar_historico: bool = True
    ) -> RespostaQwen:
        """
        Faz uma pergunta simples ao Qwen.
        
        Parâmetros
        ----------
        pergunta : str
            Pergunta do usuário.
        system_prompt : str, opcional
            Instrução de sistema (comportamento do modelo).
        salvar_historico : bool
            Se True, salva a interação no histórico.
        
        Retorna
        -------
        RespostaQwen
            Objeto com a resposta completa.
        """
        inicio = time.time()
        
        mensagens = self._montar_mensagens(pergunta, system_prompt)
        resposta_raw = self._fazer_requisicao(mensagens)
        
        tempo = time.time() - inicio
        
        resposta = RespostaQwen(
            content=resposta_raw['content'],
            modelo=resposta_raw.get('model', self.modelo),
            tokens_usados=resposta_raw.get('usage', {}),
            tempo_resposta=tempo,
            finish_reason=resposta_raw.get('finish_reason', 'stop'),
            raw_response=resposta_raw
        )
        
        if salvar_historico:
            self.historico.append(Mensagem(role='user', content=pergunta))
            self.historico.append(Mensagem(role='assistant', content=resposta.content))
        
        return resposta
    
    def conversar(self, mensagem: str) -> RespostaQwen:
        """
        Continua uma conversa, mantendo o contexto.
        
        Parâmetros
        ----------
        mensagem : str
            Nova mensagem do usuário.
        
        Retorna
        -------
        RespostaQwen
            Resposta considerando o histórico.
        """
        inicio = time.time()
        
        # Converter histórico para formato da API
        mensagens_api = [m.to_dict() for m in self.historico]
        mensagens_api.append({'role': 'user', 'content': mensagem})
        
        resposta_raw = self._fazer_requisicao(mensagens_api)
        
        tempo = time.time() - inicio
        
        resposta = RespostaQwen(
            content=resposta_raw['content'],
            modelo=resposta_raw.get('model', self.modelo),
            tokens_usados=resposta_raw.get('usage', {}),
            tempo_resposta=tempo,
            finish_reason=resposta_raw.get('finish_reason', 'stop'),
            raw_response=resposta_raw
        )
        
        # Atualizar histórico
        self.historico.append(Mensagem(role='user', content=mensagem))
        self.historico.append(Mensagem(role='assistant', content=resposta.content))
        
        return resposta
    
    def limpar_historico(self):
        """Limpa o histórico de conversa."""
        self.historico = []
        logger.info("Histórico de conversa limpo")
    
    # ------------------------------------------------------------------------
    # MÉTODOS PÚBLICOS — APLICAÇÕES PEDAGÓGICAS
    # ------------------------------------------------------------------------
    
    def explicar_conceito(
        self,
        conceito: str,
        capitulo: Optional[int] = None,
        nivel: str = 'graduacao',
        incluir_exemplo: bool = True
    ) -> RespostaQwen:
        """
        Explica um conceito do livro de forma didática.
        
        Parâmetros
        ----------
        conceito : str
            Conceito a ser explicado (ex: "Número de Reynolds").
        capitulo : int, opcional
            Capítulo do livro relacionado.
        nivel : str
            Nível didático ('graduacao' ou 'pos-graduacao').
        incluir_exemplo : bool
            Se True, inclui exemplo numérico.
        
        Retorna
        -------
        RespostaQwen
            Explicação formatada.
        """
        template = self.templates.get('explicacao_conceito', '')
        
        prompt = template.format(
            conceito=conceito,
            capitulo=capitulo or 'não especificado',
            nivel=nivel,
            incluir_exemplo='Sim' if incluir_exemplo else 'Não'
        )
        
        system_prompt = (
            "Você é um professor especialista em Fenômenos de Transporte, "
            "didático e rigoroso. Baseie suas explicações no livro "
            "'Fenômenos de Transporte: Fundamentos e Modelagem Computacional' "
            "de Jader Lugon Junior."
        )
        
        return self.perguntar(prompt, system_prompt=system_prompt)
    
    def resolver_exercicio(
        self,
        enunciado: str,
        capitulo: Optional[int] = None,
        mostrar_passos: bool = True,
        auditoria_ia: bool = True
    ) -> RespostaQwen:
        """
        Resolve um exercício passo a passo.
        
        Parâmetros
        ----------
        enunciado : str
            Enunciado do exercício.
        capitulo : int, opcional
            Capítulo do livro relacionado.
        mostrar_passos : bool
            Se True, mostra todos os passos da solução.
        auditoria_ia : bool
            Se True, inclui seção de auditoria crítica (V&V).
        
        Retorna
        -------
        RespostaQwen
            Solução detalhada.
        """
        template = self.templates.get('resolucao_exercicio', '')
        
        prompt = template.format(
            enunciado=enunciado,
            capitulo=capitulo or 'não especificado',
            mostrar_passos='Sim' if mostrar_passos else 'Não',
            auditoria_ia='Sim' if auditoria_ia else 'Não'
        )
        
        system_prompt = (
            "Você é um professor especialista em Fenômenos de Transporte. "
            "Ao resolver exercícios:\n"
            "1. Apresente a solução passo a passo\n"
            "2. Verifique consistência dimensional\n"
            "3. Interprete fisicamente o resultado\n"
            "4. Discuta limitações e hipóteses assumidas"
        )
        
        return self.perguntar(prompt, system_prompt=system_prompt)
    
    def gerar_codigo(
        self,
        descricao: str,
        linguagem: str = 'python',
        capitulo: Optional[int] = None,
        incluir_testes: bool = True,
        incluir_docstrings: bool = True
    ) -> RespostaQwen:
        """
        Gera código Python para resolver um problema de Fenômenos de Transporte.
        
        Parâmetros
        ----------
        descricao : str
            Descrição do problema a ser resolvido.
        linguagem : str
            Linguagem de programação (padrão: 'python').
        capitulo : int, opcional
            Capítulo do livro relacionado.
        incluir_testes : bool
            Se True, inclui testes unitários.
        incluir_docstrings : bool
            Se True, inclui docstrings no estilo NumPy.
        
        Retorna
        -------
        RespostaQwen
            Código comentado.
        """
        template = self.templates.get('geracao_codigo', '')
        
        prompt = template.format(
            descricao=descricao,
            linguagem=linguagem,
            capitulo=capitulo or 'não especificado',
            incluir_testes='Sim' if incluir_testes else 'Não',
            incluir_docstrings='Sim' if incluir_docstrings else 'Não'
        )
        
        system_prompt = (
            "Você é um engenheiro especialista em computação científica. "
            "Gere código limpo, eficiente e bem documentado, seguindo PEP 8. "
            "Use bibliotecas científicas padrão (numpy, scipy, matplotlib)."
        )
        
        return self.perguntar(prompt, system_prompt=system_prompt)
    
    # ------------------------------------------------------------------------
    # MÉTODOS UTILITÁRIOS
    # ------------------------------------------------------------------------
    
    def salvar_historico(self, arquivo: Union[str, Path]):
        """Salva o histórico de conversa em arquivo JSON."""
        dados = [
            {
                'role': m.role,
                'content': m.content,
                'timestamp': m.timestamp
            }
            for m in self.historico
        ]
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Histórico salvo em {arquivo}")
    
    def carregar_historico(self, arquivo: Union[str, Path]):
        """Carrega histórico de conversa de arquivo JSON."""
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        self.historico = [
            Mensagem(
                role=d['role'],
                content=d['content'],
                timestamp=d.get('timestamp', time.time())
            )
            for d in dados
        ]
        
        logger.info(f"Histórico carregado de {arquivo} ({len(self.historico)} mensagens)")
    
    def __repr__(self) -> str:
        return (
            f"QwenClient(modelo='{self.modelo}', "
            f"temperatura={self.temperatura}, "
            f"historico={len(self.historico)} mensagens)"
        )


# ============================================================================
# FUNÇÃO AUXILIAR: INSTÂNCIA PADRÃO
# ============================================================================

_client_default: Optional[QwenClient] = None


def get_client(**kwargs) -> QwenClient:
    """
    Retorna uma instância padrão do QwenClient (singleton).
    
    Parâmetros
    ----------
    **kwargs
        Argumentos passados ao construtor de QwenClient.
    
    Retorna
    -------
    QwenClient
        Instância do cliente.
    """
    global _client_default
    if _client_default is None:
        _client_default = QwenClient(**kwargs)
    return _client_default


# ============================================================================
# EXECUÇÃO COMO SCRIPT (TESTES)
# ============================================================================

if __name__ == '__main__':
    # Teste básico (requer QWEN_API_KEY definida)
    try:
        client = QwenClient()
        print(f"Cliente inicializado: {client}")
        
        # Teste simples
        resposta = client.perguntar("O que é a Lei de Fourier? Responda em uma frase.")
        print(f"\nResposta: {resposta}")
        print(f"Tokens usados: {resposta.tokens_usados}")
        print(f"Tempo: {resposta.tempo_resposta:.2f}s")
        
    except ValueError as e:
        print(f"⚠️  {e}")
        print("\nPara testar, defina a variável de ambiente:")
        print("  export QWEN_API_KEY='sua-chave-aqui'")
    except ImportError as e:
        print(f"⚠️  {e}")
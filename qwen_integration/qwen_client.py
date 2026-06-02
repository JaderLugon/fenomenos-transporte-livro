#!/usr/bin/env python3
"""
Cliente para integração com API Qwen (DashScope)
Para uso educacional no livro "Fenômenos de Transporte"

Configuração:
1. Obtenha API Key em: https://dashscope.aliyun.com/
2. Configure variável de ambiente: QWEN_API_KEY
3. Ou passe diretamente no construtor (não recomendado para produção)

Uso básico:
    from qwen_client import QwenClient
    client = QwenClient()
    resposta = client.ask(chapter="cap4", topic="Colebrook-White", level="graduation")
"""

import os
import json
import logging
from pathlib import Path
from typing import Optional, Dict, List, Union
from dataclasses import dataclass, field
from datetime import datetime

try:
    from dashscope import Generation
    from dashscope.api_entities.dashscope_response import GenerationResponse
    DASHSCOPE_AVAILABLE = True
except ImportError:
    DASHSCOPE_AVAILABLE = False
    logging.warning("dashscope não instalado. Execute: pip install dashscope")

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class ChapterContext:
    """Contexto estruturado de um capítulo para prompts da IA."""
    chapter_id: str
    title: str
    volume: int
    key_concepts: List[str]
    equations: Dict[str, str] = field(default_factory=dict)
    examples: List[Dict] = field(default_factory=list)
    difficulty_levels: List[str] = field(default_factory=lambda: ["graduation", "postgrad"])
    
    def to_prompt_snippet(self) -> str:
        """Converte contexto para formato de prompt."""
        lines = [
            f"### CONTEXTO DO CAPÍTULO {self.chapter_id.upper()}",
            f"**Título**: {self.title}",
            f"**Volume**: {self.volume}",
            f"**Conceitos-chave**: {', '.join(self.key_concepts)}",
        ]
        if self.equations:
            lines.append("\n**Equações principais**:")
            for name, eq in self.equations.items():
                lines.append(f"- {name}: `{eq}`")
        return "\n".join(lines)


class QwenClient:
    """
    Cliente simplificado para API Qwen com foco educacional.
    
    Recursos:
    - Templates de prompt pré-configurados para Fenômenos de Transporte
    - Cache de respostas para reduzir chamadas à API
    - Formatação de saída em Markdown/LaTeX
    - Modo offline com respostas pré-definidas (fallback)
    """
    
    # Modelos suportados
    SUPPORTED_MODELS = {
        "qwen-turbo": {"cost": "baixo", "speed": "rápido", "context": "8k"},
        "qwen-plus": {"cost": "médio", "speed": "balanceado", "context": "32k"},
        "qwen-max": {"cost": "alto", "speed": "detalhado", "context": "32k"},
    }
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "qwen-plus",
        cache_dir: Optional[Path] = None,
        offline_mode: bool = False
    ):
        """
        Inicializa o cliente Qwen.
        
        Args:
            api_key: Chave da API DashScope (ou use variável QWEN_API_KEY)
            model: Modelo a ser usado (ver SUPPORTED_MODELS)
            cache_dir: Diretório para cache de respostas
            offline_mode: Se True, usa apenas respostas pré-definidas
        """
        self.api_key = api_key or os.getenv("QWEN_API_KEY")
        self.model = model
        self.offline_mode = offline_mode
        
        if not self.api_key and not offline_mode:
            logger.warning(
                "QWEN_API_KEY não configurada. Usando modo offline.\n"
                "Para habilitar API: export QWEN_API_KEY='sua-chave'"
            )
            self.offline_mode = True
        
        if model not in self.SUPPORTED_MODELS:
            logger.warning(f"Modelo '{model}' desconhecido. Usando 'qwen-plus'.")
            self.model = "qwen-plus"
        
        # Configura cache
        self.cache_dir = cache_dir or Path.home() / ".fen-trans" / "qwen_cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Carrega contextos dos capítulos
        self.chapter_contexts = self._load_chapter_contexts()
        
        logger.info(f"QwenClient inicializado | Modelo: {model} | Offline: {offline_mode}")
    
    def _load_chapter_contexts(self) -> Dict[str, ChapterContext]:
        """Carrega metadados dos capítulos para contextualização."""
        # Em produção, isso viria de um arquivo JSON/YAML
        # Aqui usamos exemplos mínimos
        return {
            "cap4": ChapterContext(
                chapter_id="cap4",
                title="Escoamento em Tubulações e Bombeamento",
                volume=1,
                key_concepts=[
                    "Equação de Bernoulli", "Perda de carga", 
                    "Fator de atrito", "Colebrook-White", "Bombas"
                ],
                equations={
                    "Bernoulli": "p1/γ + z1 + V1²/2g = p2/γ + z2 + V2²/2g",
                    "Darcy-Weisbach": "hf = f·(L/D)·(V²/2g)",
                    "Colebrook-White": "1/√f = -2·log10(ε/(3.7D) + 2.51/(Re·√f))"
                },
                examples=[
                    {
                        "id": "ex4.1",
                        "title": "Sistema de Bombeamento Residencial",
                        "level": "graduation",
                        "description": "Dimensionamento de bomba para prédio de 12 pavimentos"
                    }
                ]
            ),
            # ... adicionar outros capítulos conforme necessário
        }
    
    def _build_prompt(
        self,
        chapter: str,
        topic: str,
        level: str = "graduation",
        question: str = "",
        template: str = "explicacao"
    ) -> str:
        """Constrói prompt estruturado para a IA."""
        ctx = self.chapter_contexts.get(chapter)
        
        templates = {
            "explicacao": f"""
Você é um professor especialista em Fenômenos de Transporte.

{ctx.to_prompt_snippet() if ctx else ""}

**Tópico da consulta**: {topic}
**Nível do aluno**: {level}
**Pergunta**: {question}

Instruções:
1. Responda em português do Brasil, claro e didático
2. Use notação matemática em LaTeX entre $...$ para equações
3. Para nível 'graduation': foco em conceitos e aplicações práticas
4. Para nível 'postgrad': inclua derivações, análise dimensional, limitações
5. Se houver equações relevantes, mostre a forma final e explique cada termo
6. Termine com uma dica prática ou pergunta reflexiva

Resposta:
""",
            "exercicio": f"""
Você é um tutor de Fenômenos de Transporte.

{ctx.to_prompt_snippet() if ctx else ""}

**Exercício**: {question}
**Capítulo**: {chapter}
**Nível**: {level}

Instruções:
1. Resolva passo a passo, mostrando o raciocínio
2. Destaque hipóteses e aproximações utilizadas
3. Verifique consistência dimensional em cada passo
4. Interprete fisicamente o resultado final
5. Sugira uma variação do exercício para aprofundamento

Solução:
""",
            "codigo": f"""
Você é um desenvolvedor científico especializado em Python para Engenharia.

{ctx.to_prompt_snippet() if ctx else ""}

**Tarefa**: {question}
**Contexto**: {topic}
**Nível**: {level}

Instruções:
1. Forneça código Python limpo, com docstrings e type hints
2. Use numpy/scipy para cálculos, matplotlib para plots
3. Inclua comentários explicando a física por trás do código
4. Adicione um bloco de teste mínimo ao final
5. Se aplicável, mostre como validar com solução analítica

Código:
"""
        }
        
        return templates.get(template, templates["explicacao"]).strip()
    
    def _get_cache_key(self, prompt: str) -> str:
        """Gera chave única para cache baseada no prompt."""
        import hashlib
        return hashlib.md5(prompt.encode()).hexdigest()[:16]
    
    def _load_from_cache(self, key: str) -> Optional[str]:
        """Tenta carregar resposta do cache."""
        cache_file = self.cache_dir / f"{key}.json"
        if cache_file.exists():
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Verifica se cache não expirou (24h)
                    if (datetime.now().timestamp() - data['timestamp']) < 86400:
                        logger.info(f"✓ Cache hit: {key}")
                        return data['response']
            except Exception as e:
                logger.warning(f"Erro ao ler cache: {e}")
        return None
    
    def _save_to_cache(self, key: str, response: str):
        """Salva resposta no cache."""
        cache_file = self.cache_dir / f"{key}.json"
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'timestamp': datetime.now().timestamp(),
                    'response': response,
                    'model': self.model
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.warning(f"Erro ao salvar cache: {e}")
    
    def _offline_response(self, prompt: str) -> str:
        """Resposta fallback quando offline ou sem API key."""
        return f"""
⚠️ **Modo Offline Ativado**

Para obter respostas da IA Qwen:
1. Cadastre-se em https://dashscope.aliyun.com/
2. Obtenha sua API Key
3. Execute: `export QWEN_API_KEY="sua-chave"`

**Enquanto isso, aqui está um resumo do tópico**:

> *Consulte o capítulo correspondente no livro para:
> - Desenvolvimento teórico completo
> - Exemplos resolvidos passo a passo  
> - Códigos Python nos notebooks associados
> - Exercícios graduados por nível*

📚 **Recursos disponíveis localmente**:
- Notebook: `notebooks/{prompt.split('**Capítulo**:')[1].strip().split()[0] if '**Capítulo**:' in prompt else '00_setup_check.ipynb'}`
- Dados: `data/` pasta do repositório
- LaTeX: `latex/` para compilação do PDF

💡 **Dica**: Use `jupyter lab notebooks/` para explorar os exemplos interativos!
"""
    
    def ask(
        self,
        chapter: str,
        topic: str,
        question: str = "",
        level: str = "graduation",
        template: str = "explicacao",
        use_cache: bool = True
    ) -> str:
        """
        Envia pergunta contextualizada à IA Qwen.
        
        Args:
            chapter: ID do capítulo (ex: 'cap4')
            topic: Tópico específico dentro do capítulo
            question: Pergunta do usuário (opcional, usa topic se vazio)
            level: 'graduation' ou 'postgrad'
            template: Tipo de prompt ('explicacao', 'exercicio', 'codigo')
            use_cache: Se True, tenta usar cache antes de chamar API
            
        Returns:
            Resposta formatada em Markdown
        """
        question = question or f"Explique: {topic}"
        prompt = self._build_prompt(chapter, topic, level, question, template)
        
        # Tenta cache primeiro
        if use_cache:
            cache_key = self._get_cache_key(prompt)
            cached = self._load_from_cache(cache_key)
            if cached:
                return cached
        
        # Modo offline ou sem API key
        if self.offline_mode or not self.api_key:
            response = self._offline_response(prompt)
        elif not DASHSCOPE_AVAILABLE:
            response = "❌ Pacote `dashscope` não instalado. Execute: `pip install dashscope`"
        else:
            try:
                # Chama API Qwen
                response_obj: GenerationResponse = Generation.call(
                    model=self.model,
                    prompt=prompt,
                    api_key=self.api_key,
                    result_format='message'
                )
                
                if response_obj.status_code == 200:
                    response = response_obj.output.choices[0].message.content
                else:
                    logger.error(f"Erro API: {response_obj.status_code} - {response_obj.message}")
                    response = f"❌ Erro na API Qwen: {response_obj.message}"
                    
            except Exception as e:
                logger.error(f"Exceção ao chamar API: {e}")
                response = f"⚠️ Erro de conexão: {str(e)}\n\n" + self._offline_response(prompt)
        
        # Salva no cache se sucesso
        if use_cache and "❌" not in response and "⚠️" not in response:
            self._save_to_cache(cache_key, response)
        
        return response
    
    def solve_exercise(
        self,
        chapter: str,
        exercise_id: Union[str, int],
        show_steps: bool = True,
        **kwargs
    ) -> str:
        """Método conveniente para resolver exercícios."""
        return self.ask(
            chapter=chapter,
            topic=f"Exercício {exercise_id}",
            template="exercicio",
            level=kwargs.get('level', 'graduation'),
            use_cache=kwargs.get('use_cache', True),
            question=kwargs.get('question', f"Resolva o exercício {exercise_id} do capítulo {chapter}")
        )
    
    def generate_code(
        self,
        chapter: str,
        task: str,
        language: str = "python",
        **kwargs
    ) -> str:
        """Método conveniente para gerar código."""
        return self.ask(
            chapter=chapter,
            topic=f"Código: {task}",
            template="codigo",
            level=kwargs.get('level', 'postgrad'),
            question=f"Escreva código em {language} para: {task}",
            use_cache=kwargs.get('use_cache', True)
        )
    
    def clear_cache(self, chapter: Optional[str] = None):
        """Limpa cache de respostas."""
        if chapter:
            # Limpa apenas de um capítulo (heurística simples)
            for f in self.cache_dir.glob("*.json"):
                if chapter in f.name:
                    f.unlink()
                    logger.info(f"Cache removido: {f.name}")
        else:
            # Limpa tudo
            for f in self.cache_dir.glob("*.json"):
                f.unlink()
            logger.info(f"Cache limpo: {self.cache_dir}")


# Função de conveniência para uso rápido
def ask_qwen(
    chapter: str,
    topic: str,
    question: str = "",
    **kwargs
) -> str:
    """Função rápida para perguntas sem instanciar cliente."""
    client = QwenClient()
    return client.ask(chapter, topic, question, **kwargs)


if __name__ == "__main__":
    # Exemplo de uso direto
    import sys
    
    if len(sys.argv) < 3:
        print("Uso: python qwen_client.py <capítulo> <tópico> [pergunta]")
        print("Ex: python qwen_client.py cap4 'Colebrook-White' 'Como resolver iterativamente?'")
        sys.exit(1)
    
    chap = sys.argv[1]
    topic = sys.argv[2]
    question = sys.argv[3] if len(sys.argv) > 3 else ""
    
    client = QwenClient()
    resposta = client.ask(chap, topic, question)
    print("\n" + "="*60)
    print(resposta)
    print("="*60)
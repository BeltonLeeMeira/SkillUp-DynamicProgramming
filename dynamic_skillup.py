import pandas as pd

# ===============================
# 1. Função principal com função interna
# ===============================
def analisar_profissionais():
    """
    Função principal que cria o DataFrame de profissionais,
    ordena os dados com merge sort e apresenta relatórios.
    """

    # Dados simulados (20 profissionais)
    profissionais = [
        {"nome": "Ana", "idade": 28, "profissao": "Desenvolvedora", "pontuacao": 92},
        {"nome": "Lucas", "idade": 33, "profissao": "Analista de Dados", "pontuacao": 85},
        {"nome": "Mariana", "idade": 26, "profissao": "Designer UX", "pontuacao": 73},
        {"nome": "Felipe", "idade": 29, "profissao": "Gestor de Projetos", "pontuacao": 88},
        {"nome": "Camila", "idade": 31, "profissao": "Engenheira de IA", "pontuacao": 95},
        {"nome": "Ricardo", "idade": 40, "profissao": "Professor", "pontuacao": 76},
        {"nome": "Juliana", "idade": 24, "profissao": "Cientista de Dados", "pontuacao": 97},
        {"nome": "Gabriel", "idade": 30, "profissao": "Técnico em Robótica", "pontuacao": 79},
        {"nome": "Paula", "idade": 34, "profissao": "Especialista em Segurança", "pontuacao": 91},
        {"nome": "Bruno", "idade": 22, "profissao": "Desenvolvedor Júnior", "pontuacao": 64},
        {"nome": "Beatriz", "idade": 25, "profissao": "Psicóloga Organizacional", "pontuacao": 83},
        {"nome": "Rafaela", "idade": 27, "profissao": "Analista de RH", "pontuacao": 77},
        {"nome": "Eduardo", "idade": 35, "profissao": "Gerente de Produto", "pontuacao": 89},
        {"nome": "Fernando", "idade": 29, "profissao": "Consultor em IA", "pontuacao": 94},
        {"nome": "Sofia", "idade": 32, "profissao": "Arquiteta de Software", "pontuacao": 98},
        {"nome": "João", "idade": 21, "profissao": "Estagiário TI", "pontuacao": 60},
        {"nome": "Larissa", "idade": 23, "profissao": "Engenheira Ambiental", "pontuacao": 82},
        {"nome": "Vinícius", "idade": 37, "profissao": "Coordenador de Inovação", "pontuacao": 87},
        {"nome": "Patrícia", "idade": 28, "profissao": "Analista de Sustentabilidade", "pontuacao": 84},
        {"nome": "Thiago", "idade": 27, "profissao": "Programador Python", "pontuacao": 90},
    ]

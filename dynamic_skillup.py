import pandas as pd

# Classe para representar cada profissional
class Profissional:
    def __init__(self, nome, idade, profissao, pontuacao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.pontuacao = pontuacao

# Função principal
def analisar_profissionais():
    # Lista de objetos (20 profissionais)
    profissionais = [
        Profissional("Ana", 28, "Desenvolvedora", 92),
        Profissional("Lucas", 33, "Analista de Dados", 85),
        Profissional("Mariana", 26, "Designer UX", 73),
        Profissional("Felipe", 29, "Gestor de Projetos", 88),
        Profissional("Camila", 31, "Engenheira de IA", 95),
        Profissional("Ricardo", 40, "Professor", 76),
        Profissional("Juliana", 24, "Cientista de Dados", 97),
        Profissional("Gabriel", 30, "Técnico em Robótica", 79),
        Profissional("Paula", 34, "Especialista em Segurança", 91),
        Profissional("Bruno", 22, "Desenvolvedor Júnior", 64),
        Profissional("Beatriz", 25, "Psicóloga Organizacional", 83),
        Profissional("Rafaela", 27, "Analista de RH", 77),
        Profissional("Eduardo", 35, "Gerente de Produto", 89),
        Profissional("Fernando", 29, "Consultor em IA", 94),
        Profissional("Sofia", 32, "Arquiteta de Software", 98),
        Profissional("João", 21, "Estagiário TI", 60),
        Profissional("Larissa", 23, "Engenheira Ambiental", 82),
        Profissional("Vinícius", 37, "Coordenador de Inovação", 87),
        Profissional("Patrícia", 28, "Analista de Sustentabilidade", 84),
        Profissional("Thiago", 27, "Programador Python", 90),
    ]

    # Função interna (função dentro de função) - Merge Sort
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
        return merge(esquerda, direita)

    # Função auxiliar do Merge Sort
    def merge(esquerda, direita):
        resultado = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i].pontuacao > direita[j].pontuacao:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    # Ordena a lista
    ordenados = merge_sort(profissionais)

    # Cria um DataFrame para exibição
    df = pd.DataFrame({
        "Nome": [p.nome for p in ordenados],
        "Idade": [p.idade for p in ordenados],
        "Profissão": [p.profissao for p in ordenados],
        "Pontuação": [p.pontuacao for p in ordenados],
    })

    # Saída de resultados
    print("\n===== RELATÓRIO DE QUALIFICAÇÃO PROFISSIONAL =====")
    print(df.to_string(index=False))
    print("---------------------------------------------------")
    media = df["Pontuação"].mean()
    print(f"Média geral: {media:.2f}")
    print(f"Maior pontuação: {df['Pontuação'].max()}")
    print(f"Menor pontuação: {df['Pontuação'].min()}")
    print("---------------------------------------------------")

    # Condicional simples
    if media >= 85:
        print("Desempenho geral: Excelente")
    elif media >= 70:
        print("Desempenho geral: Regular")
    else:
        print("Desempenho geral: Baixo")

    print("---------------------------------------------------")
    print("Top 3 profissionais:")
    for i in range(3):
        p = ordenados[i]
        print(f"{i+1}. {p.nome} - {p.profissao} ({p.pontuacao} pts)")

# Execução principal
if __name__ == "__main__":
    analisar_profissionais()

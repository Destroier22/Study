# Programa para calcular média de notas eniac
'''
Matéria comum
1) Exercícios de Fixação 15%
4) Nota TD 25% 
3) Prova Eletrônica 60%
Matéria de projeto
'''
# Entrada de Dados
print("Bem Vindo ao Cálculo de Média do Eniac")
nomeDisciplina = input("Qual a disciplina que você quer consultar? ")

# Perguntamos ao usuário e transformamos em True se ele digitar "comum"
tipo_materia = input("É uma matéria comum ou projeto? (Responda 'comum' ou 'projeto'): ").lower()
materia_comum = (tipo_materia == "comum")

notaEx = float(input("Digite a nota dos seus exercícios de fixação: "))
notaTD = float(input("Digite a nota do seu TD: "))
notaProva = float(input("Digite a nota da sua Prova: "))

# Subprogramas são iniciados com def 
def media_materia(eh_comum, n_ex, n_td, n_prova):
    if eh_comum:
        # Pesos: 15% (0.15), 25% (0.25) e 60% (0.60)
        m = (n_ex * 0.15) + (n_td * 0.25) + (n_prova * 0.60)
    else:
        # Caso seja matéria de projeto (ajuste a fórmula se houver pesos diferentes)
        m = (n_ex + n_td + n_prova) / 3
    return m

# Chamada da função passando os argumentos corretos
mediaFinal = media_materia(materia_comum, notaEx, notaTD, notaProva)

# Saída de Dados
print(f"A disciplina {nomeDisciplina} tem a média final de {mediaFinal:.2f}")
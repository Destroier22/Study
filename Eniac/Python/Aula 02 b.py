# Programa para calcular média de notas eniac
'''
1) Exercícios de Fixação 15%
4) Nota TD 25% 
3) Prova Eletrônica 60%
'''
#Entrada de Dados
print("Bem Vindo ao Cálculo de Média do Eniac")
nomeDiciplina = input("Qual a diciplina que você quer consultar? ")
notaEx = float(input("Digite a nota do seus execícios de fixação"))
notaTD = float(input("Digite a nota do seu TD: "))
notaProva = float(input("Digite a nota da sua Prova: "))

#Processamento
mediaFinal = notaEx * 0.15 + notaTD * 0.25 + notaProva * 0.6

#Saída de Dados
print(f"A diciplina {nomeDiciplina} tem a média final de {mediaFinal:.2f}")
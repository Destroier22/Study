#Calculadora de IMC
print("Bem-vindo a calculado de IMC")

#Subprograma para calcula imc
def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    imc
    return imc

#Relatório IMC
def resultado_imc(imc):
    if (imc < 18.5):
        print("Abaixo do peso")
    if (18.5 >= imc <= 24.9):
        print("com peso normal")
    if(24.9 > imc <= 29.9):
        print("Obeso")
    if(29.9 > imc <= 34,9):
        print("em Obesidade grau I")
    if(34.9 > imc <=39.9):
        print("Obesidade grau II")
    if(imc > 39.9):
        print("em Obesidade grua III, procure um médico")

peso = input(float("Informe seu peso:"))
altura = input(float("Informe sua altura: "))

imc = calcular_imc(peso,altura)
print(f"seu IMC é {imc:.2f}")

avaliacao_imc=(resultado_imc) 
print(f"Você está {avaliacao_imc:.2f} ")

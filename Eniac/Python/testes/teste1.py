number = int(input("Digite um número: "))
paridade = "par"
mod = number % 2
if number < 0:
    valor = "negativo"
elif number == 0:
    valor = "neutro"
else:
    valor = "positivo"
    
if mod == 1:
    paridade = "ímpar"
print(f"O número {number} é {valor} e {paridade}")
    

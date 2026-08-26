import random

def gerar_ticket(qtd):
    while(cont <= qtd):
        cont = 1
        num = random.randint(10000, 99999)
        print(f"{num}")
        cont += 1

print("Quantos tickets você quer comprar")
qtd = input(int("Tickets: "))


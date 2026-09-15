'''
LIÇÃO 2 — LISTAS + FOR

Conceito:
O for percorre cada elemento de uma sequência, como uma lista.
A variável criada no for recebe um item diferente a cada repetição.

Exemplo:
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

Leia como:
"Para cada fruta em frutas, execute o bloco abaixo."

EXERCÍCIO 1 — FÁCIL
Use um for para exibir cada número no formato "Número: X".

numeros = [5, 10, 15, 20]

Saída esperada:
Número: 5
Número: 10
Número: 15
Número: 15
Número: 20

Não use quatro print() separados.
=========================================================================================
EXERCÍCIO 2 — INTERMEDIÁRIO
Use a lista abaixo:

numeros = [12, 7, 5, 20, 33, 42, 8, 11]

Percorra a lista e descubra:
- quantos números são pares
- quantos números são ímpares
- a soma de todos os números

Não use sum().

NOVO CONCEITO — CONTADORES E ACUMULADORES
Um contador começa normalmente em 0 e aumenta quando alguma condição acontece.
Um acumulador também começa em 0, mas recebe valores que queremos somar ao longo do for.

Exemplo de contador:
contador = 0
for numero in [2, 4, 6]:
    contador = contador + 1

Exemplo de acumulador:
total = 0
for numero in [2, 4, 6]:
    total = total + numero

Formas abreviadas que você verá muito em Python:
contador += 1       # igual a contador = contador + 1
total += numero     # igual a total = total + numero
==========================================================================================
EXERCÍCIO 3 — PRÁTICA COM CONTADOR
idades = [15, 22, 17, 30, 18, 12, 40]

Percorra a lista e descubra:
- quantas pessoas são menores de 18 anos
- quantas pessoas têm 18 anos ou mais

Saída esperada:
Menores: 3
Maiores ou iguais a 18: 4
===========================================================================================
EXERCÍCIO 4 — PRÁTICA COM CONTADOR + ACUMULADOR
vendas = [120, 80, 250, 40, 310, 95]

Percorra a lista e descubra:
- quantas vendas foram de 100 reais ou mais
- quantas vendas foram abaixo de 100 reais
- qual foi o valor total vendido

Não use sum().

Saída esperada:
Vendas de R$100 ou mais: 3
Vendas abaixo de R$100: 3
Total vendido: R$895

IMPORTANTE:
Resolva um exercício por vez. Não apague o enunciado; escreva sua solução na área correspondente.
'''

# EXERCÍCIO 1 — CONCLUÍDO
numeros = [5, 10, 15, 20]

for numero in numeros:
    print(f"número: {numero}")

# EXERCÍCIO 2 — EM ANDAMENTO
numeros = [12, 7, 5, 20, 33, 42, 8, 11]

# Escreva sua solução abaixo:
soma = 0
par = 0
impar = 0 

for numero in numeros:
    mod = numero % 2 
    if mod == 1:
        impar+=1
    else:
        par+=1
    soma += numero
print(f"{par} números são pares\n{impar} são impares\nA soma de todos os números é igual a {soma}")


# EXERCÍCIO 3 — FAÇA APÓS CONCLUIR O 2
idades = [15, 22, 17, 30, 18, 12, 40]

# Escreva sua solução abaixo:
menor = 0
maior = 0
for idade in idades:
    if idade < 18:
        menor+=1
    else:
        maior+=1
print(f"Menores: {menor}\nMaiores ou iguais a 18: {maior}")

# EXERCÍCIO 4 — FAÇA APÓS CONCLUIR O 3
vendas = [120, 80, 250, 40, 310, 95]

# Escreva sua solução abaixo:

maior=0
menor=0
total_faturado = 0

for venda in vendas:
    if venda < 100:
        menor+=1
    else:
        maior+=1
    total_faturado+=venda
print(f"{maior} vendas de 100 reais ou mais.\n {menor}vendas abaixo de 100 reais.\nTotal faturado R${total_faturado}")

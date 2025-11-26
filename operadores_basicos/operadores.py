inteiro = 10
decimal = 3.14
complexo = 3 +4j

print(inteiro, decimal, complexo)
print(f"Tipos: {type(inteiro)}, {type(decimal)}, type{(complexo)}")

#Texto
Texto = "Olá mundo"
print(Texto)
print(f"Tipos: {type(Texto)}")

#Booleano

verdadeiro = True
falso = False
print(verdadeiro)
print(falso)
print(f"Tipos: {type(verdadeiro)}, {type(falso)}")

# coleções

lista = [1, 2, 3]
tupla = (1, 2, 3)
dicionario = {"nome": "Marcos"}
conjunto = {1, 2, 3}
print(lista, tupla, dicionario, conjunto)
print(f"Tipos: {type(lista)}, {type(tupla), type(dicionario), type(conjunto)}")

nome = input ("Digite seu nome: ")

print(f"Olá: {nome} ! Bem vindo ao Python")

idade = int(input("Digite sua idade: "))
print(f"Daqui a 5 anos você terá {idade + 5} anos.")
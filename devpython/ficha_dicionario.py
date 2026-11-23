# -*- coding: utf-8 -*-
"""Ficha - dicionário

UFCD 10805 - Programação em Python
"""

"""1. Criar um Dicionário"""

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Porto",
    "funcao": "Programadora"
}
print(pessoa)

"""2. Aceder Valores do Dicionário"""

print(pessoa["nome"])
print(pessoa["idade"])

"""3. Modificar Valores do Dicionário"""

pessoa["idade"] = 26
print(pessoa)

"""4. Adicionar"""

pessoa["email"] = "ana@teste.com"
pessoa["telefone"] = "912345678"
print(pessoa)

"""5. Remover Pares Chave-Valor"""

pessoa.pop("telefone")
print(pessoa)

"""6. Verificar se uma Chave Existe"""

amigos = {
    "rui": "rui@teste.com",
    "marta": "marta@teste.com",
    "joao": "joao@teste.com"
}

nome = input("Insira o nome de um amigo: ")
nome = nome.lower()

if nome in amigos:
    print("O amigo está na lista")
else:
    print("O amigo não está na lista")

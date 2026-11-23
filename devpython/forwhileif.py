# Tarefa: estruturas de controlo for, while e if
# UFCD 10805 - Programação em Python

# ---------- FOR ----------
# Percorre uma lista de cidades e usa if/elif/else para classificar cada uma
cidades = ['Lisboa', 'Porto', 'Algarve', 'Évora']

print("=== FOR: lista de cidades ===")
for cidade in cidades:
    if cidade == 'Lisboa':
        print(f"{cidade} é a capital")
    elif cidade == 'Porto':
        print(f"{cidade} fica no Norte")
    else:
        print(f"{cidade} é um destino a visitar")

# FOR com range e break: pára quando i for 5
print("\n=== FOR com range e break ===")
for i in range(10):
    if i == 5:
        break
    print(i)

# ---------- WHILE ----------
# Contador com incremento (evita o loop infinito)
print("\n=== WHILE: contador ===")
i = 1
while i < 6:
    print(i)
    i += 1

# ---------- IF / ELSE com input ----------
# Verifica se o número digitado está na lista
print("\n=== IF/ELSE: número na lista? ===")
numeros = [1, 3, 6, 10, 5, 23]
numero_digitado = int(input("Digite um número: "))

if numero_digitado in numeros:
    print(f"O número {numero_digitado} está na lista")
else:
    print(f"O número {numero_digitado} não está na lista")

# ---------- Os três juntos ----------
# WHILE repete o pedido até o utilizador acertar; FOR conta os pares; IF decide
print("\n=== Os três juntos: adivinhar a palavra ===")
segredo = "python"
tentativas = 0

while True:
    palavra = input("Qual é a linguagem do curso? ").lower()
    tentativas += 1
    if palavra == segredo:
        print(f"Certo! Acertaste em {tentativas} tentativa(s).")
        break
    else:
        print("Errado, tenta outra vez.")

pares = 0
for n in range(1, 11):
    if n % 2 == 0:
        pares += 1
print(f"Existem {pares} números pares entre 1 e 10.")
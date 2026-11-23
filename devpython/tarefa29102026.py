import io
import os

import pandas as pd
import mysql.connector
from reportlab.pdfgen import canvas


# 1. Ligação Python com SQL
nome = input("Nome da empresa: ")
setor = input("Setor da empresa: ")

ligacao = mysql.connector.connect(
	host="sql8.freesqldatabase.com",
	database="sql8839629",
	user="sql8839629",
	password="EZvsMKjHlc",
	port=3306,
)
cursor = ligacao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS company (nome TEXT, setor TEXT)")
cursor.execute("INSERT INTO company (nome, setor) VALUES (?, ?)", (nome, setor))
ligacao.commit()
ligacao.close()

# 2. Criar e ler um ficheiro TXT usando io
with open("ficheiro.txt", "w", encoding="utf-8") as ficheiro:
	ficheiro.write("Exemplo de ficheiro de texto.\n")

with open("ficheiro.txt", "r", encoding="utf-8") as ficheiro:
	print(ficheiro.read())

# 3. Criar formandos.txt e inserir cinco nomes usando os
nomes = ["Ana", "Bruno", "Carla", "Diogo", "Eva"]
with open("formandos.txt", "w", encoding="utf-8") as ficheiro:
	for nome in nomes:
		ficheiro.write(nome + os.linesep)

# 4. Criar e ler tinteiros.xlsx usando pandas
dados = pd.DataFrame({"nome": ["Azul", "Preto"], "quantidade": [2, 3]})
dados.to_excel("tinteiros.xlsx", index=False)
print(pd.read_excel("tinteiros.xlsx"))

# 5. Converter o ficheiro TXT para PDF
pdf = canvas.Canvas("ficheiroconvertido.pdf")
texto = pdf.beginText(50, 800)
with open("ficheiro.txt", "r", encoding="utf-8") as ficheiro:
	for linha in ficheiro:
		texto.textLine(linha.rstrip())
pdf.drawText(texto)
pdf.save()

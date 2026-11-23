import csv

with open("Produtos.csv", "r") as file:
	ficheiro = csv.reader(file, delimiter=",")
	for linha in ficheiro:
		print(linha)
import io

with io.open("emails.txt", "r", encoding="utf-8") as ficheiro:
	texto = ficheiro.read()
	print(texto)

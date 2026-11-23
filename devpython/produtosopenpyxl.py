from pathlib import Path

from openpyxl import load_workbook


ficheiro = Path(__file__).with_name("Produtos.xlsx")
livro = load_workbook(ficheiro, data_only=True, read_only=True)

for folha in livro.worksheets:
	print(f"\n{folha.title}")
	for linha in folha.iter_rows(values_only=True):
		print(*linha, sep=" | ")

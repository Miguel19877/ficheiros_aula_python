import mysql.connector

conexao = mysql.connector.connect(
	host="sql8.freesqldatabase.com",
	port=3306,
	user="sql8839629",
	password="EZvsMKjHlc",
	database="sql8839629",
)

verifica = conexao.cursor()

#Verificar se a tabela existe, caso não exista, criar a tabela
verifica.execute("CREATE TABLE IF NOT EXISTS aulas (nome VARCHAR(100), idade VARCHAR(100))")

sql = "INSERT INTO aulas (nome, idade) VALUES (%s, %s)"
dados = ("rita", 18)

verifica.execute(sql, dados)
registros_inseridos = verifica.rowcount

conexao.commit()
verifica.close()
print(registros_inseridos, "registro inserido com sucesso.")
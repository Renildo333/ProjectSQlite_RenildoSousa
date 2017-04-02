
#Author: Renildo Sousa Silva
#Email: sousarenildo61@gmail.com



import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados (database) da aplicação"""

	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None




	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		self.conexao = sqlite3.connect(self.nome)



	def desconecta(self):
		"""Desconecta do banco"""
		try:
			self.conexao.close()
		except AttributeError:
			pass




	def criar_tabelas(self):
		"""Cria as tabelas do banco"""
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					nome TEXT NOT NULL,
					senha VARCHAR(20) NOT NULL,
					cpf VARCHAR(11) UNIQUE NOT NULL,
					email TEXT NOT NULL
			);
			""")

		except AttributeError:
			print('Faça a conexão do banco antes de criar as tabelas.')





	def inserir_cliente(self, nome, senha, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)
				""", (nome, senha, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpf %s já existe!' % cpf)

			self.conexao.commit()

		except AttributeError:
			print('Faça a conexão do banco antes de inserir clientes.')






	def buscar_cliente(self, cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()

			# obtém todos os dados
			cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])

			cliente = cursor.fetchone()
			
			if cliente:
				return True
			return False
		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')



    #Area de fazer login no banco de dados

	def login(self, username, senha):
		try:
			cursor = self.conexao.cursor()
			sql = 'SELECT * FROM clientes WHERE nome=? and senha=?'
			cliente = cursor.execute(sql, [username, senha]).fetchone()
			if cliente:
				print("Logado com sucesso")
			else:
				print("Dados invalido")
		except AttributeError:
			print('Faça a conexão do banco.')




    #Buscar pelo email

	def buscar_email(self, email):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("SELECT * FROM clientes 	WHERE email = ?",[(email)])
			cliente = cursor.fetchone()

			if cliente:
				print("Busca via email encontrda")

			else:
				print("Busca via email nao encontrada")

		except AttributeError:
			print("Faça a conexao entes de buscar o cliente")



	#Remover cliente pelo cpf

	def remover_cliente(self,cpf):
		try:
			cursor = self.conexao.cursor()
			cursor.execute('''DELETE FROM clientes WHERE cpf=?''',[(cpf)])
			self.conexao.commit()
			if cpf:
				print("Excluido com sucesso")
			else:
				print("Cpf nao encontrado")
		except AttributeError:
			print("Faça a conexao com o banco de dados antes")
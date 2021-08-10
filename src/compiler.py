
# --------------------------------------------------------------------------- Imports -------------------------------------------------------------------------- #

# Tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from text_editor import TextEditor as TextEditor

# Auxiliares
import time
import random

# Lexico
from lexico.lexico import Lexico
from lexico.analysis_error import AnalysisError

# Sintatico
from lexico.sintatico import Sintatico

# Semantico
from lexico.semantico import Semantico

# Tabela
from tabulate import tabulate

# ---------------------------------------------------------------------- Classe do Compilador ------------------------------------------------------------------ #

class Compiler(object):

	"""
	Gerencia a tela do Compilador
	"""

	def __init__(self, root):

		# Definir variáveis gerais
		self.root = root
		self.width = self.root.winfo_screenwidth()
		self.height = self.root.winfo_screenheight()

		# Variável para output das mensagens.
		self.message = ""

		# Variável para output do status.
		self.status = ""

		# Variável para guardar o arquivo que está sendo editado.
		self.file = ""

		# Autores.
		self.GROUP = "Equipe: Christyelen Kramel, Luis Augusto Kühn e Thomas Ricardo Reinke"

	def defineFrames(self):

		"""
		Definição dos frames a serem utilizados.
		"""

		# Define o Frame de ferramentas.
		self.FERRAMENTAS = Frame(self.root, width = self.width, height = 70)
		self.FERRAMENTAS.pack(side = TOP, anchor='w')

		# Define o Frame de status.
		self.STATUS = Frame(self.root, width = self.width, height = 30)
		self.STATUS.pack(side =BOTTOM, anchor='w')

		# Define o Frame do editor.
		self.EDITOR = Frame(self.root, width = self.width)
		self.EDITOR.pack(side = TOP, expand = True, fill = BOTH)

		# Define o frame de mensagens
		self.MENSAGENS = Frame(self.root, width = self.width, height = 100)
		self.MENSAGENS.pack(side = TOP, fill = BOTH)

	def isEmpty(self):

		"""
		Checa se o arquivo está apenas com espaços
		"""

		if (len(self.editorBox.getText()) > 0):

			for char in self.editorBox.getText():

				# Se char diferente de espaço em branco, tab, \n
				if (ord(char) not in [32, 10, 9]):

					return False

		return True

	def compile(self, evento = None):

		"""
		Compilação do código.
		"""

		self.clearMessageBox()

		if (self.isEmpty()):

			self.addMessage('nenhum programa para compilar')

		else:

			lexico = Lexico()
			codigo = self.editorBox.getText()
			lexico.setInput(codigo)

			semantico = Semantico()
			sintatico = Sintatico()

			try:

				sintatico.parse(lexico, semantico)

				self.addMessage('programa compilado com sucesso')

			except AnalysisError as e:

				self.addMessage(str(e))

	def showGroup(self, evento = None):

		"""
		Mostra o grupo na caixa de mensagens.
		"""

		self.addMessage(self.GROUP)

	def defineStatus(self, message):

		"""
		Define a mensagem da barra de status
		"""

		self.status =  message
		self.statusBox.config(text = self.status)

	def addMessage(self, message):

		"""
		Adiciona mensagem no final da caixa de mensagens.
		"""

		self.message = message

		self.messageBox.configure(state='normal')
		self.messageBox.insert('end', self.message + '\n')
		self.messageBox.configure(state='disabled')
		self.messageBox.see("end")

	def defineMessage(self, message):

		"""
		Define a mensagem da caixa de mensagens.
		"""

		self.message = message

		self.messageBox.configure(state='normal')
		self.messageBox.delete('1.0', 'end')
		self.messageBox.insert('end', self.message + '\n')
		self.messageBox.configure(state='disabled')
		self.messageBox.see("end")
 
	def save(self, evento = None):

		"""
		Salva o arquivo atual.
		"""

		if (self.file == ''):

			# Escolhe a pasta e o nome do arquivo.
			file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")

			if file is not None:

				self.clearMessageBox()

				text = str(self.editorBox.getText())
				file.write(text)
				file.close()

				self.defineMessage('')

				self.file = file.name
				self.defineStatus('Arquivo salvo em ' + self.file)

		else:

			self.clearMessageBox()

			# Salva automaticamente no arquivo que está sendo editado.
			text = str(self.editorBox.getText())
			file = open(self.file, "w")
			file.writelines(text)
			file.close()

			self.defineStatus('Arquivo salvo em ' + self.file)

	def copy(self, evento = None):

		"""
		Copia o texto selecionado.
		"""

		self.editorBox.copyText()

	def paste(self, evento = None):

		"""
		Cola o texto copiado.
		"""

		self.editorBox.pasteText()

	def cut(self, evento = None):

		"""
		Recorta o texto selecionado.
		"""

		self.editorBox.cutText()

	def open(self, evento = None):

		"""
		Abre arquivo selecionado.
		"""

		select = filedialog.Open(self.root)

		file = select.show()

		if file != '':

			self.clearMessageBox()

			self.file = file
			codigo = open(file, "r")
			text = codigo.read()

			self.editorBox.setText(text)

		self.defineStatus('Arquivo aberto em ' + self.file)

	def new(self, evento = None):

		"""
		Cria um novo arquivo.
		"""

		if str(self.editorBox.getText()) == '':

			# Se o editor estiver vazio apenas cria.
			self.editorBox.clearText()

			self.defineMessage('')
			self.defineStatus('')

			self.file = ''

			self.defineStatus('Novo arquivo criado.')

		else:

			# Se houver texto pergunta antes de criar.
			answer = messagebox.askquestion("Novo arquivo", "Você tem certeza que deseja criar um novo arquivo?", icon='warning')

			if answer == 'yes':

				self.editorBox.clearText()

				self.defineMessage('')
				self.defineStatus('')

				self.file = ''

				self.defineStatus('Novo arquivo criado.')

	def clearMessageBox(self):

		self.messageBox.configure(state='normal')
		self.messageBox.delete('1.0', 'end')
		self.messageBox.configure(state='disabled')
		self.messageBox.see("end")

	def keyController(self):

		"""
		Controla as teclas pressionadas.
		"""

		self.root.bind("<Control-s>", self.save)
		self.root.bind("<Control-o>", self.open)
		self.root.bind("<Control-n>", self.new)
		self.root.bind("<F1>", self.showGroup)
		self.root.bind("<F9>", self.compile)

	def createButtons(self):

		"""
		Cria os botões.
		"""

		# Botão Novo
		self.imageNew = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoBAMAAAB+0KVeAAAAHlBMVEUAAABPjcpOjclNjcpcl9BcmNBHiMfT5/nf8P7///8f2X56AAAABnRSTlMAyczN/v7/dcq+AAAAAWJLR0QJ8dml7AAAAEhJREFUKM9jYCAFpMFAEpJg5kwoSBXAIpjujEUwo8QAi2C7MxbBDoRSJEGEUiRBhFJkQbhSuCDYB+iCIDBtVHBEC6ahAJJyBgBuThGP4OkA8AAAAABJRU5ErkJggg==').subsample(1)
		buttonNew = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Novo [ctrl-n]", image = self.imageNew, command = self.new, compound = TOP)
		buttonNew.pack(side = LEFT)

		# Botão Abrir
		self.imageOpen = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAAArlBMVEUAAABJhsJJisZIichMi8lLjMlOjslOjclTkMtJichjnNFMjMlXlM+Br9tNjMlHiMdKishMjMlQjspRj8tTkMxTkcxcmNFemNBhmtBooNZsotVtpdpwp9txp9t6rNt6r+B/rtuDst2DteSKtuCNvemRwOuXv+SXxe6ew+ahzPSmyems1Pmt1fmz0u602v223P631O+31e++2fLB3PPP5fjQ5fnZ7Pza7Pzf8P7////YVbL6AAAAD3RSTlMAFT9qjY6cnc/u7/P09vcA+fq5AAAAAWJLR0Q51wCVQAAAAMhJREFUOMvV0dcOgkAQheEBG9axY8WuCNjbvv+TuRliJGHjzKWc6w/IzwBkYfhd/jc8fRbVCjLIyATUEk1LQ/P+D0ZjU085BTfdxVOldnEIholH3asyzC8R3I0Us3qO4HLFwYpNcBJwsGER7N8Y96jS7zm2Xgw8OwT3Lvdlv0hw7UmiNZxtJdEaDg+SaA17d0k0YNhRkmhA/oAUDcgfkKIBp4EoGpA9YBwNyB4wjgZ0ZdGAniwamuwB5xQNbfaAAzt+I7KzIBt7A6yKy1sUV/yvAAAAAElFTkSuQmCC').subsample(1)
		buttonOpen = Button(self.FERRAMENTAS, width =  100, height = self.FERRAMENTAS.winfo_height(), text = "Abrir [ctrl-o]", image = self.imageOpen, command = self.open, compound = TOP)
		buttonOpen.pack(side = LEFT)

		# Botão Salvar
		self.imageSave = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAAAUVBMVEUAAACJdqGOeaSMd6KCeJ1meY9tfZRufpRygplzhJt4i5yBd5yLdaGqqM27u9bC6P/D0NrE0NvF0tzGuubHvN3IvejIvt/Wze/c1fLh6/L///+rX7HNAAAABXRSTlMAQfT3+lWbjp0AAAABYktHRBp1Z+QyAAAAi0lEQVQ4y+3VwQ7CIAyA4eHEAaJuQxT2/g865pLZLl17WqLG/9rvQAoJVbVDful80qjmqBBMr0IIps+ozhwUCXVepR9QktA5N8EEJQuh5CGQAnxLCS5ShOlei+uZR8lDGMvCO+xaS8FnDBeDr9BeKcj1XdAxYThs9lHwRvQ/42+eUYYl7oVP8z2+hBGkqWiQDu71wAAAAABJRU5ErkJggg==').subsample(1)
		buttonSave = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Salvar [ctrl-s]", image = self.imageSave, command = self.save, compound = TOP)
		buttonSave.pack(side = LEFT)

		# Botão Copiar
		self.imageCopy = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAAAYFBMVEUAAABVgIBkdpJqe41leo9meY/FmVTFmFXGmVRleY5meI9meY9meI9meY9meY9neo9neY5oeY5oeo1oeo5neo7DllRmeY92gYx4i5zCllPMrX3NrX3y+v/zwHT1wnb////0N3s6AAAAFnRSTlMABhwdiImen6C1tsDB5eb19vv7+/z9U/Go8gAAAAFiS0dEHwUNEL0AAACWSURBVDjL7dRbD4IgFMDxI9D9hhXQKeT7f0wVVFhx6aVWm/8Hx/A3x3kQgOeqxfHAKijHNoRsWeLlWqBNdnECQE/9yu2JVQBFY2wT5P3K7TUigGg8vOwp3dUeGkxAeeX8LAtQySCVgfdAqkcGRpuhh7cuHXm8Qh3tG1An+qUzzsP86TDjtVccZjlcpIiFL/o+APO/6xu1GZ9/EHytMKUAAAAASUVORK5CYII=').subsample(1)
		buttonCopy = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Copiar [ctrl-c]", image = self.imageCopy, command = self.copy, compound = TOP)
		buttonCopy.pack(side = LEFT)

		# Botão Colar
		self.imagePaste = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAAAY1BMVEUAAABVgIBkdpJqe41leo9meY/FmVTFmVTFmFXGmVRleY5meI9meY9meI9meY9meY9neo9neY5oeY5oeo1oeo5neo7DllRmeY93iJt3iJzCllPT2d/U2d/ywHXzwHT1wnb///8o/LjRAAAAF3RSTlMABhwdiImdnp+gtbbAweXm9fb7+/v8/W486dYAAAABYktHRCCzaz2AAAAAiUlEQVQ4y+3U0RKCIBCF4RWwMjWjdFEq8f2fUtHKHQWbcaY7/itm+a4PwLIoLi4igt+JM2Op8HwmqMfUkGQA/Gpf0w1PBGJrxr5Q2td0a5FAbWZY5pxntxka7YGqkvKuNmA3VCtSYy8e+CCyeW7AdQEGGGCAy5Fytgt+htTViw7p8T3NrvAA/6kHTYl/Bks/wIMAAAAASUVORK5CYII=').subsample(1)
		buttonPaste = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Colar [ctrl-v]", image = self.imagePaste, command = self.paste, compound = TOP)
		buttonPaste.pack(side = LEFT)

		# Botão Recortar
		self.imageCut = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAABzlBMVEUAAADMQEDCSUnFRkbERUWOeKONcqHIR0fJRUXHRESNeKKOeaOPeKONd6OMdqSOdqKKdaCNdaOLdqOLdqWMd6ONeaSOeKWPdJ+QdqDJRUXJRETKRkaOdaKMd6TJRUXIRUXJRUXJR0eQfKaPe6WzV2iyWGqzV2azV2mzWWmzWGiyWWmyWGrLSEjLSEjKR0fKSEjISUyPeqWQeaXJRUWSfaeSfanIRkbJRkbVWVnWWlqPeqSSfqiTfamTfqrJRUXKSUnUWFjUWlrJSEjKSEjIRESQe6fJRUXaYWHaYmLbYmLbY2OQe6eRfaiSfqjIRUXJRkaSfaiTfajIRUXJRUW1psu1p8q7VWCMdqGNdqKNd6LBUFeLdaGMd6ONd6PJTE7KTE6LdaGMd6KQe6aRfKeSfamUgKqVgaq8r9K/stW/s9W/s9bDttjEudvJTE7LweHNYWfNZWzOaXDOanHPxubQxOLQxubRxeLRyObRyOfSwt/SyOjSyefSyenSyunUXV7XYWLYYWLZY2Tbzurbz+vb1PHcz+vc1PLc1fLsfn7tfn7tf3/ugIDugYHvg4PwhITxhYXxhobyhobyh4f0ior0i4v1jIz2jo73jo73j4////+BmsuWAAAAYHRSTlMAFBUWGiQmU1VWYGFmZ2hoaWlsbm9wcXJzent8foOFhoiJoaSkpqeoqqusrdzd3t7l6+zz9PT09PT09fX19fX19fX29vf4+Pj4+Pj5+fn5+fr6+vr7/Pz9/f39/v7+/v7IQLnGAAAAAWJLR0SZAdY2qAAAAf9JREFUOMtjYKAJYFbU8/PTVWAmpI7T3Ktz6tROL3MOAurse2aAQY89XpXM5j0zJlkEBzv0zugxY0KRYlM2Ck8AgWgBIE/Ra8YkJ0kWFimniTM85JHVcVuFVrS0t7dX2QiBuPpdMyykQAwpyxldOkjqhGxK29sR6hjcpswIYgExWPxnTHFDqOOzrgarqzUVZoApDIYpnGyHWx2DbifUammLGV0GuNUxKHjO6HWSAnrGuW/GhFwNnOrAwTPR0t/fsQ8YlP252rjUMTBwwAIcCKY3REngUgdUaebZMWVy1ySgwsb8SltRXOoYGJjkddzsDHL7p9UXNLVXefviUgcFanF1hc3t7empBNQxMKiElQDVpRFUx8DAb1KRnlaekdEGUieCLyXxuqZWZyQkZLbXBuBVx8DnU90OUlibEiuLT50gKFzaMrNqUhITIsVwq1MNK4P4A6guOcdWFJc69dy6omaouqS89losKkG5EBrgre1VgTEgde1YVIJzITwKTUVkIrIhTkBTyYmaKMTB4YlFJVIuBCazeC2QGA82lci5cEKuJjTkrTFVouRCeFbAohI5FyJlLkyVyLlwigsDbpXIubADtQAoRikAkHOhuxxyuHFZhSAXKUi5sNuYESWEWZUMkQopRC7stmfHX0CCc+GUDnczdkJFLigXuunIMTLQFQAAP8sGL2zdy3IAAAAASUVORK5CYII=').subsample(1)
		buttonCut = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Recortar [ctrl-x]", image = self.imageCut, command = self.cut, compound = TOP)
		buttonCut.pack(side = LEFT)

		# Botão Compilar
		self.imageCompile = PhotoImage(data = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAABcVBMVEUAAACAgP9VqqpAgL9AgL9VjsZNgMxNjMxJhsJGi8VIh8dGi8lJisVHh8ZGh8lHh8dFh8hHh8ZHiMdGh8dGiMhIh8ZHiMZGicdIiMhIiMZIichHiMZMjMlMi8pJi8pLi8pKi8lMi8lLjMpMjMtNi8tNjctMjctMjstMjcxMjcpNjstLjMpMjMtMjctMjctKjMpLi8lMi8lKispNjctNjMtMjctNjMpLjMlLi8pKi8pKjMpKi8pLishVldJWldFWldJWltJXltJJi8hJi8lWldJKislOjsxPjsxgnthjn9lKiclgnddhndhhntdhnthjn9pjoNpkn9pkoNpkoNtMi8pMjMpgn9ltqOBuqOBIichIicd5s+l6sul/t+2AuO2AuO6HvvGHvvKIvvKRxviSx/mUyPqUyfqWyvuWyvyWy/yXy/yXzP2YzP2azf2g0P2p1P2q1f232/663f7I5P7W6/7i8P7k8f7w9//4/P/9/v/////BY0oXAAAAW3RSTlMAAgMECAkKFBUWICEjJEJERkhWV1hZWltcZ2prnZ6goKGipK+wsLGys9DR09PT1NXW1tjb3N3e4OHi4uPl8vLy8vLz8/P09PT09PX19fX19fX19fX29vb5+fv8rd/+JAAAAAFiS0dEejjVhWoAAAGkSURBVDjLY2CgMeCV1jD1iopyNVWX4sGtillcLzQoOjElIyMlMTogVEeMCbs6QRvH2KwcOMiKc7AWwKKMTck9PgcNxLkpsqKr4zQKS8vBAGl+hhxo6iwjcrCB7AhLFJVsRtjVAUGEAQuSQqUwXOpysv3kkfzrnoZTYU6aGz88/Gzic/CAWCtYeEq4IETLCjBVOohAFerGIgSrKkvyMIJTCxq/oUjxUVVVVVGci6owM5QbrFA6OAdFYVVVeRGqykBJsEKNaHSFVVWoTo1RBSs0S8JUiOrUBGOwQtcULApRnJrsDFYYlYFVIZJT0yMJKCxEVUi01UR7Ro1w8CiDFUoFYgR4IWqAe0ICnIdgFIZwQRNFHP5EEasJTT1itgjB0nzMZGYnBFXIZB2LL+HGmcMLAgE3PFkh1Y0PkWkUPLJxZi4fWaRcyGqIM7uGayNnVwYOywisZmaHW7CjFhUc+r5Y3Jnqrc2BXviwyrnFYhZSMixYyjN+K8e4TKT4iLU358NeQDKJaoX6x4AL0oQYzxBNYUbchS63pKqJa1SUk7GKJBetqwEAZcmgvBxujJUAAAAASUVORK5CYII=').subsample(1)
		buttonCompile = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Compilar [F9]", image = self.imageCompile, command = self.compile, compound = TOP)
		buttonCompile.pack(side = LEFT)

		# Botão Equipe
		self.imageGroup = PhotoImage(data = b'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').subsample(1)
		buttonGroup = Button(self.FERRAMENTAS, width = 100, height = self.FERRAMENTAS.winfo_height(), text = "Equipe [F1]", image = self.imageGroup, command = self.showGroup, compound = TOP)
		buttonGroup.pack(side = LEFT)

	def createMessageBox(self):

		"""
		Cria a caixa de mensagens.
		"""

		# Define scrollbar do eixo X
		xscrollbar = Scrollbar(self.MENSAGENS, orient = HORIZONTAL)
		xscrollbar.pack(side = BOTTOM, fill = X)

		# Define scrollbar do eixo Y
		yscrollbar = Scrollbar(self.MENSAGENS)
		yscrollbar.pack(side = RIGHT, fill = Y)

		# Define a caixa de mensagens
		self.messageBox = Text(self.MENSAGENS, height = 7, wrap = NONE, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
		self.messageBox.configure(state = "disabled")
		self.messageBox.pack(fill = BOTH)

		# Configura as relações
		xscrollbar.config(command = self.messageBox.xview)
		yscrollbar.config(command = self.messageBox.yview)

	def createStatusBox(self):

		"""
		Cria a caixa de status.
		"""

		self.statusBox = Label(self.STATUS, text = self.status, justify = 'left')
		self.statusBox.pack(side = LEFT, fill = BOTH)

	def run(self):

		"""
		Função geral.
		"""

		# Configurações iniciais.
		self.root.title("Compilador")
		self.root.geometry("900x600")
		self.root.minsize(900, 600) 

		# Criação de Frames.
		self.defineFrames()

		# Atualização dos valores de dimensão.
		self.root.update()

		# Criação de todos os componentes.
		self.createButtons()
		self.createMessageBox()
		self.createStatusBox()
		self.editorBox = TextEditor(self.EDITOR)
		self.editorBox.pack(side = "top", fill = "both", expand = True)
		
		# Loops.
		self.keyController()
		self.root.mainloop()

if __name__ == '__main__':

	root = Tk()

	compiler = Compiler(root)
	compiler.run()

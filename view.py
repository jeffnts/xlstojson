from tkinter import *
from tkinter.filedialog import *
from XlsToJson import controller


class Janela():


  def __init__(self, janela):
      self.containerRaiz = Frame(janela).grid()
      janela.title("Conversor de arquivos XLS para JSON")
      janela.geometry("400x100+300+100")
      janela.resizable(width=False, height=False)
      self.btnCarregar = Button(self.containerRaiz, text="Carregar arquivo.", command = controller.converter).grid(row=1, column=1, padx=6, pady=30)
















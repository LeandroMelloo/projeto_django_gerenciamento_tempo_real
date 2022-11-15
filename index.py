# importar as bibliotecas
from tkinter import *
from tkinter import messagebox

# criar nossa janela
jan = Tk()
jan.title("DP Systems - Access Painel")
jan.geometry("800x400")
jan.configure(background="white")
jan.resizable(width=False, height=False)

LeftFrame = Frame(jan, width=300, height=400, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=500, height=400, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

jan.mainloop()
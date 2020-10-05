# import tkinter
#
#
# class GUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#
#         # Frame
#         self.frame1 = tkinter.Frame(self.main_window, height=70, width=900)
#         self.frame2 = tkinter.Frame(self.main_window, height=70, width=400)
#
#         # Labels
#         self.label1 = tkinter.Label(self.main_window, text="texto em cima", bg='black', fg='white')
#         self.label2 = tkinter.Label(self.main_window, text="texto em baixo", bg='green', fg='red')
#         self.label3 = tkinter.Label(self.main_window, text="texto esquerda", bg='blue', fg='yellow')
#         self.label4 = tkinter.Label(self.main_window, text="texto direita", bg='white', fg='black')
#         self.label_frame = tkinter.Label(self.frame1, text="Cores para 'background'")
#         self.label_frame2 = tkinter.Label(self.frame2, text="https://www.w3schools.com/colors/colors_names.asp")
#
#         # Pack Frame
#         self.frame1.pack()
#         self.frame2.pack()
#
#         # Pack Label
#         self.label_frame2.pack(side='bottom')
#         self.label_frame.pack(side='top', fill=tkinter.X)
#         self.label1.pack(side='top', fill=tkinter.X)
#         self.label3.pack(side='left', fill=tkinter.Y)
#         self.label4.pack(side='right', fill=tkinter.Y)
#         self.label2.pack(side='bottom', fill=tkinter.X)
#
#         tkinter.mainloop()
#
#
# GUI()
# ******************************************
# from tkinter import *
# from tkinter import messagebox
#
#
# class GUI:
#     def __init__(self):
#         self.window = Tk()
#
#         # criação de frames
#         self.frameInput = Frame(self.window)
#         self.frameButton = Frame(self.window)
#
#         # definição do frame de entrada de dados
#         self.labelInput = Label(self.frameInput, text='Informe seu nome: ')
#         self.userNameInput = Entry(self.frameInput, width=50)
#
#         # pack entrada de dados
#         self.labelInput.pack(side='left')
#         self.userNameInput.pack(side='left')
#
#         # definição do frame dos botoes
#         self.botaoClick = Button(self.frameButton, text='Enviar', command=self.botao_press, width=10)
#         self.botaoQuit = Button(self.frameButton, text='Sair', command=self.window.quit, width=10)
#
#         # pack botoes
#         self.botaoClick.pack(side='left')
#         self.botaoQuit.pack(side='left')
#
#         # pack frames
#         self.frameInput.pack()
#         self.frameButton.pack()
#
#         mainloop()
#
#     def botao_press(self):
#         messagebox.showinfo("Olá", "Bem vindo, " + self.userNameInput.get())
#
#
# GUI()
# ******************************************
# from tkinter import *
# from tkinter import messagebox
#
#
# class GUI:
#     def __init__(self):
#         self.main = Tk()
#         self.main.geometry("250x100")
#
#         self.frame_pergunta = Frame(self.main)
#         self.frame_botao = Frame(self.main)
#
#         self.labelTitle = Label(self.frame_pergunta, text='Selecione uma opção: ').pack()
#
#         self.radioOption = IntVar()
#         self.radioOption.set(0)
#
#         self.check = Radiobutton(self.frame_pergunta, text='Ver Check button', variable=self.radioOption, value=1).pack(
#             anchor='w')
#         self.sair = Radiobutton(self.frame_pergunta, text='Sair', variable=self.radioOption, value=2).pack(anchor='w')
#
#         self.botao_enviar = Button(self.frame_botao, text='Enviar', command=self.envio)
#
#         self.frame_pergunta.pack()
#         self.frame_botao.pack()
#         self.botao_enviar.pack(side='left')
#
#         mainloop()
#
#     def envio(self):
#         opcao = self.radioOption.get()
#         if opcao == 1:
#             Checkbox()
#         elif opcao == 2:
#             self.main.quit()
#
#
# class Checkbox:  # ERRO. não executa com 2 janelas pq??
#     def __init__(self):
#         self.janela = Tk()
#
#         self.frame_check = Frame(self.janela)
#         self.frame_botao = Frame(self.janela)
#
#         self.check_var1 = IntVar()
#         self.check_var2 = IntVar()
#         self.check_var3 = IntVar()
#
#         self.check_var1.set(0)
#         self.check_var2.set(0)
#         self.check_var3.set(0)
#
#         self.opcao1 = Checkbutton(self.janela, text='Opção 1', variable=self.check_var1).pack(anchor='w')
#         self.opcao2 = Checkbutton(self.janela, text='Opção 2', variable=self.check_var2).pack(anchor='w')
#         self.opcao3 = Checkbutton(self.janela, text='Opção 3', variable=self.check_var3).pack(anchor='w')
#
#         self.btn_envio = Button(self.frame_botao, text='Enviar', command=self.option)
#
#         self.btn_envio.pack(side='left')
#         self.frame_check.pack()
#         self.frame_botao.pack()
#
#     def option(self):
#         select = True
#
#         self.texto = "Itens selecionados: \n"
#
#         if self.check_var1.get() == 1:
#             self.texto += 'Opção 1\n'
#             select = False
#         if self.check_var2.get() == 1:
#             self.texto += 'Opção 2\n'
#             select = False
#         if self.check_var3.get() == 1:
#             self.texto += 'Opção 3\n'
#             select = False
#         if select:
#             self.texto += "Não foram selecionadas nenhuma das opções."
#
#         messagebox.showwarning("AVISO!!", self.texto)
#         self.janela.quit()
#
#
# GUI()
# ******************************************
# from tkinter import *
# from tkinter import messagebox
#
#
# def exibe(event):
#     # Pegando o nome do widget
#     nome_caixa = event.widget.winfo_name()
#     # Pegando o conteúdo do widget
#     conteudo_caixa = event.widget.get()
#     messagebox.showinfo("Texto na caixa", nome_caixa + ": " + conteudo_caixa)
#
#
# def tratar_evento(event):
#     master = Tk()
#     master.title("Componentes de entrada")
#     master.geometry("325x100")  # width x length
#
#     # Criando o primeiro frame que vai armazenar
#     # as duas primeiras caixas de entrada
#     frame1 = Frame(master)
#     frame1.pack(pady=5)
#
#     # Criando a primeira caixa de entrada
#     text1 = Entry(frame1, name="caixa1")
#
#     # Associando o evento <Return> com o
#     # event handler exibe()
#     text1.bind("<Return>", exibe)
#     text1.pack(side=LEFT, padx=5)
#
#     # Criando a segunda caixa e seu bind
#     text2 = Entry(frame1, name="caixa2")
#     text2.insert(INSERT, "Digite um texto aqui")
#     text2.bind("<Return>", exibe)
#     text2.pack(side=LEFT, padx=5)
#
#     # Segundo frame, com as duas outras caixas
#     frame2 = Frame(master)
#     frame2.pack(pady=5)
#
#     # Criando a caixa que não dá pra editar
#     text3 = Entry(frame2, name="caixa3", state=DISABLED)
#     text3.insert(INSERT, "Texto ineditável")
#     text3.bind("<Return>", exibe)
#     text3.pack(side=LEFT, padx=5)
#
#     # Criando a caixa estilo senha
#     text4 = Entry(frame2, name="caixa4", show="*")
#     text4.insert(INSERT, "Texto escondido")
#     text4.bind("<Return>", exibe)
#     text4.pack(side=LEFT, padx=5)
#
#
# janela = Tk()
# janela.geometry("250x100")
# frame = Frame(janela)
# label = Label(frame, text='Clique aqui para abrir uma nova janela')
# label.bind("<Button-1>", tratar_evento)
# frame.pack()
# label.pack(pady=10)
#
# janela.mainloop()
# ******************************************
# from tkinter import *
# from tkinter import messagebox
#
#
# class ButtonEvent:
#     def __init__(self):
#         self.master = Tk()
#         self.master.title("Botão")
#         self.master.geometry("120x40")
#
#         self.botao = Button(self.master, text="Clique aqui", command=self.apertou)
#         self.botao.bind("<Enter>", self.passou_por_cima)
#         self.botao.bind("<Leave>", self.saiu_de_cima)
#         self.botao.pack(side=LEFT, padx=5, pady=5)
#
#         mainloop()
#
#     def apertou(self):
#         messagebox.showinfo("Mensagem", "Você apertou o botão")
#
#     def passou_por_cima(self, event):
#         event.widget.config(relief=GROOVE)
#
#     def saiu_de_cima(self, event):
#         event.widget.config(relief=RAISED)
#
#
# ButtonEvent()
# # ******************************************
# from tkinter import *
#
#
# class MouseEvents(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title("Eventos com Mouse")
#         self.master.geometry("300x200")
#
#         self.stringLabel = StringVar()
#         self.stringLabel.set("Mouse fora da janela")
#
#         self.label = Label(self, textvariable=self.stringLabel)
#
#         self.bind("<Button-1>", self.mouseClick)
#         self.bind("<ButtonRelease-1>", self.mouseRelease)
#         self.bind("<Enter>", self.mouseEnter)
#         self.bind("<Leave>", self.mouseLeave)
#         self.bind("<B1-Motion>", self.mouseArraste)
#
#         self.label.pack(pady=10, padx=10, side=BOTTOM)
#
#         mainloop()
#
#     def mouseClick(self, event):
#         self.stringLabel.set("Mouse clicado nas coordenadas X: " + str(event.x) + "e Y: " + str(event.y))
#
#     def mouseRelease(self, event):
#         self.stringLabel.set("Mouse solto nas coordenadas X: " + str(event.x) + "e Y: " + str(event.y))
#
#     def mouseEnter(self, event):
#         self.stringLabel.set("Mouse na janela")
#
#     def mouseLeave(self, event):
#         self.stringLabel.set("Mouse fora da janela")
#
#     def mouseArraste(self, event):
#         self.stringLabel.set("Mouse arrastado até X: " + str(event.x) + "e Y: " + str(event.y))
#
#
# MouseEvents()
# ******************************************
# from tkinter import *
#
#
# class TecladoEvento(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.pack(expand=YES, fill=BOTH)
#         self.master.title("Eventos de teclado")
#         self.master.geometry("250x50")
#
#         self.stringLabel = StringVar()
#         self.stringLabel.set('Pressione alguma tecla')
#
#         self.label = Label(self, textvariable=self.stringLabel)
#         self.label.pack(pady=15)
#
#         self.master.bind("<KeyPress>", self.keyPress)
#         self.master.bind("<KeyRelease>", self.keyRelease)
#         self.master.bind("<KeyPress-Control_L>", self.ctrlPress)
#         self.master.bind("<KeyRelease-Control_L>", self.ctrlRelease)
#
#         mainloop()
#
#     def keyPress(self, event):
#         self.stringLabel.set("Tecla " + event.char + ' pressionada.')
#
#     def keyRelease(self, event):
#         self.stringLabel.set("Tecla " + event.char + ' solta.')
#
#     def ctrlPress(self, event):
#         self.stringLabel.set("Pressionada a tecla control.")
#
#     def ctrlRelease(self, event):
#         self.stringLabel.set("Solta a tecla control.")
#
#
# TecladoEvento()
# from tkinter import *
#
#
# class Grid(Frame):
#     def __init__(self):
#         # Inicializando o frame
#         Frame.__init__(self)
#         self.master.title("Grid")
#         self.master.geometry("80x80")
#
#         # Criando os labels e adicionando
#         # com o método grid()
#         for linha in range(3):
#             for coluna in range(3):
#                 Label(self.master, text=str(linha) + ',' + str(coluna)).grid(row=linha, column=coluna)
#         Label(self.master, text="0x10").grid(row=1000, column=1)
#         mainloop()
#
#
# Grid()
# ******************************************
# # Com barra de rolagem visível
# from tkinter import *
#
# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# mylist = Listbox(root,)
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
#
# mainloop()
# ******************************************
# # Sem barra de rolagem visível
# from tkinter import *
#
# root = Tk()
# # scrollbar = Scrollbar(root)
# # scrollbar.pack(side=RIGHT, fill=Y)
#
# mylist = Listbox(root,)
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
#
# mylist.pack(side=LEFT, fill=BOTH)
# # scrollbar.config(command=mylist.yview)
#
# mainloop()
# ******************************************

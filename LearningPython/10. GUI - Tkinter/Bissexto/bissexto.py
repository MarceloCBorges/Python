from tkinter import *


class Year(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Ano Bissexto')
        self.master.geometry('260x200')

        self.dataLabelUP = Label(self)
        self.dataLabelDown = Label(self)
        self.btnLabel = Label(self)
        self.respostaLabel = Label(self, relief="ridge")

        self.startDateLabel = Label(self.dataLabelUP, text='Ano de início: ')
        self.startEntry = Entry(self.dataLabelUP, width=5)
        self.endDateLabel = Label(self.dataLabelDown, text='Ano final: ')
        self.endEntry = Entry(self.dataLabelDown, width=5)
        self.btnAnalisa = Button(self.btnLabel, text='Verificar', command=self.numero)

        self.btnAnalisa.bind("<Enter>", self.mouseOn)
        self.btnAnalisa.bind("<Leave>", self.mouseOff)

        self.startDateLabel.pack(side=LEFT)
        self.startEntry.pack(anchor=W)
        self.endDateLabel.pack(side=LEFT)
        self.endEntry.pack(anchor=W)
        self.btnAnalisa.pack(padx=5, pady=1, anchor=E)

        self.barraRolagem = Scrollbar(self.respostaLabel)
        self.barraRolagem.pack(side=RIGHT, fill=Y)

        self.listaResposta = Listbox(self.respostaLabel, yscrollcommand=self.barraRolagem.set)

        self.dataLabelUP.pack(fill=BOTH)
        self.dataLabelDown.pack(fill=BOTH)
        self.btnLabel.pack(fill=BOTH)
        self.respostaLabel.pack(fill=BOTH, padx=2, pady=2)

        mainloop()

    def numero(self):
        while self.listaResposta.get(0) != "":
            self.listaResposta.delete(0)

        try:
            start = int(self.startEntry.get())
            end = int(self.endEntry.get())
            self.checkAno(start, end)
        except ValueError:
            # self.respostaLabel.config(text='Informar somente números.', pady=50)
            self.listaResposta.insert(END, "Informar somente números.")
            self.listaResposta.pack(fill=BOTH)
            self.barraRolagem.config(command=self.listaResposta.yview)

    def checkAno(self, start, end):
        if start > end:
            # self.respostaLabel.config(text='Período de ano inválido.')
            self.listaResposta.insert(END, 'Período de ano inválido.')
        else:
            resposta = "Ano(s) bissextos de acordo com intervalo:\n"
            self.listaResposta.insert(END, resposta)
            for ano in range(start, end + 1):
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    # resposta += str(ano) + '\n'
                    self.listaResposta.insert(END, str(ano))

            # self.respostaLabel.config(text=resposta)
        self.listaResposta.pack(fill=BOTH)
        self.barraRolagem.config(command=self.listaResposta.yview)

    def mouseOn(self, event):
        event.widget.config(relief=GROOVE)

    def mouseOff(self, event):
        event.widget.config(relief=RAISED)


Year()

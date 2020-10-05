from tkinter import *


class ParImparTela(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Número par ou ímpar.")
        self.master.geometry("250x80")

        self.labelUp = Label(self.master)
        self.labelDown = Label(self.master)

        # label IN
        self.labelInput = Label(self.labelUp, text="Informe número: ")
        self.valueInput = Entry(self.labelUp, width=5)
        self.btnCheck = Button(self.labelUp, text='Check', command=self.check)
        self.master.bind("<Return>", self.checkKey)
        # pack IN
        self.labelInput.pack(side=LEFT, pady=5, padx=5)
        self.valueInput.pack(side=LEFT, pady=5, padx=5)
        self.valueInput.insert(INSERT, 0)
        self.btnCheck.pack(side=LEFT, pady=5, padx=5)
        # label OUT
        self.labelOutput = Label(self.labelDown, text="Resultado: ")
        self.valueOutput = Entry(self.labelDown, name="saida")
        # pack OUT
        self.labelOutput.pack(side=LEFT, pady=5, padx=5)
        self.valueOutput.pack(side=LEFT, pady=5, padx=5)

        self.labelUp.pack()
        self.labelDown.pack()

        mainloop()

    def checkKey(self, event):
        self.check()

    def check(self):
        valor = int(self.valueInput.get())
        if not valor == 0:
            if valor % 2 == 0:
                self.valueOutput.insert(INSERT, "Valor é par")
            else:
                self.valueOutput.insert(INSERT, "Valor é ímpar")


ParImparTela()

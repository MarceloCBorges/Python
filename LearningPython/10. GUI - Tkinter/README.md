## Gui - Tkinter

_GUI_ - Graphical User Interface
_Tkinter_ - Tool Kit Interface
_Widgets_ - Componentes de janela 

Módulo _Python_ para interface gráfica.

##### Widgets disponíveis
 
> __Button__: Botão
>
> __Checkbutton__: Botões de check, tipo on e off
>
> __Canvas__: uma área retangular, que podemos colocar e exibir coisas dentro, como uma imagem
>
> __Entry__: um campo de entrada, onde o usuário pode digitar alguma linha de informação
>
> __Frame__: um 'container', uma área que serve pra abrigar e agrupar outros widgets
>
> __Label__: rótulo, uma área que exibe um texto ou uma imagem
>
> __Listbox__: uma lista de opções para o usuário marcar o que quiser
>
> __Menu__: uma lista de opções, um menu, onde o usuário vai clicar em alguma opção e algo vai ocorrer
>
> __Menubutton__: menu que é exibido na tela e pode ser clicado pelo usuário
>
> __Message__: mostra múltiplas linha de texto na tela
>
> __Radiobutton__: botões do tipo radio, onde é permitido escolher apenas uma opção (Masculino ou Feminino, por exemplo)
>
> __Scale__: um widget onde o usuário pode clicar, segurar e mover um ao longo de uma faixa (tipo, aumentar e reduzir o volume)
>
> __Scrollbar__: barra de rolagem
>
> __Text__: permite o usuário digitar múltiplas linhas de texto
>
> __Toplevel__: um container, como um Frame, mas exibe sua própria janela
>
>__messagebox__: caixas de diálogo/mensagem
***
#### Módulo

Importar módulo 

`import tkinter`

Desenvolvimento da GUI se dá através do uso de classes.

`janela = tkinter.Tk()`


Cria classe do tipo _Tk_ e atribui na variável _var_.

`self.janela.geometry("100x200")`

Define tamanho da janela

`tkinter.mainloop()`

Inicia em loop infinito janela principal.

##### Label

`var = tkinter.Label(self.janela)`

Cria uma label(Rótulos) para textos.
> Necessário empacotar (.pack())

##### Frame

`var = tkinter.Frame(self.janela)`

Cria um __Frame__.

> NOTA: A ordem de criação influencia na visualização.
> Necessário empacotar (.pack())

##### Empacotar métodos

`var.pack()`

"Empacota" método da variável

> Sempre empacotar os métodos 

###### Parâmetros pack


`var.pack(fill=tkinter.)`

* _fill=tkinter.X_ ->  Preenche toda a tela na linha horizontal

* _fill=tkinter.Y_ ->  Preenche toda a tela na linha vertical

* _fill=BOTH_ -> Cobre todo o espaço horizontal ou vertical 

* _side='left'_ -> Alinhado a esquerda

* _side='right'_ -> Alinhado a direita

* _side='bottom'_ -> Alinhado em baixo

* _side='top'_ -> Alinhado em cima

* _padx=_ -> Espaçamento horizontal

* _pady=_ -> Espaçamento vertical

* _expand_ -> (YES/NO) Define de widget irá preencher todo espaço restante ou não

`var.pack(anchor = 'w')`

Define onde texto está posicionado com relação a um ponto de referência.

![anchor](https://www.tutorialspoint.com/python/images/tkanchor.jpg)


`Label().grid(row=,column=)`

Divide container em grades, podendo posicionar elementos em linhas e colunas.

Parâmetros obrigatórios:
- _row=_ -> Número da linha
- _column=_ -> Número da coluna

##### Janela de aviso

`messagebox.showinfo('Título','Corpo da mensagem')`

Exibe caixa de diálogo.
Outras opções de caixa de diálogo:

* showwarning()

* showerror()

* askquestion()

* askokcancel()

* askyesno ()

* askretrycancel ()

##### Botões, radioButtons e checkButton

`var = Button(self.janela, text='', command=)`

Cria botões.

Parâmetros obrigatórios:
- Janela
- Texto que será exibido no botão
- Comando que será executado ao apertar botão(Geralmente algum método ou função).


> Necessário empacotar (.pack()).

`var = Radiobutton(self.janela, text='', variable=, value=)`

Parâmetros obrigatórios:
- Janela
- Texto da opção
- Variável (objeto tipo _IntVar_)
- Valor da opção (número inteiro)

Parâmetros opcionais:
- __Command__ -> Quando informado, executa método informado, dispensando o uso de botões.
- Para outros, verificar documentação.

> Necessário empacotar (.pack()) cada opção.

`var.set(X)`

Define estado inicial do item X
0 -> Nenhum
1 -> Radio button 1 já ativo  
2 -> Radio button 2 já ativo
..
N -> Radio button N já ativo

`var = Checkbutton(self.janela, text='', variable=)`

Parâmetros obrigatórios:
- Janela
- Texto da opção
- Variável (objeto tipo _IntVar_)

> Necessário empacotar (.pack()) cada opção.

`var.set(1)`

Define estado inicial 
1 -> Marcado.
0 -> Não marcado.

`var.get()`

Efetua leitura de estado.
Funciona para Radio Button e Check Box


`radio_valor = IntVar()`

Armazena variável na variável _var_ com opção escolhida.
Funciona para Radio Button e Check Box

##### Entrada de dados

`self.var = Entry(self.janela)`

Caixa de entrada de dados do usuário.
> Necessário empacotar (.pack())

Parâmetros obrigatórios:
- Janela

Parâmetros opcionais:
- _name=_ -> nome do box
- _state=DISABLED/ENABLE_ -> Define se box pode ser editado.
- Para outros, verificar documentação.

`var.insert(INSERT, "texto")`

Define um texto já pré-escrito.

Parâmetros obrigatórios:
- INSERT
- _texto_ -> texto para exibição na caixa.


`self.entrada.get()`

Pega valor informado no método _Entry_.
__SEMPRE__ será uma __String__. Para números, converter string para tipo desejado.

```
self.var = StringVar()
self.var1 = Label(self.frame/janela, textvariable=self.var)
...
self.var1.set(nome)
```
Cria um "texto dinâmico". Exibe informações do usuário sem abrir uma nova janela.

* StringVar() -> "Pega" o que foi digitado no campo de entrada
* textvariable='' -> Recebe texto como variável
* self.var1.set(self.input.get()) -> Seta valor da INPUT como parâmetro para label de exibição.  

Recebe um parâmetro chamado textvariable, que vai receber um texto variável, passando como argumento o nome do label 
dinâmico.

###### Parâmetros 

> Disponível para Frames, Labels, Botões e opções de entrada(Entry)

var = tkinter.Label(_varJanela_, _texto=_, _cor de fundo=_, _cor da fonte=_)
var = tkinter.Frame(_varJanela_, _texto=_, _cor de fundo=_, _cor da fonte=_)

_janela_ -> Variável da janela que irá aparecer o label

_texto_ -> Texto que irá ser mostrado

_cor de fundo_* -> Cor de fundo da janela

_corda fonte_* -> Cor do texto

_height_ -> Define altura em pixels 

_width_ -> Define largura em pixels 


* Pode ser usado junto com atributo _fill_ = tkinter.Z_ do método __.pack()__


##### Eventos

Eventos são algum tipo de interação com usuário, seja digitando algo, apertar de um botão, selecionar algo, etc.
GUI é feita tratamento de eventos de modo onde rodam e aguardam retorno.


`evento.bind(evento , tratador_do_evento)`

Criação de um tratador de eventos.

event.y -> identifica posição 'Y' do mouse 
event.x -> identifica posição 'X' do mouse
event.char -> identifica tecla pressionada

###### Tipos de eventos

__MOUSE__
- _<Button-1>_ -> mouse1
- _<Button-2>_ -> mouse3
- _<Button-3>_ -> mouse2
- _<Return>_   -> Enter
- _<Enter>_    -> Passa o mouse por cima do botão
- _<Leave>_    -> Tira o mouse de cima do botão
    -  event.widget.config(relief=) -> altera configuração do efeito
        - FLAT -> Apenas o texto, sem bordas
        - RAISED -> Botão volta estado normal.
        - SUNKEN -> Como se tivesse sido pressionado, mas com profundidade
        - GROOVE -> Borda em linha sem efeitos
        - RIDGE -> Borda em linha com "Alto relevo"
- _<ButtonRelease-1>_ -> Botão liberado('solto')
- _<B1-Motion>_ -> Click e arraste do mouse

__TECLADO__
- _<KeyPress>_ ou _<Key>_ - Tecla é pressionada
- _<key>_ - Mesmo de <KeyPress-tecla>
- _<KeyRelease>_ - Tecla é solta ou liberada
- _<KeyPress-tecla>_ ou _<Key-tecla>_ - Tecla específica, a tecla, é pressionada
- _<KeyRelease-tecla>_ - Tecla específica é solta ou liberada
- _<prefixo-tecla>_ - Tecla específica tecla enquanto segura a prefixo. Esse prefixo pode ser Alt, Shift ou Control apenas.
    - prefixo -> KeyPress/key/KeyRelease


##### Listbox

Mostra uma lista de itens.
Lista é mostrada somente em _string_.

`var=Listbox(master, param)`

Parâmetros obrigatórios:
- Janela

Parâmetros opcionais:
- Parâmetros(alguns)
    - _xscrollcommand_ -> Barra de rolagem da lista na horizontal 
    - _yscrollcommand_ -> Barra de rolagem da lista na vertical
- Para outros, verificar documentação.
    
    
`lista.delete(inicio, fim)`

Apaga linha da lista.

Parâmetros obrigatórios:
- Linha inicial (0)

Parâmetros opcionais:
- Linha final. Quando não informada, __NONE__ é definida
- Para outros, verificar documentação.

`lista.insert(index, elemento)`

Insere linha na lista.

Parâmetros obrigatórios:
- Index (Posição na lista). 
    - Podendo ser _END_ para inserir no final da lista.

Parâmetros opcionais:
- Linha final. Quando não informada, __NONE__ é definida.
- Para outros, verificar documentação.
***
#### Scrollbar (barra de rolagem)

Cria uma barra de rolagem visível.

`var=Scrollbar(janela, opcional)`

Parâmetros obrigatórios:
- Janela

Parâmetros opcionais:
- verificar documentação.

###### Métodos

- _get()_ -> Retorna (a,b) com posição atual do "slider". 
            __a__ = Posição da esquerda ou superior da borda para as barras de rolagem horizontal e vertical (respectivamente).
            __b__ = Posição da borda direita ou inferior
- _set()_ -> Conecta barra de rolagem a outro widget. Utilizar juntamente com xscrollcommand= ou yscrollcommand= no widget escolhido.


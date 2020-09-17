## Listas

Listas = vetor
Listas -> informações ordenadas

##### Criar uma lista

Basta utilizar colchetes __[ ]__ após variável

`nomeLista = []`


Cada valor dentro de uma lista é um ___item___
Cada item é separado por ___vírgula ,___

##### Acessar dados lista

A lista armazena seus itens em "endereços", para acessa-los utiliza-se o endereço correspondente.

```python
nomeLista = [0]
nomeLista = [1]
```

> Nota: O primeiro item sempre é representado pelo endereço 0.

##### Adicionar dados

Há dois métodos de se criar uma lista, com seus valores já preenchidos ou o mais comum, solicitando para item ser
adicionado na lista conforme for necessitando, usando comando ___append()___

`nomeLista.append(item)`

Parâmetro obrigatório:
- Item

##### Tamanho lista

Para saber tamanho da lista, ou quantos itens estão inseridos nela, utilizar comando ___len()___

`len(lista)`

Parâmetro obrigatório:
- Nome da lista

##### Alterando item

Alterar um item da lista é similar ao acessar os dados da mesma, necessitando apenas informar o endereço correspondente 
e atribuir novo valor ao endereço.

`nomeLista[endereco] = novoValor`

Parâmetro obrigatório:
- Endereço

##### Apagar item

`del nomeLista[endereco]`

Parâmetro obrigatório:
- Endereço

***
##### Operações com listas

>Unir duas ou mais listas em uma única
>
>`listaFinal = lista1 + lista2`

>Repetir lista 
>
>`lista = lista * 2`

>Inserir item em endereço específico
>
>`lista.insert(endereco, item)`

>Eliminar primeira ocorrencia do item
>
>`lista.remove(item)`

>Inverter lista
>`reverse()`

>Ordena em ordem alfabética ou numérica
>`lista.sort()`

>Apagar lista
>`lista.clear()`

>Copiar lista
>```python
>lista.copy()
>ou
>lista2 = [] + lista1
>```

>Contar ocorrencia de um item
>
>`lista.count(item)`

>Retirar elemento específico
>
>`lista.pop(x)`
>
>'X' podendo ser NULO -> remove último item da lista<br>
>'X' podendo ser endereço

##### Sublistas

Quebrar ou fatiar lista __:__

`novaLista = lista[inicio:fim]`

Onde início e fim correspondem ao índice(endereço) da lista.
Deixando início ou fim sem valores, representa pegar todos os valores até ou a partir do endereço informado.

```python
novaLista = lista[:2] # armazena do início ao endereço 2
novaLista = lista[1:] # armazena do endereço 1 até o final da lista
```

##### Verificando itens na lista

para saber se há um item na lista, ___in___ ou ___not in___
***

## Matriz

Uso de matrizes consiste no uso de lista dentro de lista. Em listas, temos 1 linha e X colunas, (Lista = lista[X]). 

`matriz = [a,b,c],[d,e,f] # matriz 2 linhas e 3 colunas `

Para acessar informações, deve-se informar a coluna e a linha para acesso.

`matriz = [0][1] # Acessa segundo elemento da primeira linha`

##### Inicializar matriz

Tanto para inicializar quanto para mostrar uma matriz, utiliza-se _for_ dentro de _for_.

* Inicializar

    Inicializa uma matriz 4x4
    
`matriz = [ [0 for i in range(4)] for j in range(4)]`

* Exibir

    Exibe toda a matriz  
```python
for linha in range(4):
    for coluna in range(4):
        pass    
```
***
## Tuplas

Listas que não podem ser alteradas. Ideal para armazenamento de senhas, onde não podem sofrer alterações.
Diferente das listas, as tuplas são usadas em itens com diferentes tipos, tipo string, int e float em uma única tupla, 
listas geralmente mais usada com um único tipo.


##### Declaração

Seguem os mesmos princípios das listas, sendo declaradas por __( )__.

`tupla = ('nome', 1992, 27  )`

Para armazenar uma tupla com somente um único item, informar vírgula no final e deixar vazio próximo campo.

`tupla = (senha,)`

> Transformar lista em tupla
>
> `list(nomeTupla)`
>
> Transformar lista em tupla
>
> `tuple(nomeLista)`
***
***

> Desafio: Faça um script em Python que permite que dois jogadores joguem o jogo da velha
>

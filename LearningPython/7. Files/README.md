## Arquivos

São objetos assim como dicionários ou listas, porém do tipo _FILE_.

#### Abrir arquivos

`arquivo.open('nome_arquivo', tipo)`

Retorna como _string_ o endereço do arquivo que deseja abrir.
Caso tipo não seja informado, arquivo é aberto em modo leitura.

Parâmetro obrigatório:
- _nome_arquivo_
***
#### Ler arquivos

`arquivo.read()`

Retorna conteúdo do arquivo em única string (copia todo o conteúdo, inclusive quebras de linha).

#### Leitura linha a linha

`arquivo.readlines()`

Retorna uma ___lista de strings___, cada linha em uma posição da lista, até final do arquivo.

`arquivo.readline()`

Mesmo caso que o anterior, retorna uma ___lista de strings___ até a primeira quebra de página (\n).
Nesse caso retorna apenas uma única linha por vez, conforme método for chamado.

#### Tamanho 

`len('nome_arquivo')`

Pelo fato do arquivo ser um objeto, podemos usar suas propriedades. Uma delas é o método _len()_, usado para saber 
de determinado objeto.

Parâmetro obrigatório:
- _nome_arquivo_

`arquivo.truncate(tam)`

Trunca tamanho do arquivo de acordo com posição atual. Se _tam_ for informado, é mostrado as informações até tamanho de 
_tam_, e o restante excluído do arquivo, caso não seja informado tamanho, tudo o que houver após posição de leitura atual
 será excluido.
Exemplo: feita a leitura da primeira linha e o "cursor"encontra-se agora na segunda linha. Solicitado o 'truncamento', 
todo o conteúdo da segunda linha em diante é apagado.

>NOTA: Quando aberto um arquivo na condição de escrita ('w') a função de truncar já é realizada implicitamente.

Parâmetro opcional:
- _nome_arquivo_
***
#### Escrever no arquivo

`arquivo.open('nome_arquivo', tipo)`

Para escrita, deve-se informar que arquivo aberto será de escrita, informando 'w' (com aspas) no tipo.

`arquivo.write('info')`

Após abertura do arquivo usa o comando _.write()_ para fazer a adição da informação no arquivo.

`arquivo.close()`

Após abrir um arquivo para escrita, deve-se fechar o arquivo. 

> NOTA:
> 1. SEMPRE que arquivo for aberto para escrita deve-se fechar o mesmo após término da escrita.
> 2. O que for escrito irá sobrescrever o arquivo, apagando as antigas informações.

Aproveitando outra propriedade dos objetos, para adicionarmos uma outra informação sem apagar informações anteriores, 
usamos o _append_. No momento da abertura do arquivo informar o _tipo_ com 'a' (com aspas).

> NOTA:
> Ao inserir uma nova informação, ela será atribuida na mesma linha que a informação anterior. Para inserir uma nova 
> linha, informar também a quebra de página ('\n').

##### Modos para abertura de arquivo

* "a"  - Escreve ao final do arquivo; se este não existir, é criado
* "r"  - Abre o arquivo para a leitura, se não existir, lançar um eerro de IOError
* "r+" - Abra um arquivo para leitura e escrita. Se não existe, lança um erro IOError
* "w"  - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e escreve por cima. Se não existir o arquivo, ele cria
* "w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e escreve por cima. Se não existir o arquivo, ele cria
* "ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com entrada e saída no modo binário, para plataformas Windows e Macintosh


##### Retirar quebra de linha [\n]

`rstrip('\n')`

Cada linha lida apresenta também o caractere de quebra de linha ('\n' ou 'enter'), para retirá-la, usa-se o método _rstrip()_
Ele retira da _string_ algum caractere informado, neste caso '\n'.
Outra ideia é utilizar para retirar definitivamente a quebra de toda a lista importada do arquivo:

```python
for index in range(len(arquivo)):
    arquivo[index] = arquivo[index].rstrip('\n')
``` 

##### Identificando fim do arquivo

Quando feita a litura linha a linha (.readline()) quando atingido o final do arquivo é apresentado um erro _list index out of range_,
informando que foi tentado acessar um dado da lista que não existe. Para "contornar" erro, basta checar se linha lida está 
vazia ('')  

```python
if linha != '':
    print(linha.rstrip('\n'))
else:
    print("Fim do arquivo")
``` 

#### Caminhos e diretórios

path -> endereço completo do arquivo a ser aberto.

> NOTA: Em caminho diretórios, usa-se '\\'.  

`os.path.join('pasta1', 'pasta2','pasta3')`

Python é usado em sistemas operacionais diferentes, para não haver problemas com caminhos (Windows usa-se \\ e Linux //),
utiliza a função ___os.path.join()___. De acordo com sistema operacional que está sendo utilizado, ele irá automaticamente
preencher da forma que o sistema interpreta.  

Podem ser utilizadas variáveis para o caminho, muito utilizado quando usuário informa caminho aonde deverá ser instalado 
o arquivo. 

```python
path = 'C:\\Users'
os.path.join(path,'Administrador')
```

A saída do código acima será: C:\Users\Administrador


#### Módulo __OS__

Módulo __OS__ --> módulo de sistema operacional. 

> getcwd(path)
```python
import os
print(os.getcwd())
```

Retorna endereço do diretório atual (endereço onde está rodando o script).

> chdir()

```python
import os
os.chdir('endereço')
```

Muda de pasta/diretório para o _endereço_ informado.

> makedirs()

```python
import os
os.makedirs('endereço')
```

Cria uma nova pasta. Caso informe mais de um diretório que não exista, ele irá criar ambos.

`os.path.basename(path)`

Retorna nome do arquivo

`os.path.dirname(path)`

Retorna nome do diretório 'Raiz' do arquivo.

`os.path.split(path)`

Mostra em formato de tupla diretório e nome arquivo.

`getsize(path)`

Informa tamanho em bytes do arquivo

`os.listdir(path)`

Mostra conteúdo de uma pasta
***
***

> #### Exercícios
>
>1. Crie um programa simples que pergunta se a pessoa deseja ler um arquivo ou escrever algo nele.
>
>2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
>Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e 
>identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o 
>seguinte arquivo, chamado "usuarios.txt":
>
>   alexandre       456123789
>   anderson        1245698456
>   antonio         123456456
>   carlos          91257581
>   cesar           987458
>   rosemary        789456125
>
>   Neste arquivo, o nome do usuário possui 16 caracteres. A partir deste arquivo, você deve criar um programa que gere um 
>relatório, chamado "relatório.txt", no seguinte formato:
>
>   ACME Inc.               Uso do espaço em disco pelos usuários
>
>   ***
>
>   Nr.  Usuário        Espaço utilizado     % do uso
>
>   1    alexandre       434,99 MB             16,85%
>
>   2    anderson       1187,99 MB             46,02%
>
>   3    antonio         117,73 MB              4,56%
>
>   4    carlos           87,03 MB              3,37%
>
>   5    cesar             0,94 MB              0,04%
>
>   6    rosemary        752,88 MB             29,16%
>
>   Espaço total ocupado: 2581,57 MB
>
>   Espaço médio ocupado: 430,26 MB
>
>   O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de 
>forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser 
>feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também 
>deverá ser feito através de uma função, que será chamada pelo programa principal.
>
>3. Foi feito um game onde o computador sorteia um número de 1 até 100 e você deve adivinhar.Implemente a função recorde nele.
>Ou seja, num arquivo de no recorde.txt você deve armazenar o recorde do número mínimo de tentativas que alguém conseguiu 
>acertar.
## Funções

Função -> pedaço de código específico.

Vantagens: 
 - Reuso do código;
 - Simplificação do código;
 - Desenvolvimento em blocos;
 - Facilidade em encontrar erros;
 - Facilidade de realizar testes;
***
 
 ##### Declarar função
 
 Para se criar uma função, basta utilizar a palavra-chave: ___def___ seguida do nome da função.
 
 
 ```python
def funcao(argumentos):
   codigo
   codigo
```

##### Chamar função

Para chamar uma função, é necessária somente chamá-la pelo nome seguida de parênteses.
>Nota: Prestar atenção ao criar códigos grandes. Pode-se estar criando funções porém nunca chama-las, causando apenas 
>uso desnecessário de memória.Funções simplificam o código, porém deve-se ter organização no desenvolvimento. 

```python
funcao()
```

Uma função não necessariamente deve apenas chamar uma única função. Assim como os _laços_ e os _testes condicionais_, 
pode-se ter um aninhamento de funções.

```python
def bomdia():
    print('Bom dia.')


def mensagem():
    print('Olá.  ')
    bomdia()

mensagem()
```
##### Variável local

São variáveis que são utilizadas apenas nos blocos de códigos onde são informadas, podendo ser usadas em outros trechos 
com outros valores que não são alteradas.

```python
def func1():
    a = 'Olá'


def func2():
    a = 5000
```

##### Variável global

Variáveis que podem ser usadas em todo o programa e são visíveis em todos os blocos do código. Um valor que será 
utilizado em diversas partes do programa pode ser definida como variável global.

Para usar uma _variável global_ é necessário que a mesma seja definida fora do escopo das funções e que seja utilizado o 
temo ___global___ antes da variável em uma função.

>Nota: Deve-se atentar ao utilizar uma variável global pois por poder ser vista em todo o programa, também pode ser 
>alterada em qualquer parte.

```python
desc = 10

def desconto(valor):
    global desc
    print("Preço original   : R$ ",valor)
    print("Desconto         : ", desc,"%")
    desc /= 100
    print("Valor do desconto   : ", valor*desc)
    print("Preço c/ desconto: ", valor*(1-desc) )

val = float(input("Preço do produto: "))
desconto(val)
```
***

#### Argumentos e parâmetros (Passagem por valor)

Na grande maioria dos códigos precisamos passar informações para as funções, a fim de não precisar solicitar novamente
ao usuário o valor ou para não haver necessidade de realizar todo o calculo feito por outro bloco. Desse modo a função 
cria uma _cópia_ do valor da variável que foi recebida e a utiliza em seu bloco. Assim por mais que tenham 2 ou mais 
variáveis com mesmo nome, ambas são diferentes. 

Não necessariamente precisam ter mesmo nome. Podendo ser passado infinitos argumentos, porém a quantidade de argumentos 
devem ser a mesma de parametro.

> Argumento

Informações que são enviados para a função.

`nome_da_funcao(argumento1, argumento2, argumento3,...)`

> Parâmetro

Informações que são recebidas na função.

`def nome_da_funcao(parametro1, parametro2, parametro3,...)`

```python
def func1(x, y):
    print(x,y)

x = 10
y = 100
func1(x,y)
```
##### Argumento Posicional e Argumento Nomeado

> Argumento Posicional

A ordem de que foi passada no parâmetro ao chamar a função é o mesmo recebido nos argumentos.

`funcao(1, a, Z)`

`def funcao(par1, par2, par3)`

No caso os valores recebidos são:

par1 = 1

par2 = a

par3 = Z

> Argumento Nomeado

É definida no momento da passagem dos argumentos quais serão os valores dos parâmetros, não importando a ordem.

`funcao(nome, idade, sexo)`

`def funcao(sexo = m, nome = marcelo, idade = 27)`

nome = marcelo

idade = 27

sexo = m

O resultado é o mesmo, porém foram nomeados qual parâmetro recebe qual argumento

>Nota: Argumentos posicionais devem sempre aparecer antes dos nominais.  
>
>`funcao(nome, idade, sexo)`
>
>`def funcao(marcelo, sexo = m , idade = 27)`

##### _RETURN_ em funções

Utilizada quando deseja receber algum retorno de informação da função que foi chamada.
Podendo retornar mais de um valor.

```python
def funcao(parametro):
    código
    código
    return algo, parametro

algo, parametro = funcao(argumento)
```  
***
## Módulos

Módulo -> Arquivo de códigos Python

![Tipos de módulos Python](https://3.bp.blogspot.com/-NoYw_bGbOmM/Wz1dPnRj53I/AAAAAAAAB3s/lfLk1Sgt514sBAR2zg72LVnZI6NV1h8lgCLcBGAs/s640/modulos-python-principais.png)

O módulo ajuda a dividir o bloco em blocos menores, parecido com as funções, porém em arquivos separados.
Diferente das funções, os módulos são usados quando o trecho do código não é chamado diversas vezes durante a execução, 
como por exemplo um menu de algum código, necessário apenas no início do código.

##### Importando módulos

Para importar um módulo, necessário apenas utilizar o comando ___import___ antes do nome do módulo

>Nota: Qualquer importação de módulos deve ser a primeira atividade do programa.

Para usar alguma função dentro do módulo, utiliza-se o nome do módulo '.' função que deseja

```python
nomemodulo.funçãoModulo()
```

O comando _import_ acaba por importar todo o módulo, para importar somente uma única função, ou mais de uma, de um módulo 
que pode contém inúmeras linhas, usa-se a sintaxe:

```python
from nomemodulo import funçãoModulo
```

Com isso deixa o programa mais leve pois não é carregao diversas linhas que não serão utilizadas.

##### Números aleatórios

Para geração de números aleatórios, é utilizada o módulo/biblioteca _random_

```python
import random
``` 

###### Gerar número

> ```python
> random.randint(inicio, fim)
> ```

Gerar números aleatórios inteiros com definição de início e fim.

Parâmetros obrigatórios:
- _inicio_ -> Número inicial
- _fim_ -> Número final

> ```python
> random.randrange(A)
> ```

Gera número aleatório de 0 até 'A-1'.



> ```python
> random.randrange(A, B)
> ```

Gera número aleatório de A até B-1.

> ```python
> random.randrange(A, B, C)
> ```

Gera número aleatório de 'A' até 'B-1', pulando de 'C' em 'C'.

Parâmetros obrigatórios(randrange):
- _A_ -> Número inicial

Parâmetros opcionais(randrange):
- _B_ -> Número final
- _C_ -> Número de "pulo"

> ```python
> random.random(A, B, C)
> ```

Número aleatório decimal de 0.0 até 1.0

> ```python
> random.uniform(início, fim)
> ```

Números float aleatórios que compreendem entre início e fim.

> ```python
> random.sample(sequencia, comprimento)
>```

Números aleatórios sem repetição, definida pela sequencia(lista de números) e comprimento, quantidade de números

***

##### Módulo math

```python
import math
```

Algumas funções que podem ser utilizadas do módulo de cálculos matemáticos de python

> cos(x) - dá o valor cosseno de x radianos
>
> sin(x) - valor do seno de x radianos
>
> tan(x) - valor da tangente de x radianos
>
> acos(x) - retorna o arco cosseno de x, em radianos
>
> asin(x) - retorna o arco seno de x, em radianos
>
> atan(x) - retorna o arco tangente de x, em radianos
>
> degrees(x) - transforma radianos em graus 
>
> radians(x) - transforma graus em radianos
>
> sqrt(x) - raíz quadrada
>
> math.pi - constante PI
>
> math.e - número de Euler ou Néper
>
> math.exp(x) - cálculo exponenciação e^x
>
> math.log(x) - logaritmo natural de 'x'
>
> math.log10(x) - log base 10 de 'x'
>
> floor(x) - arredondamento para baixo
>
> ceil(x) - arredondamento para cima
>
***
***

>#### Exercícios
>
>1. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou
>vice-versa. Para cada opção, crie uma função.
>
>2. programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através de 
>outra função
>
>3. Faça um script em Python que simule 1 milhão de lançamentos de dados e mostre a frequência que deu para cada número.
>
>4. Faça uma script em Python que solicite um inteiro positivo ao usuário, n. Então uma função exibe todos os termos da 
>sequência de Fibonacci até o n-ésimo termo.
>
>5. Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou 
>seja, podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um 
>inteiro e dizer se é perfeito ou não. Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.
>
>6. Faça um programa para imprimir:
>
>    1
>
>    2   2
>
>    3   3   3
>
>    .....
>
>    n   n   n   n   n   n  ... n
>
>   para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
>
>7. Faça um programa para imprimir:
>
>    1
>
>    1   2
>
>    1   2   3
>
>    .....
>
>    1   2   3   ...  n
>
>   para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
>
>Desafio: 
>Crie um programa onde o computador vai sortear um número de 1 até 100.
>Em seguida, você vai tentar adivinhar que número foi esse.
>A cada tentativa, ele vai te dizer se seu palpite foi alto, baixo ou se você acertou.
>Quando acertar, deve mostrar quantas tentativas você fez até acertar.

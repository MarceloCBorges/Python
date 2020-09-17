## Introdução

### Mostar informações no visor
print('text') ou print("text")
Comando print podendo ser utilizado aspas simples ou duplas.

### Variáveis

`<p>_variavel_ = dado`

Não necessário informar tipo da variável, de acordo com dado pyhton entende qual é tipo de variável e a atribui atuomaticamente

##### Ler dados teclado:

`_variavel_ = input(string)`

Comando *input()* irá "pausar" o programa esperando usuário digital algo. Enquanto não apertar *Enter*, nada  irá acontecer
Pode-se utilizar o comando *input()* com algo a ser informado na tela para auxílio ao usuário, eliminando um comando 
*print()*.

`_variavel_ = input("Informe seu nome:" string)`

Dentro da função *input()* independente se for digitado um número ou qualquer tipo de formato, será armazenado na 
variável uma string.

Caso deseje informar um número, deve-se utilizar o comando *int()* ou o tipo da variável que deseja antes do comando *input()*.

`_var_ = int(input("Digite número: "))`
***
##### Operações Matemáticas

    - Soma: +
    - Subtração: -
    - Multiplicação: * 
    - Divisão: / 
    - Exponenciação: ** 
    - Resto da divisão: % 
***
##### Precedência de operadores

Na ordem de importância, maior pra menor:

    - Exponenciação: **
    - Multiplicação, divisão e resto da divisão: *  / %
    - Adição e subtração: + -
    - Tudo o que estiver entre () será realizado primeiro, seguindo a ordem dos operadores.
<hr>
##### Formatação números quebrados

Em casos de divisões, podemos ter como respostas dízimas periódicas ou números quebrados muito grandes.
3.33333333333333... ou 3.14159265359...

Para ajustar, necessário informar como deve ser a saída no momento da impressão do valor com o operador **{:.2}**:
  
  No caso, o retorno do cálculo mostrará apenas 2 casas decimais.
  Nota-se que mudou o tipo de saída de dados. No caso foi utilizada um método para formatação de strings(*str.format*), 
  podendo ser representada de duas formas:
  
  >print(**f**'Cada um vai ficar com **R${valor:.2f}**')
>
  >print('Cada um vai ficar com R$<b>{:.2f}'.format(valor)</b>) 
>
***

#### Operadores de Atribuição: += , -= , *= , /= e %=

Existe algumas simplificações na hora de executar alguns cálculos, principalmente quando falamos em ___contadores___.


Original  |Simplificação
:--------:|:------:
x = x - y | x -= y
x = x + y | x += y
x = x / y | x /= y
x = x * y | x *= y
x = x % y | x %= y

***
***

>#### Exercícios
>
>1. Conversor Farenheit Celsius.
>
>2. Conversor Celsius Farenheit.
>
>   `F = (9/5)C+32`
>
>3. Programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível ele 
>pode comprar e quantos quilometros o carro consegue andar com este tanto de combustível.


## Laços e Loopings - FOR & WHILE

Uso de loops para execução de grandes tarefas repetidas, por exemplo solicitar ao usuário notas de seus alunos. 
Tarefa simples, porém imagine se é necessária inserir 50, 100 ou talvez mais notas. Looping nos ajuda a escrever o código
e a simplifica-lo também.

##### WHILE

```python
while condição:
   codigo1
   codigo2
   ... 
```

__Enquanto__ condição for verdadeira, executa linha de código.
Caso termine as linhas de códigos, verificará se condição permanece verdadeira, caso positivo, executará linhas de código 
novamente. Caso negativo, sairá do loop.

***

#### FOR

```python
for variavel in [val1, val2, val3, etc]:
    codigo
    codigo
``` 
 
 A __variável__ irá assumir o valor presente em _val1_, executará as linhas de código, depois assumirá o valor presente 
 em _val2_ e assim por diante. 
 
 O laço for é mais "controlado" se comparado ao laço _while_, pois consegue ser informado quantas vezes será executado.
 Não sendo necessário ser utilizado somente valores para atribuição.
 
>##### Função range() 

A fim de não determinarmos todos os valores a serem executados pelo laço __FOR__, como informar todos os valores de 1 
até 1000, utilizamos a função _range()_:

``` python
for variavel in range(n):
    codigo
    codigo
``` 

Ele vai fornecer uma lista com os elementos: 0, 1, 2, ..., (n-1). Sempre será fornecida uma lista de 'n' elementos, 
começando do 0.

>##### Função range(_início_, _fim_) 

Pode-se ser informada junto da função, o valor de início e fim, porém deve-se atentar que por mais que seja informado os 
valores de início e fim, sua contagem ainda segue a regra de ser efetuada até _n-1_. 
```python
for variavel in range(_início_, _fim+1_):
    codigo
    codigo
``` 

>##### Função range(_início_, _fim_, _pulo_)

Sempre que executada, a função _range()_ é executada na contagem de 1+1, porém ela também pode ser orientada a executar 
a quantidade que se desejar, basta apenas informá-la no argumento.
```python
for variavel in range(_início_, _fim+1_, _pulo_):
    codigo
    codigo
```

>##### Passando argumento para função

Não é sempre que temos os argumentos ara as funções, as vezes necessitamos de informações que somente o usuário tem.
Para resolver isso, basta perguntar ao usuário quais são os parametros e informa-los na função.

```python
valor_inicial = int(input())
valor_final = int(input())

for variavel in range(valor_inicial, valor_final):
    codigo
    codigo
```
#### Instruções ELSE, BREAK, PASS e CONTINUE

Embora dificilmente vista e não muito praticada, as instruções BREAK, CONTINUE, PASS e ELSE também podem ser vistas em 
laços. 

>##### Instrução ELSE

```python
while TESTE:
    codigo
    codigo
    ...
else:
    codigo
    ...
```
Função _ELSE_ é utilizada quando queremos executar alguma ação assim que o laço é encerrado (torna-se _falso_).

>##### Instrução BREAK
```python
while TESTE:
    codigo
    if TESTE2:
       break;
    ...
```
A instrução _BREAK_ tem a função de literalmente "parar", "quebrar", "interromper" o laço. 

>##### Instrução CONTINUE
```python
while TESTE:
    codigo
    continue
    if TESTE2: 
        codigo
    ...
```
Instrução _CONTINUE_ atua de forma semelhante ao _BREAK_, porém ao invés de encerrar o laço, ele cria um "atalho" para o 
início, todo o código que estiver após _continue_ não será executado, porém irá ao início do laço e continuará sua 
execução.

>##### Instrução PASS
```python
while TESTE:
    pass #condição de teste para tal coisa
```
Instrução _PASS_ é uma instrução que literalmente não faz nada. Usada quando queremos validar  ou "reservar" uma 
condição, função ou trecho de código que será usada mais a frente no decorrer do desenvolvimento do programa. Com isso, 
consegue deixar tal etapa do código semi pronta, enquanto ainda desenvolve em nível abstrato, sem pensar em como as 
funções devam executar.
***
***

>#### Exercícios Laços
>1. Peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário 
>informe um valor válido.
>
>2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando 
>uma mensagem de erro e voltando a pedir as informações.
>
>3. Supondo que a população de um país A seja da ordem de X habitantes com uma taxa anual de crescimento de X1% e que 
>a população de B seja Y habitantes com uma taxa de crescimento de Y1%. Faça um programa que calcule e escreva o 
>número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
>de crescimento.
>Os valores de X e Y devem ser informados pelo usuário.
>
>4. Programa que leia 5 números e informe o maior número, soma e a média dos números.
>
>5. Programa que imprima na tela apenas os números ímpares entre 1 e 50.
>
>6. Programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
>
>7. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve 
>informar de qual numero ele deseja ver a tabuada.
>
>8. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de 
>números ímpares.
>
>9. Faça um programa capaz de gerar a série Fibonacci até o n−ésimo termo.
>
>10. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da 
>turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média 
>calculada.
>
>11. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de 
>valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da 
>compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para 
>então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar 
>a próxima compra. A saída deve ser conforme o exemplo abaixo:
>
>    * Produto 1: R$ 2.20
>    * Produto 2: R$ 5.80
>    * Produto 3: R$ 0
>    * Total: R$ 9.00
>    * Dinheiro: R$ 20.00
>    * Troco: R$ 11.00
>
>12. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a 
>tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também 
>pelo usuário,
>
>13. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo 
>representando a sua nota.Mostre o número e a nota do aluno, com maior e menor nota.
>
>14. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos 
>seguintes intervalos: 
>    * [0-25] 
>    * [26-50] 
>    * [51-75]
>    * [76-100] 
>
>    A entrada de dados deverá terminar quando for lido um número negativo.
>
>15. O cardápio de uma lanchonete é o seguinte:
>    * Especificação   Código  Preço
>    * Cachorro Quente 100     R$ 1,20
>    * Bauru Simples   101     R$ 1,30
>    * Bauru com ovo   102     R$ 1,50
>    * Hambúrguer      103     R$ 1,20
>    * Cheeseburguer   104     R$ 1,30
>    * Refrigerante    105     R$ 1,00
>
>    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago 
>por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
>
>16. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
>Os códigos utilizados são:
>    * 1 , 2, 3, 4  - Votos para os respectivos candidatos 
>    * 5 - Voto Nulo
>    * 6 - Voto em Branco
>
>    Faça um programa que calcule e mostre:
>    * O total de votos para cada candidato;
>    * O total de votos nulos;
>    * O total de votos em branco;
>    * A percentagem de votos nulos sobre o total de votos;
>    * A percentagem de votos em branco sobre o total de votos. 
>
>       Para finalizar o conjunto de votos tem-se o valor zero.
>
>17. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua 
>nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos 
>sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
>(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. 
>Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
> * Atleta: Aparecido Parente
> * Nota: 9.9
> * Nota: 7.5
> * Nota: 9.5
> * Nota: 8.5
> * Nota: 9.0
> * Nota: 8.5
> * Nota: 9.7
> * Resultado final:
> * Atleta: Aparecido Parente
> * Melhor nota: 9.9
> * Pior nota: 7.5
> * Média: 9,04
>
>Desafio:
>Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

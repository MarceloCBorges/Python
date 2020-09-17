## Testes Condicionais

**Operadores de comparação:**

- Igualdade: == 
- Diferente: != 
- Maior que: >
- Menor que: <
- Maior igual a: >=
- Menor igual a: <= 
<hr>

#### IF

```python
if condition :
    [código]
    [código]
    ...
else:
    [código]
    [código]
    ...
```

Tudo o que estiver abaixo da condição if, desde que esteja indentado (espaçado na linha abaixo do if) 
irá funcionar. Quando "quebrar" essa formatação, o Python identificará que condição IF não possui mais códigos e 
prosseguirá com execução do programa.

Será executado comando **IF**
```python
if age>17:
    print('Você é de maior, já pode dirigir!')
```
Não será executado comando **IF**
```python
if age>17:
print('Você é de maior, já pode dirigir!')
```
<hr>

#### ELIF

Para simplificar o uso de IF ELSES em sequência, pode ser utilizada a condição `elife [codigo]:`
Com isso conseguimos escrever mais rápido o código e fica visualmente melhor e compreensível, além de ficar com código 
menor.

Sem ELIF:
```python
if resposta == 1:
    print('A')
else:
    if resposta == 2:
          print('B')
    else:
        if resposta == 3:
            print('C')
        else:
            if resposta == 4:
                print('D')
            else:
                if resposta == 5:
                    print('E')
```
Com ELIF:
```python
if resposta == 1:
    print('A')
elif resposta == 2:
    print('B')
elif resposta == 3:
    print('C')
elif resposta == 4:
    print('D')
elif resposta == 5:
    print('E')
```
#### Operadores Lógicos

* AND
* OR
* NOT

Necessários para realização de mais de uma validação nos testes condicionais.

>AND

`if code1 and code2:`

Idéia de soma, somente quando ambas as condições (1 e 2) forem verdadeiras que a validação se tornará verdadeira.

>OR

`if code1 or code2:`

Validação se torna verdadeira quando alguma condição (1 ou 2) forem verdadeiras, independente de qual seja.

>NOT 

`if not code == 10`

 Inverte o sentido da validação. Usada para quando apenas uma única resposta é válida. No caso acima, caso resposta não 
 seja 10, pulará a condição **IF**.
 
1.Tabela Verdade: Operador AND

Condição A|Condição B|AND (A.B)
:--------:|:--------:|:-------:|
True      |True      |True
True      |False     |False
False     |True      |False
False     |False     |False
 
2.Tabela Verdade: Operador OR

Condição A|Condição B|AND (A.B)
:--------:|:--------:|:-------:|
True      |True      |True
True      |False     |True
False     |True      |True
False     |False     |False 

3.Tabela Verdade: Operador NOT

Condição A|NOT ( ~A)
:--------:|:--------:|
True      |False
False     |True

<hr>
<hr>

>#### Exercícios Testes Condicionais
>
>1. Programa que verifique se uma letra digitada é vogal ou consoante
>
>2. Programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
>   - A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
>   - A mensagem "Reprovado", se a média for menor do que 7;
>   - A mensagem "Aprovado com Distinção", se a média for igual a 10.
>
>3. Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
>
>4. Programa que peça um número inteiro e determine se ele é par ou ímpar
>
>5. Programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela
>
>6. Programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
>   - salários até R$ 280,00 (incluindo) : aumento de 20%
>   - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
>   - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
>   - salários de R$ 1500,00 em diante : aumento de 5% 
>
>   Após o aumento ser realizado, informe na tela:
>   - o salário antes do reajuste;
>   - o percentual de aumento aplicado;
>   - o valor do aumento;
>   - o novo salário, após o aumento.
>
>7. Programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do 
>salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não 
>é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa 
>deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
>
>   Desconto do IR:
>    - Salário Bruto até 900 (inclusive) - isento
>    - Salário Bruto até 1500 (inclusive) - desconto de 5%
>    - Salário Bruto até 2500 (inclusive) - desconto de 10%
>    - Salário Bruto acima de 2500 - desconto de 20% 
>
>   Imprima na tela: 
>   - Salário Bruto
>   - IR(5%)
>   - (-)INSS(10%)
>   - (-)FGTS(11%)
>   - Total de descontos
>   - Salário Líquido
>
>8. Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
>Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
>
>   `Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;`
>
>   Triângulo Equilátero: três lados iguais;
>
>   Triângulo Isósceles: quaisquer dois lados iguais;
>
>   Triângulo Escaleno: três lados diferentes;
>   
>9. programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os 
>valores de a, b e c.
>
>   * Se 'A' igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores;
>   * Se delta negativo, a equação não possui raizes reais;
>   * Se delta igual a zero a equação possui apenas uma raiz real;
>   * Se delta positivo, a equação possui duas raiz reais;
>
>   PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)
>
>10. Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
>Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
>
>     * 326 = 3 centenas, 2 dezenas e 6 unidades;
>     * 12 = 1 dezena e 2 unidades 
>
>    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
>
>11. Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
>quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
> é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
>    * Exemplo 1: Para sacar 256 reais, duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
>    * Exemplo 2: Para sacar 399 reais,  três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
>
>12. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
>    * Álcool: até 20 litros, desconto de 3% por litro
>    acima de 20 litros, desconto de 5% por litro
>    * Gasolina:
>    até 20 litros, desconto de 4% por litro
>    acima de 20 litros, desconto de 6% por litro 
>
>    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível, calcule e imprima o valor a ser 
>pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
>    
>13. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
>
>    Produto    |Até 5 Kg         |Acima de 5 Kg 
>    -----------|:---------------:|:--------------:|
>    File Duplo |R$ 4,90 por Kg   |R$ 5,80 por Kg       
>    Alcatra    |R$ 5,90 por Kg   |R$ 6,80 por Kg       
>    Picanha    |R$ 6,90 por Kg   |R$ 7,80 por Kg       
>
>    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há 
>limites para a quantidade de carne por cliente. Se compra for feita no dinheiro, o cliente receberá ainda um
> desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo 
>usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
> pagamento, valor do desconto e valor a pagar.
>


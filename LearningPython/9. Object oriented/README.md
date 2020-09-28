## Orientação a objetos

Classe -> Molde/modelo - Agrupamento de objetos com a mesma estrutura de dados

Objeto -> Uma instância da classe

Atributo -> informações/característica/propriedades de uma classe

Métodos -> Funcionalidades, "modelo" para diversos valores

Com clases, pode-se criar infinitos objetos todos com mesmas características.

> Herança

Objetos herdam características da Classe que os criou.

> Encapsulamento

Agrupar métodos e atributos com "proteção" para que não possa ser acessado de qualquer parte do código, criando uma 
restrição no acesso.
***
#### Classe

```python
class MinhaClasse:
    [codigo da classe]
    [atributos]
    [metodos]
```

#### Objeto 

`varObjeto = nomeClasse()`

Declarar um nome para objeto e recebe o nome da classe.
Todo atributo e método presente na classe será atribuido ao objeto.

#### Método

> `__init__(self)`

Método construtor para criação do objeto.
Método a ser definido no começo de toda classe.

___SELF___ refere-se ao objeto chamado. Para identificação de qual método executar.


Os métodos em classes são iguais as funções, utilizando o comando na frente _def_, seguindo os mesmos princípios de 
passagem de parametros. 


##### Chamar Funções de uma classe
  
Para chamar uma função ou um método, utilizar nome do objeto + ponto(.) + método/função.

##### Segurança

Para tornar um atributo seguro, utilizar __underline duplo__ (__)
Com isso somente é possível ser acessado e modificado por métodos do próprio objeto.
Isso é utilizado para esconder senhas e outros dados frágeis.

`objeto.__atributo`

#### Composição e Herança

Composição -> Combinação de objetos, instanciamento de objetos de uma classe dentro de outra.
Herança -> Classe __herda__ atributos e métodos de outras classes. 

Pra fazer uma classe herdar outra, informar classe herdeira e 'mestre' na chamada da classe:

`class X(Y)`

Classe __X__ herda atributos da classe __Y__

Y = superclasse.
X = subclasse

> NOTA: Classe "master" deverá ser criada e instanciada primeiro.

***
***

>#### Exercícios
>1. Crie dois jogos simples: Cara e Coroa e lançamento de dados.
>2. Crie um sistema bancário com criação de contas e métodos de saque e depósito de dinheiro onde só deve ser possível 
>fazer um saque se a pessoa tiver um saldo positivo, e o saque máximo é esse valor.
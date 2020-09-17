## Dicionário

É uma lista de ítens desordenados, item são armazenados de forma desordenada.
Diferente das listas e tuplas que são ordenados por índices, dicionários são ordenados por ___chaves___.
Dicionário é parecido como um cofre, onde só se consegue ter acesso com uma chave.
   
> Nota: Não se consegue apagar uma chave.
>
##### Declarar e mostrar

* Listas -> [ ]
* Tuplas -> ( )
* Dicionários -> { }

`nomeDicionario = {chave: valor, chave2: valor2}`

Para mostrar, usa-se mesmo conceito das listas e tuplas, porém ao invés do índice, usa a chave.

`nomeDicionario[chave]`


Modos de exibição de um dicionário:
* dicionario.items(): exibe todos os itens, ou seja, os pares chave-valor
* dicionario.keys(): exibe todas as chaves do dicionário
* dicionario.values(): exibe todos os valores do dicionário

##### Validação de chaves

Não pode ter 2 chaves de mesmo nome em dicionários. Para verificação, pode-se ter 2 métodos:

> get()

`dicionario.get('chave', 'value')`

Caso chave exista, retorna valor de _value_, caso chave não exista no dicionário retorna _None_.

Parâmetros obrigatórios:
- _chave_
- _value_

> setdefault()

`dicionario.setdefault('chave', 'value')`

Valida de há ou não chave e caso não exista, cria item com nome da _chave_ e com _value_ informado.
Caso chave exista, nada acontece.

Parâmetros obrigatórios:
- _chave_
- _value_

> _in_

>`chave in dicionário.keys()`

Usado junto com laços de repetições ou loops, verifica em toda a cadeia de chaves do dicionário. 

##### Adicionar item

`dicionario[chave] = valor`

Método para inserção ou alteração direta no dicionário. 

> NOTA: __Sempre__ verificar se chave já existe. Caso exista, será feita a substituição para novo valor.


##### Remover item 

`dicionario.pop(chave)`

Parâmetros obrigatórios:
- _chave_

##### Alterar nome chave

Diretamente falando, não é possível efetuar alteração direta no dicionário. O que ocorre é inserção e remoção de uma 
chave.
Não se consegue efetuar alteração de chave por método direto.

Método alteração 1:

Atribui valor chave antiga na nova e apaga chave antiga

```python
dicionario[novaChave] = dicionario[antigaChave]
del dicionario[antigaChave]
```

Método alteração 2:

Faz mesma operação que método 1, porém com uma única chamada através do comando _pop()_.

`dicionario[novaChave] = dicionario.pop(antigaChave)`
***
***

>#### Exercício(Lista, Tupla, Dicionário)
>
>
>1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
>2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
>3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela
>4. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
>números IMPARES no vetor impar. Imprima os três vetores
>5. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima 
>o número de alunos com média maior ou igual a 7.0.
>6. Foram anotadas as idades e alturas de 30 pessoas. Faça um Programa que determine quantas pessoas com mais de 13 anos 
>possuem altura inferior à média de altura dessas pessoas.
>7. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados 
>quando for informado um valor igual a -1 (que não deve ser armazenado).
> 
>   Após esta entrada de dados, faça:
>   - Mostre a quantidade de valores que foram lidos;
>   - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
>   - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
>   - Calcule e mostre a soma dos valores;
>   - Calcule e mostre a média dos valores;
>   - Calcule e mostre a quantidade de valores acima da média calculada;
>
>8. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
>
>   - Resultado final:
>   - Atleta: Rodrigo
>   - Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
>   - Média dos saltos: 5.9 m
>
>9. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer 
>um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
>encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
>Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número 
>indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito.
>Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
>    - Quantidade de mouses: 100
>    - Situação                        Quantidade              Percentual
>    - 1- necessita da esfera                  40                     40%
>    - 2- necessita de limpeza                 30                     30%
>    - 3- necessita troca do cabo ou conector  15                     15%
>    - 4- quebrado ou inutilizado              15                     15%
>
>10. No dicionário abaixo, temos os dados de acesso de 3 usuários, cada um com seu login e senha, onde o login é a chave 
>e a senha o valor.
>Faça um script que peça ao usuário seu login e senha, se tiver certo envie uma mensagem de acesso autorizado, se fornecer 
>a senha errada, informe o erro.
>    - loginSenha={'joao'   : 'rush', 'maria'  : 'yes', 'zezinho': 'genesis'}
>
>11. Uma escola quer que você crie um script que exiba o seguinte menu:
>
>    - 0 Sair
>    - 1 Exibir lista de alunos com suas notas (cada aluno tem uma nota)
>    - 2 Inserir aluno e nota
>    - 3 Alterar a nota de um aluno
>    - 4 Consultar nota de um aluno específico
>    - 5 Apagar um aluno da lista
>    - 6 Dar a média da turma
>
>    Onde a professora que vai fornecer o nome e nota dos alunos. Quantos ela quiser. Quantas vezes quiser.
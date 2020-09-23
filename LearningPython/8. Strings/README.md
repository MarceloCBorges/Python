## String

String --> sequência de caracteres, podendo ser letras (maiúsculas ou minúsculas), acentos, caracteres especiais, outros 
próprios da computação quebras de linha ou tabulação (\n e \t). Strings são imutáveis.

#### Caracteres de um texto

Pode-se acessar cada caractere individualmente de um determinado texto.

```python
texto = "Leitura de texto"

for caractere in texto:
    print(caractere)
```

Também podendo ser acessado caracteres individualmente como se fossem uma lista, utilizando de suas propriedades.

```
texto[0]
texto[1]
texto[2:5]
```

#### Comprimento

Aproveitando propriedade das listas, usa o mesmo método _len()_.

`len(string)`

#### Concatenação

Operador '+'.

```
texto1 = 'string '
texto2 = 'concatenada.'
textoFinal = string concatenada.
```

#### Maiúscula/minúscula

```
string = 'Texto em maiúsculo e minúsculo.'
string = string.upper()
string = string.lower()
```

Converte texto em maiúsculo e minúsculo.
Assim como "transformar" uma string, pode-se verificar caso string for maiúscula ou minúscula.
 
```
if string.isupper()
if string.islower()
```

#### Unir e Separar Strings

> `'caract'.join(lista)`

Irá juntar lista em uma única string itens da lista separados pelo que for determinado em _caract_.

> `string.split('info')`

Irá transformar string em uma lista, sendo _info_ o delimitador para separação da string. Caso em branco, será utilizado 
espaços em branco, caso contrário o que for informado.  

#### Buscar

Métodos para buscar uma substring dentro de uma string principal.

> `texto.endswith(substring)`

Busca substring que esteja no final do texto principal.

> `texto.startswith(substring)`

Busca substring que esteja no início do texto principal.

> `texto.find(substring)`

Busca substring que esteja em qualquer posição do texto principal.

#### Substituir 

> `texto.replace(antiga, nova)` 

Método para substituir uma substring.


##### Caracteres Especiais

* \\ - Exibe uma barra
* \' - Exibe a aspa simples
* \" - Exibe a aspa dupla
* \a - Dá um bipe
* \b - Retrocesso
* \f - Avanço
* \n - Caractere de nova linha (enter)
* \r - Carriage return
* \t - Tab horizontal
* \v - Tab vertical
***
#### Métodos com strings

> ```
> "b" in "abc"     
> "d" in "abc"     
> ```

Verifica se caractere compreende dentro do texto. Retorna _True_ ou _False_

> `str(string)`

Converte texto em string.

> `string.strip()`

Retira espaços em branco no começo e no fim.

> `if string.isalpha()`

Verifica se string são somente letras.

> `if string.isdecimal()`

Verifica se string são somente números.

> `if string.isalnum()`

Verifica se string são compostas por somente letras e  números(sem caracteres especiais ou está vazia).

> `if string.isspace()`

Verifica se há espaço em branco, tabulação ou quebra de linha.
***

## Expressão Regular

Busca por elementos específicos em um número ilimitado de informações (uma base de informações contendo o cadastro de 
clientes de um banco, por exemplo) e sem padrão definido.
Tomando como exemplo a busca por todos e-mails cadastrados, não conseguimos buscar por substrings pois não sabemos qual 
é e-mail específico de cada cliente, as únicas informações que temos:

- algum texto
- @
- algum site
- .com ou .com.br
 
Com o uso de expressões regulares, pode-se montar em poucas linhas uma expressão que retorne todos os e-mails buscados.

`import re`

Necessário importar módulo de  ___Expressão Regular___.

> `re.compile(padrão, string)`

Objeto de uma expressão regular, usada caso expressão for repetida diversas vezes. 
Podendo ser passado como parâmetro do método um objeto de expressão regular.
Retorna um dado tipo _Objeto_.

> `re.search(padrão, string)`

Busca em toda a string uma equivalência do padrão.
Retorna um dado tipo _Match_.

> `.group()`

Armazena todas as correspondências da regex encontradas na string.
Caso contenha grupo na regex, utilizar os métodos _compile()_ e _search()_
Pode-se "separar" o retorno em grupos, para poder acessar cada um individualmente. Desde que seja utilizado _(__)_ para
dividir o objeto de busca.  

> `re.findall(padrão, string)`

Retorna uma lista com todas ocorrências encontradas.

> `re.match(padrão, string)`

Encontra equivalência caso ocorra no início da string.

> __`|`__

Símbolo de condição _OU_ em expressões regulares. 

> __`?`__

Utilizado para quando item é opcional, ou seja, item pode ou não estar lá.
Deve-se estar separado em um grupo _(xx)?_

> __`*`__

Item pode conter __nenhuma__ ou infinitas vezes.
(a)* = ' ' ou a ou aa ou aaaaaaaa ou aaaaaaaaaaaaaaa...
Deve-se estar separado em um grupo.

> __`+`__

Item pode conter __uma__ ou infinitas vezes.
(a)+ =  ou a ou aa ou aaaaaaaa ou aaaaaaaaaaaaaaa...
Deve-se estar separado em um grupo.

> __`^`__

Busca correspondência no início da string.
Deve-se estar separado em um grupo.

> __`$`__

Busca correspondência no final da string.
Deve-se estar separado em um grupo.

> __`.`__

Coringa. Detecta toda e qualquer string informada após ponto (__.__).
Não reconhece quebra de linha.

> __`.*`__

Detecta _tudo_.
Não reconhece quebra de linha.

> __`re.DOTALL`__

Item coringa também reconhece quebra de linha.
Passar como segundo argumento da re.compile()

> __`re.IGNORECASE ou re.I`__

Faz busca sem se importar letras maiúsculas ou minúsculas.
Passar como segundo argumento da re.compile().

> `Substituição`

Busca por uma string e a substitui por uma nova.

> `re.compile(r'regex', re.VERBOSE)`

Ignora espaços em branco e comentários. Conforme regex for ficando muito grande.
Método de _re.compile_ 


#### Classes de Caracteres

* \d - Qualquer dígito de 0 a 9.
* \D - Qualquer caractere que não seja um dígito (contrário de \d).
* \w - Qualquer letra, dígito ou o caractere underscore (qualquer caractere de uma palavra).
* \W - Qualquer caractere que não seja uma letra, um dígito ou o underscore (contrário de \w).
* \s - Qualquer espaço, tabulação ou caractere de quebra de linha,  ou seja, qualquer espaçamento.
* \S - Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha (contrário de \S).
* [a-zA-Z] - Letras minúsculas e maiúsculas.
* [a-zA-Z0-9] - Qualquer tipo de letras e números de 0 a 9.
* [0-X] - Números de 0 a X.
##Resumo:
    Efetuar leitura de um arquivo ‘master’ de projetos e verificar qual período de contratos, gerando um relatório de prioridades, informando o período dos mesmos e envia-lo via e-mail.
***
##Linguagens:
Python
Pandas(biblioteca Python)
***
##Funcionamento:
   Através da linguagem Python juntamente com a biblioteca PANDAS, o programa efetuará a leitura de determinadas informações do arquivo mestre (informações que contenham as datas de fim de contrato e status do projeto).
   Para cada linha de leitura do projeto, é identificado o status do projeto, onde caso o mesmo esteja em status PENDENTE, e verificado sua data de término de contrato e caso esteja com status de CONCLUÍDO ou CANCELADO, ele é ignorado.
   Com stattus pendente e a data de término de contrato, será realizada uma comparação com data do dia (retirada pelo próprio programa do sistema do Windows) e de acordo com seu período restante, coloca-lo em uma lista de prioridades. Abaixo segue a lisa de período x prioridades:

Período menor  a 1 mes, prioridade URGENTE.
Período menor/igual a 3 meses, prioridade ALTA.
Período de 6 a 3 meses, prioridade MÉDIA.
Período maior de 6 meses, SEM PRIORIDADE.

•	Os projetos com status em pendente, são inseridos em uma lista e realizado o envio 1x por semana. (segunda-feira)
•	O relatório de final de contrato, serão enviados 2x por semana(segunda-feira e quinta-feira)


Etapas de desenvolvimento:
Etapa 1 -> Efetuar leitura do arquivo e filtrar informações necessárias.
Etapa 2 -> Leitura de data do windows para cálculo do período.
Etapa 3 -> Gerar relatório com informações encontradas. 
Etapa 4 -> Enviar relatório por e-mail.

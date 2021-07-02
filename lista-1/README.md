# Lista 1 

**Questão 1:** Como um classificador não sequencial pode ser modificado para identificar padrões sequenciais?

**R:** Tal feito pode ser alcançado introduzindo-se memória (blocos de atraso) na entrada do classificador, que não mais receberá os dados de forma paralela, mas sim sequencial. A figura a seguir ilustra a modificação indicada.

![](https://user-images.githubusercontent.com/48038742/124295644-78b4e900-db2f-11eb-95e5-89fb556c3cee.png)



**Questão 2:** Descreva o que caracteriza os seguintes problemas na área de aprendizagem de máquina: classificação, regressão, clustering.

**R:** O problema de classificação consiste em reconhecer à qual classe um determinado elemento observado pertence.

O problema de regressão consiste em determinar uma equação matemática que relacione os dados de saída como função dos dados de entrada.

O problema de clustering consiste em agrupar amostras semelhantes de um conjunto de dados, obedecendo uma determinada métrica.





**Questão 3:** Em reconhecimento de padrões, o que é um problema linearmente separável?

**R:** Um problema é dito linearmente separável quando as classes de seu conjunto de dados podem ser separadas por um ente linear (linha, plano, hiperplano, etc...). A figura a seguir ilustra um conjunto linearmente separável e outro não, no caso bidimensional.

![](https://jtsulliv.github.io/images/perceptron/linsep_new.png?raw=True)



**Questão 4:** Como um classificador linear pode ser modificado para identificar padrões não lineares?

**R:** Uma possível abordagem é realizar uma transformação nos dados, gerando assim um novo espaço de maior dimensionalidade, no qual os dados sejam linearmente separáveis, possibilitando a utilização de um classificador linear. Na figura abaixo é ilustrado o processo.

![](https://miro.medium.com/max/1400/1*zWzeMGyCc7KvGD9X8lwlnQ.png)



**Questão 5:** Considerando a base de dados do Iris, calcule os vetores de média, matrizes de covariância e probabilidades a priori para cada uma das classes da base de dados. Represente os vetores e matrizes com a mesma sintaxe utilizada no Scilab. (notação vetor coluna, "[" para delimitar o início do vetor ou matriz, "]" para delimitar o fim do vetor ou matriz, ";" para delimitar as linhas e "," para as colunas.)





**Questão 6:** Considerando a base de dados "wine", implemente um classificador para determinar a que classe um determinado vinho pertence. O classificador deve apresentar uma saída por classe e deve ser um das seguintes opções: KNN ou Bayesiano. Para determinar a taxa de acerto do sistema deve ser utilizada validação cruzada 5 folds e o resultado deve ser plotado utilizando uma matriz de confusão.
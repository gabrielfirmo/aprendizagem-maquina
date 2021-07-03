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

**R:** Os vetores de média são denotados por ![](https://latex.codecogs.com/gif.latex?%5Cbar%7B%5Cmathbf%7Bx%7D%7D_i), as matrizes de covariância por ![](https://latex.codecogs.com/gif.latex?%5Cmathbf%7B%5CSigma%7D_i) e as probabilidades a priori por ![](https://latex.codecogs.com/gif.latex?p_i). O dataset Iris possui 3 classes: Iris-setosa, Iris-versicolor e Iris-virginica, que são mapeadas em 0, 1 e 2, respectivamente. Assim temos o seguinte:


![](https://latex.codecogs.com/gif.latex?%5Cbar%7B%5Cmathbf%7Bx%7D%7D_0%20%3D%20%5Cbegin%7Bbmatrix%7D%205.006%5C%5C%203.418%5C%5C%201.464%5C%5C%200.244%20%5Cend%7Bbmatrix%7D)

![](https://latex.codecogs.com/gif.latex?%5Cmathbf%7B%5CSigma%7D_0%20%3D%20%5Cbegin%7Bbmatrix%7D%200.12424898%20%26%200.10029796%20%26%200.01613878%20%26%200.01054694%5C%5C%200.10029796%20%26%200.14517959%20%26%200.01168163%20%26%200.01143673%5C%5C%200.01613878%20%26%200.01168163%20%26%200.03010612%20%26%200.00569796%5C%5C%200.01054694%20%26%200.01143673%20%26%200.00569796%20%26%200.01149388%20%5Cend%7Bbmatrix%7D)

![](https://latex.codecogs.com/gif.latex?p_0%20%3D%20%5Cfrac%7B1%7D%7B3%7D)


![](https://latex.codecogs.com/gif.download?%5Cbar%7B%5Cmathbf%7Bx%7D%7D_1%20%3D%20%5Cbegin%7Bbmatrix%7D%206.588%5C%5C%202.974%5C%5C%205.552%5C%5C%202.026%20%5Cend%7Bbmatrix%7D)   ![](https://latex.codecogs.com/gif.download?%5Cmathbf%7B%5CSigma%7D_1%20%3D%20%5Cbegin%7Bbmatrix%7D%200.40434286%20%26%200.09376327%20%26%200.3032898%20%26%200.04909388%5C%5C%200.09376327%20%26%200.10400408%20%26%200.07137959%20%26%200.04762857%5C%5C%200.3032898%20%26%200.07137959%20%26%200.30458776%20%26%200.04882449%5C%5C%200.04909388%20%26%200.04762857%20%26%200.04882449%20%26%200.07543265%20%5Cend%7Bbmatrix%7D)   ![](https://latex.codecogs.com/gif.download?p_1%20%3D%20%5Cfrac%7B1%7D%7B3%7D)


![](https://latex.codecogs.com/gif.download?%5Cbar%7B%5Cmathbf%7Bx%7D%7D_2%20%3D%20%5Cbegin%7Bbmatrix%7D%206.588%5C%5C%202.974%5C%5C%205.552%5C%5C%202.026%20%5Cend%7Bbmatrix%7D)   ![](https://latex.codecogs.com/gif.download?%5Cmathbf%7B%5CSigma%7D_2%20%3D%20%5Cbegin%7Bbmatrix%7D%200.40434286%20%26%200.09376327%20%26%200.3032898%20%26%200.04909388%5C%5C%200.09376327%20%26%200.10400408%20%26%200.07137959%20%26%200.04762857%5C%5C%200.3032898%20%26%200.07137959%20%26%200.30458776%20%26%200.04882449%5C%5C%200.04909388%20%26%200.04762857%20%26%200.04882449%20%26%200.07543265%20%5Cend%7Bbmatrix%7D)   ![](https://latex.codecogs.com/gif.download?p_2%20%3D%20%5Cfrac%7B1%7D%7B3%7D)

Os resultados foram obtidos utilizando o script em _Python_ **_createStatisticsIris.py_** e podem ser acessados pelo arquivo **_statisticsIris.sce_**  de acordo com a sintaxe do _scilab_.



**Questão 6:** Considerando a base de dados "wine", implemente um classificador para determinar a que classe um determinado vinho pertence. O classificador deve apresentar uma saída por classe e deve ser um das seguintes opções: KNN ou Bayesiano. Para determinar a taxa de acerto do sistema deve ser utilizada validação cruzada 5 folds e o resultado deve ser plotado utilizando uma matriz de confusão.


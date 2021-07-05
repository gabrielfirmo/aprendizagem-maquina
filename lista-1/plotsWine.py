import numpy as np
from tools import *
from classifiers import *
import matplotlib.pyplot as plt

# Parâmetros
kRange = 31
numClasses = 3
numFolds = 5

X = readWineDataset("datasets/wine/wine.data")
trainSet, testSet = kFolds(numFolds, X)


# Lista das taxas de acertos para as diferentes métricas
AccE = []
AccC = []
# Utilizando o classificador KNN
for k in range(1,kRange):
    hitsEuclidian = 0
    hitsCosine = 0
    total = 0
    for i in range(numFolds):
        actual = testSet[i][:, -1]
        predict = knn(k, trainSet[i], testSet[i][:, :-1], metric='cosine')
        hitsCosine+= np.sum([1 if x==y else 0 for x,y in zip(predict,actual)])

        predict = knn(k, trainSet[i], testSet[i][:, :-1], metric='euclidian')
        hitsEuclidian+= np.sum([1 if x == y else 0 for x, y in zip(predict, actual)])
        total+=len(predict)

    accE = hitsEuclidian/total*100
    accC = hitsCosine/total*100
    print(f"k = {k} | Hit ratio = {hitsEuclidian}/{total} = {accE:.2f} %")
    print(f"k = {k} | Hit ratio = {hitsCosine}/{total} = {accC:.2f} %\n")
    AccE.append(accE)
    AccC.append(accC)


k = np.arange(1,kRange)
plt.plot(k, AccC, 'ro', linestyle='dashed', label='Cosine Similarity metric')
plt.plot(k, AccE, 'bo', linestyle='dashed', label='Euclidian Distance metric')

plt.title('Hit Ratio for Wine Dataset using KNN')
plt.xlabel('k')
plt.ylabel('Hit Ratio (%)')
plt.xticks(np.arange(kRange,step=kRange//6))
plt.show()
plt.legend()
plt.savefig('img/wineKNN.png')
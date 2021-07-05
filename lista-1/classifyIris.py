import numpy as np
from classifiers import *
from tools import *

"""Classificação do dataset Iris """

# Parâmetros
k = 5
numClasses = 3
numFolds = 5

# Leitura do dataset
X, _, _, _ = readIrisDataset('datasets/iris/iris.data')
# Aplicação do método de validação cruzada no dataset
trainSet, testSet = kFolds(numFolds, X)

# Utilizando o classificador KNN
confusion = np.zeros((numClasses, numClasses))
for i in range(numFolds):
    actual = testSet[i][:, -1]
    predict = knn(k, trainSet[i], testSet[i][:, :-1])
    confusion+= confusionMatrix(numClasses, predict, actual)
print("Confusion KNN")
print(confusion)
hits = confusion.trace(dtype=int)
miss = np.sum(confusion, dtype=int)
print(f"Hit ratio = {hits}/{miss} = {hits/miss*100:.2f} %\n")

# Utilizando o classificador Bayesiano
confusion = np.zeros((numClasses, numClasses))
for i in range(numFolds):
    actual = testSet[i][:, -1]
    predict = bayes(numClasses, trainSet[i], testSet[i][:, :-1])
    confusion+= confusionMatrix(numClasses, predict, actual)
print("Confusion Bayes")
print(confusion)
hits = confusion.trace(dtype=int)
miss = np.sum(confusion, dtype=int)
print(f"Hit ratio = {hits}/{miss} = {hits/miss*100:.2f} %\n")


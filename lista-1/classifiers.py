import numpy as np
from tools import *


# Implementação do classificador knn
# k é o parâmetro de vizinhos
# trainSet é a matriz do conjunto de treinamento, assumindo que o rótulo é o último elemento de cada coluna
# testSet é a matriz do conjunto de teste, assumindo que não há rótulo
# Retorna o vetor predict com as classes previstas para cada elemento do conjunto de testes
def knn(k, trainSet, testSet, metric='euclidian'):
    predict = []
    labels = trainSet[:, -1]
    for i in range(testSet.shape[0 ]):
        D = []
        testSample = testSet[i]

        for j in range(trainSet.shape[0]):
            trainSample = trainSet[j, :-1]
            if metric == 'euclidian':
                d = euclidianDistance(testSample, trainSample)
            elif metric == 'cosine':
                d = cosineSimilarity(testSample, trainSample)
            else:
                raise ValueError("Invalid metric")

            D.append((j, d))

        # D é uma lista que contêm as tuplas (índice, distância)
        # Ordena D de acordo com as distâncias
        D.sort(key=lambda x: x[1])

        # Dicionário para fazer a contagem dos rótulos mais próximos
        count = {}
        for j in range(k):
            label = labels[D[j][0]]
            if label in count:
                count[label]+=1
            else:
                count[label] = 1

        # Verifica o rótulo mas frequente
        mostFrequent = max(count.items(), key=lambda item: item[1])[0]

        predict.append(mostFrequent)


    return predict


# Implementação do classificador knn
# numClasses é a quantidade total de classes
# trainSet é a matriz do conjunto de treinamento, assumindo que o rótulo é o último elemento de cada coluna
# testSet é a matriz do conjunto de teste, assumindo que não há rótulo
# Retorna o vetor predict com as classes previstas para cada elemento do conjunto de testes
def bayes(numClasses, trainSet, testSet):
    # Vetor de propbabilidades a priori
    p = []
    # Matrizes de classes
    X = []
    # Vetores de média
    xm = []
    # Matrizes de Covariância
    Cv = []
    # Vetor de saída
    predict = []

    # Calcula os vetores média, matrizes de covariância e probabilidades a priori para cada classe
    for i in range(numClasses):
        X.append(trainSet[trainSet[:, -1] == i][:, :-1])
        p.append(prioriProbability(X[i], trainSet))
        xm.append(meanVector(X[i]))
        Cv.append(covarianceMatrix(X[i], xm[i]))


    for i in range(testSet.shape[0]):
        x = testSet[i]
        # Calcula a função discriminante g para cada classe
        g = np.zeros(numClasses)
        for j in range(numClasses):
            g[j] = -0.5*np.log(np.linalg.det(Cv[j])) - 0.5*(x-xm[j]).dot(np.linalg.inv(Cv[j])).dot((x-xm[j]).T) + np.log(p[j])

        # A amostra é classificada de acordo com o maior valor de discriminante
        predict.append(np.argmax(g))
    return predict








import pandas as pd
import numpy as np

"""
Módulo que contém funções auxiliares para facilitar a implementação dos algoritmos de machine learning
"""

# Função para realizar a leitura do dataset Iris
# Retorna as matrizes de dados de cada classe (matriz linha)
def readIrisDataset(file):
    # Leitura do dataset Iris
    iris = pd.read_csv(file, header=None)
    iris.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']

    # Indexação das classes
    iris['label'] = iris['label'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

    # Transforma em matriz
    iris = iris.to_numpy()

    # Extração dos dados de entrada para cada classe
    X0 = iris[iris[:, 4] == 0][:, :-1]
    X1 = iris[iris[:, 4] == 1][:, :-1]
    X2 = iris[iris[:, 4] == 2][:, :-1]

    return iris, X0, X1, X2


# Função para realizar a leitura do dataset Iris
# Retorna as matrizes de dados de cada classe (matriz linha)
def readWineDataset(file):
    # Leitura do dataset Iris
    wine = pd.read_csv(file, header=None)
    # Transforma em matriz
    wine = wine.to_numpy()
    # Realiza um shift para a esquerda, deixando assim o rótulo na última coluna
    wine = np.roll(wine, -1, axis=1)
    # Faz os rótulos irem de 0-2 ao invés de 1-3
    wine[:, -1]-=1
    return wine


# Função para calcular o vetor de médias
# X é a matriz dos dados de entrada (matriz linha)
def meanVector(X):
    return X.mean(axis=0)


# Função para calcular a matriz de covariância
# x são os dados de entrada (matriz linha)
# xm é o vetor de médias (vetor linha)
def covarianceMatrix(X, xm):
    return (X-xm).T.dot(X-xm)/(X.shape[0]-1)


# Função para calcular a probabilidade a priori de uma classe
def prioriProbability(Xi, X):
    return Xi.shape[0]/X.shape[0]


# Função para calcular a distância euclidiana entre dois vetores
def euclidianDistance(x,y):
    d = np.linalg.norm(x-y)
    return d

# Função para calcular a similaridade entre dois vetores
# Quando cos=1 a similaridade é máxima, logo a distância é mínima. Portanto retorna-se o negativo do cos
def cosineSimilarity(x,y):
    cos = x.dot(y)/(np.linalg.norm(x)*np.linalg.norm(y))
    return -cos

# Função para determinar os conjuntos de treino e teste de acordo com o método de validação cruzada k-folds
def kFolds(k,X):
    # Define um seed para que o embaralhamento do dataset seja sempre o mesmo
    rng = np.random.default_rng(1)
    rng.shuffle(X)

    # N = Quantidade total de asmostras do dataset
    N = X.shape[0]
    # M = Quantidade de atributos de cada asmostra
    M = X.shape[1]

    # Divide as amostras em k pastas
    folds = (k+1)*[np.empty((0,M))]
    for i in range(N):
        folds[i%k] = np.append(folds[i%k],[X[i]], axis=0)

    # Rearranja as pastas em k conjuntos de teste (1 pasta) e treino (k-1 pastas)
    trainSet = []
    testSet = []
    for i in range(k):
        testSet.append(folds[i])
        samples = np.empty((0,M))
        for j in range(k):
            if i!=j:
                samples = np.append(samples, folds[j], axis=0)
        trainSet.append(samples)

    return trainSet, testSet


# Função para calcular a matriz confusão
# M é a quantidade de classes
# predict é o vetor com as classes previstas pelo classificador
# actual é o vetor com os rótulos verdadeiros
def confusionMatrix(M, predict, actual):
    N = len(actual)
    confusion = np.zeros((M,M))
    for i in range(N):
        confusion[int(actual[i])][int(predict[i])]+=1

    return confusion


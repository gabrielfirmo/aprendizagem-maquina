import pandas as pd
import numpy as np

"""
Módulo que contém funções auxiliares para facilitar a implementação dos algoritmos de machine learning
"""

#Função para realizar a leitura do dataset Iris
#Retorna as matrizes de dados de cada classe (matriz linha)
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


# Função para calcular o vetor de médias
# X é a matriz dos dados de entrada (matriz linha)
def meanVector(X):
    return X.mean(axis=0)


# Função para calcular a matriz de covariância
# x são os dados de entrada (matriz linha)
# xm é o vetor de médias (vetor linha)
def covarianceMatrix(X, xm):
    return (X-xm).T.dot(X-xm)/(X.shape[0]-1)

#Função para calcular a probabilidade a priori de uma classe
def prioriProbability(Xi, X):
    return Xi.shape[0]/X.shape[0]
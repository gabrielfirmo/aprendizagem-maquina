# Módulo criado para auxiliar no desenvolvimento dos algoritmos
from utils import *

#Xi são as matrizes de dados do dataset Iris para cada classe i
X, X0, X1, X2 = readIrisDataset('datasets/iris/iris.data')

#xmi são os vetores de média para cada classe i
#Cvi são as matrizes de covariância para cada classe i
#pi são as probabilidades a priori para cada classe i
xm0 = meanVector(X0)
Cv0 = covarianceMatrix(X0, xm0)
p0 = prioriProbability(X0, X)
print("xm0 =", xm0)
print("Cv0 =", Cv0)
print("p0 =", p0, "\n\n")

xm1 = meanVector(X1)
Cv1 = covarianceMatrix(X1, xm1)
p1 = prioriProbability(X1, X)
print("xm1 =", xm1)
print("Cv1 =", Cv1)
print("p1 =", p1, "\n\n")

xm2 = meanVector(X2)
Cv2 = covarianceMatrix(X2, xm2)
p2 = prioriProbability(X2, X)
print("xm2 =", xm2)
print("Cv2 =", Cv2)
print("p2 =", p2, "\n\n")
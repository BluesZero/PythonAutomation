#Linear Regression
'''
Y=β0+β1X+ϵ

Y representa el precio de la casa.
X es el año de la transacción.
β0 es la intersección con el eje Y (el precio de base cuando X=0)
β1 es la pendiente de la línea, indicando cómo cambia el precio de la casa por año.
ϵ es el término de error, representando la variación en 
Y no explicada por X.

β1 = N∑(XY)−∑X∑Y/N∑X^2−(∑X)^2
β0 = Yprom - β1Xprom

Donde:
N es el número total de observaciones.
∑(XY) es la suma del producto de los valores de X e Y.
∑X y ∑Y son las sumas de los valores de X e Y respectivamente.
Xprom y Yprom son los promedios de los valores de X e Y.

Para hacer una predicción para un año futuro, simplemente reemplazamos 
X en la ecuación del modelo con el año para el que queremos predecir. Por ejemplo, para predecir el precio en el año 2050, si = 2050
X=2050, la predicción sería:
Y=β0+β1 (2050)
'''
#Sumatory
def sumList(list):
  sumList = 0
  n = len(list)
  for i in range (0, n):
    sumList = list[i] + sumList
  return sumList

#Product sumatory
def sumXY(X,Y):
  n = len(X)
  sumXY = 0
  for i in range (0, n):
    sumXY = (X[i] * Y[i] + sumXY)
  return sumXY

#Promedy Sumatory
def sumProm(list):
  sumProm = 0
  n = len(list)
  sumProm = (sumList(list)/n)
  return sumProm

#Sqrt Sumatory

def sumSqrt():
  XTemp = []
  for i in range(0, N):
    XTemp.append(X[i] ** 2)
  return XTemp

X = [2015,  2016,  2017,  2018,  2019,  2020,  2021,  2022,  2023]
Y = [200000,200200,200300,200400,200500,200600,200700,200800,200900]

#β1 = N∑(XY)−∑X∑Y/N∑X^2−(∑X)^2
#β0 = Yprom - β1Xprom

N = len(Y)
sumXY = sumXY(X,Y)
sumX  = sumList(X)
sumY  = sumList(Y)
Xprom = sumProm(X)
Yprom = sumProm(Y)
X2 = sumSqrt()

#B1 = ((N * sumXY) - (sumX * sumY))/((N * (sumList([x**2 for x in X]))) - (sumX ** 2))
B1 = ((N * sumXY) - (sumX * sumY))/((N * (sumList(X2))) - (sumX ** 2))
B0 = ((Yprom) - (B1 * Xprom))

year = int(input('Inserte hasta que año quiere predecir: '))

i = X[-1] #Empezar en el ultimo año

for i in range(i + 1, year + 1):
  print(f"De acuerdo a los datos la casa valdra {round((B0+(B1 * year)),2)} en el año: {i}")
  year = year + 1

#Cargando la librería de "numpy" dando una abreviación llamado "np".
import numpy as np

#Al igual la librería randint que significa un número entero aleatorio a la cual proviene del metodo random.
from random import randint

#De la misma manera se importa la líbreria "matplolib" a la cul donde proviene y se importa los ejes de un gráfico.
# con la abreviación plt.
import matplotlib.pyplot as plt

#Por utlimo otra libreria "seaborn" para gráficos estadisticos a la cual se abrevia "sns"
import seaborn as sns

"""Se declaran variables matrices para los 12 niveles las barras de color que se representan en ceros para hacer la simulación
de números aleatorios entre el uno y cero para el uso de relleno."""
niveles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
barras = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""Variables con nombre "canicas" para el número de canicas a la cual nos piden en este caso 3000, de tipo entero. Luego 
otra variable de igual valor para utilizar el salto a otra barra en los 12 niveles."""
canicas = 3000
salto = 0

#Utilizamos esta función para calcular el gráfico de Galtón 
def Calcular() :

    """Se nesecita dos ciclos for para las canicas y para los 12 niveles, se nesecitas el salto del relleno y distribución 
    a la cual son las 3000 canicas de manera aleatoria."""
    for i in range(canicas):
        salto = -1
        for j in range(12):
            salto = salto + randint(0, 1)
        barras[salto] = barras[salto] +1

#Dando el returno del resultado dado por las barras rellenas y pixeleadas de manera gráfica.
    return barras
    
"""En esta función llamado "Gráfico " para poner el nombre de título, etiquetas a los ejes (x) y (y)."""

def Grafica() :
    plt.title("Grafica de Galtón")
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')

    """Llamando a la matriz de los 12 niveles que se almacena en la variable (x) y la función Cálcular para que se almacene en (y),
    y se empieza a definir el ancho de los datos estadisticos."""

    sns.barplot(x= niveles, y=Calcular(),width=-1)
    plt.show()

#Se imprime la función Cálcular dentro de gráfica a la cual el metodo tiene el mismo nombre.    
print(Calcular())
Grafica()

from matplotlib import pyplot as plt
import numpy as np
import random


def individuo(min, max):
    return[random.randint(min, max) for i in range(largo)]

def crearPoblacion(num):
    return [individuo(1,1000) for i in range(num)]

def seleccion_y_reproduccion(poblacion, alcance):
    puntuados = [ (calcularFitness(i), i) for i in poblacion] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    puntuados = [i[1] for i in sorted(puntuados)] #Ordena los pares ordenados y se queda solo con el array de valores
    poblacion = puntuados
  
    seleccionados =  puntuados[(len(puntuados) - alcance):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(poblacion)-alcance):
        punto = random.randint(1,largo-1) #Se elige un punto para hacer el intercambio
        padre = random.sample(seleccionados, 2) #Se eligen dos padres
          
        poblacion[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        poblacion[i][punto:] = padre[1][punto:]
  
    return poblacion # se retorna la nueva poblacion de individuos

def mutar(poblacion, probabilidad_de_mutacion, alcance):
    for i in range(len(poblacion) - alcance):
        if random.random() <= probabilidad_de_mutacion: #Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(1,1000) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == poblacion[i][punto]:
                nuevo_valor = random.randint(1,1000)
  
            #Se aplica la mutacion
            poblacion[i][punto] = nuevo_valor
  
    return poblacion

def calcularFitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        # calcular fitness aquí!
        kp = individuo[0]
        kd = individuo[1]
        ad = objetivo[0]
        ai = 0
        t = np.linspace(0,1,100)
        a = respuesta(kp, kd, ad, ai, t)
        fitness = -abs(max(a)-ad) 
    return fitness

def respuesta(kp, kd, ad, a0, t):
    a = np.zeros(t.size)
    for i in range(t.size):
        if i < 2:
            a[i] = a0
        else:
            dt = t[i]-t[i-1]
            a[i] = (kp*dt**2*ad+a[i-1]*(2+kd*dt)-a[i-2])/(1+kp*dt**2+kd*dt)
    return a


# Ejemplo de uso de la función
ad = 10    # altura de destino
a0 = 0     # altura inicial
kp = 500   # constante proporcional
kd = 10    # constante diferencial

t = np.linspace(0,1,1000)

# respuesta
a = respuesta(kp, kd, ad, a0, t)
plt.plot(t,a)
plt.show(block=False)
plt.pause(2)
plt.clf()

# Tres respuestas posibles
a1 = respuesta(500, 10, ad, a0, t)
a2 = respuesta(500, 20, ad, a0, t)
a3 = respuesta(500, 30, ad, a0, t)
plt.plot(t,a1)
plt.plot(t,a2)
plt.plot(t,a3)
plt.pause(2)
plt.clf()




objetivo = [5] #Objetivo a alcanzar [valor final]
largo = 2       #La longitud del material genetico de cada individuo
num = 20        #La cantidad de individuos que habra en la poblacion
alcance = 2    #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
probabilidad_de_mutacion = 0.2   #La probabilidad de que un individuo mute

poblacion = crearPoblacion(num)  #Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(poblacion)) #Se muestra la poblacion inicial

#Se evoluciona la poblacion 1
for i in range(1000):
    poblacion = seleccion_y_reproduccion(poblacion, alcance)
    poblacion = mutar(poblacion, probabilidad_de_mutacion, alcance)

print("Poblacion Final:\n%s"%(poblacion)) #Se muestra la poblacion final


# verificamos la respuesta del controlador obtenido
ad = objetivo[0]
a0 = 0
seleccionado = poblacion[-1]
kp = seleccionado[0]
kd = seleccionado[1]
t = np.linspace(0,1,1000)

a = respuesta(kp, kd, ad, a0, t)
plt.plot(t,a)
print("Buscamos encontrar el individuo que hace mejor la prediccion par evitar oscilaciones, en este caso es: ", seleccionado)
plt.pause(3)
plt.clf()







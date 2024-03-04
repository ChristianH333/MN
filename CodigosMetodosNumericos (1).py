#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np #Numpy con alias

import matplotlib.pyplot as plt #Matplotlib

from matplotlib.patches import Circle #Para insertar formas dentro de 1 gráf

def E(q, r0, x, y):
    
    dist = np.hypot(x-r0[0], y-r0[1])**3 #Calcular la hipotenusa de las coordenadas
    
    return q * (x-r0[0])/dist , q * (y-r0[1]) / dist
    
    #usaremos una malla para luego evaluar y graficar el campo
    
nx, ny = 72, 72 #Cantidad de puntos para la malla

x = np.linspace(-2, 2, nx) #Malla en x

y = np.linspace(-2, 2, ny) #Malla en y

X, Y = np.meshgrid(x,y) #Hacemos 1 matriz de valores generando la malla real

print("Especifique el no. de cargas")
cargas_unsig = len(np.arange(0,int(input()),1)) #Para que se ingrese una variable, se pasa de 1 string a 1 number

cargastotales = cargas_unsig #Copia de la variable

charges = [] #Lista vacía donde ingresaremos el valor de la carga y los componentes vectoriales x, y

print("Elija un tipo de distribución - colineal vertical, colineal horizontal, circular, carga única negativa, carga única positiva")
seleccion = input()
if seleccion == 'colineal horizontal':
    for i in range(cargastotales):
        
        q = i%2 * 2 - 1 #Esto hace que las cargas cambien
        charges.append((q, (i/(cargastotales-1)*2-1, 0))) #Imanes colineales verticales
        
        
if seleccion == 'colineal vertical':
    for i in range(cargastotales):
        
        q = i%2 * 2 - 1 #Esto hace que las cargas cambien
        charges.append((q, (0, i/(cargastotales-1)*2-1, 0))) #Imanes colineales horizontales
        
if seleccion == 'circular':
    for i in range(cargastotales):
        
        q = i%2 * 2 - 1 #Esto hace que las cargas cambien
        charges.append((q, (np.cos(2*np.pi*i/cargastotales), np.sin(2*np.pi*i/cargastotales)))) #Circular
        
if seleccion == 'carga unica negativa' and cargastotales == 1:
    q = -1
    charges.append((q,(0,0)))
    
if seleccion == 'carga unica positiva' and cargastotales == 1:
    q = 1
    charges.append((q,(0,0)))
    
if seleccion == 'colineal diagonal':
    for i in range(cargastotales):
        q = i%2 * 2 - 1 
        charges.append((q, (i/(cargastotales-1)*2-1, i/(cargastotales-1)*2-1))) #Imanes colineales diagonales
        
if seleccion == 'capacitor':
    print('Ingrese la distancia de las placas')
    distancia = float(input())
    for i in range(cargastotales):
        charges.append((1, (i/(cargastotales-1)*2-1, -distancia/2)))
        charges.append((-1, (i/(cargastotales-1*2-1, distancia/2))))
        
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

for charge in charges:

    ex, ey = E(*charge, x=X, y=Y) #Asigno un valor a cada punto de la matriz
    
    Ex += ex #Variable recursiva para la suma de campos
    
    Ey += ey 
    
fig = plt.figure()

ax = fig.add_subplot(111)

#Dibujar las líneas de flujo con mapa de colores y estilos

color = 2 * np.log(np.hypot(Ex, Ey)) #Cambia según el largo

ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno, #Crea las líneas del gráf

            density=2, arrowstyle='->', arrowsize=1.5) #Crea las líneas del gráf; Ex, Ey, mallas relacionadas a x, y
            
#Agregar círculos para las cargas
charge_colors = {True: '#aa0000', False: '#000aa'}

for q, pos in charges:
    
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0])) #Para lograr el dibujo de círculo para la carga

ax.set_xlabel('$x$')

ax.set_ylabel('$y$')

ax.set_xlim(-2,2)

ax.set_ylim(-2,2)

ax.set_aspect('equal')

plt.show()


# # Biseccion
# 

# In[14]:


import numpy as np

function = lambda x: np.sin(x)


#def f(x):
#    return float("{:.3f}".format(x**2-4))

def Biseccion(a,b,TOL,N0=100):
    #lista = []
    #contador=0
    for i in range(N0):
        distanciaMedia = (b-a)/2
        p = a+distanciaMedia
        f_p = function(p)
        f_a = function(a)
        print("a:{}\nb:{}\np:{}\n".format(f_a,b,f_p))
        if (p==0) or ((b-a)/2 < TOL):
            print("Valor p: {:.3f}".format(p))
            return float("{:.3f}".format(p))
        if (f_a * f_p > 0):
            a=p
        else:
            b=p
    return "El metodo fracaso"


#funcion_biseccion = Biseccion(1,3,0.0001,100)
#print("Resultado: " + str(funcion_biseccion))


# In[17]:


a = float(input("Ingrese punto a:"))
b = float(input("Ingrese punto b:"))
TOL = float(input("Ingrese punto tolerancia:"))
#itera = input("Ingrese punto a:")
p=Biseccion(a,b,TOL,1e6)


# In[ ]:


lista3 = []
for i in range(0,len(listaExterna)):
    lista3.append(listaExterna[i]*5)
    print


# In[ ]:





# In[ ]:


from sympy.solvers import solve
from sympy import Symbol


# In[ ]:


x = Symbol("x")
solve(x**2+3*x+72,x)


# In[ ]:


####AGREGAR EVALUACION

text2Func="(x**2)+3*x+72"

def ApplyFunction(f,var):
    funcArray=[]
    monomio=""
    for i in f:
        if i=="(":
            monomio = monomio+f[i]
            
    
ApplyFunction(text2Func,"x")


# In[ ]:


print(type(x**2+3*x+32))


# In[9]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


f = lambda x: (1-np.cos(x))/(x**2)


# In[10]:


f(np.pi/2)


# In[13]:


vector = []
for i in np.arange(0,100*np.pi,0.0001):
    vector.append(f(i))
plt.plot(vector)


# In[19]:


import IteracionPuntoFijo as IPF
import MetodoDeBiseccion as MDB
IPF.iteracion()
MDB.sadasd()



import Funciones as func
func.IFP()
func.MDB()


# In[80]:


import numpy as np

import matplotlib.pyplot as plt #Matplotlib

from matplotlib.patches import Circle #Para insertar formas dentro de 1 gráf

class MetodosNumericos:
    
    function = lambda x: np.sin(x)
    
    
    def Biseccion(self,a,b,TOL,N0=100):
        for i in range(N0):
            distanciaMedia = (b-a)/2
            p = a+distanciaMedia
            f_p = function(p)
            f_a = function(a)
            print("a:{}\nb:{}\np:{}\n".format(f_a,b,f_p))
            if (p==0) or ((b-a)/2 < TOL):
                print("Valor p: {:.3f}".format(p))
                return float("{:.3f}".format(p))
            if (f_a * f_p > 0):
                a=p
            else:
                b=p
        return "El metodo fracaso"
        
        
    def E(self,q, r0, x, y):
        dist = np.hypot(x-r0[0], y-r0[1])**3 #Calcular la hipotenusa de las coordenadas
        return q * (x-r0[0])/dist , q * (y-r0[1]) / dist
     
    
    
    def CamposElectricos(self):
        nx, ny = 72, 72 #Cantidad de puntos para la malla

        Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

        
        x = np.linspace(-2, 2, nx) #Malla en x

        y = np.linspace(-2, 2, ny) #Malla en y

        X, Y = np.meshgrid(x,y) #Hacemos 1 matriz de valores generando la malla real

        print("Especifique el no. de cargas")
        cargas_unsig = len(np.arange(0,int(input()),1)) #Para que se ingrese una variable, se pasa de 1 string a 1 number

        cargastotales = cargas_unsig #Copia de la variable

        charges = [] #Lista vacía donde ingresaremos el valor de la carga y los componentes vectoriales x, y

        
    

        print("Elija un tipo de distribución (numericamente) \n1)colineal vertical\n2)colineal horizontal\n3)circular\n4)carga única negativa\n5)carga única positiva\n6)Colineal diagonal\n7)Capacitor")
        seleccion = input()
        if seleccion == '1':
            for i in range(cargastotales):
        
                q = i%2 * 2 - 1 #Esto hace que las cargas cambien
                charges.append((q, (i/(cargastotales-1)*2-1, 0))) #Imanes colineales verticales
        
        elif seleccion == '2':
            for i in range(cargastotales):
        
                q = i%2 * 2 - 1 #Esto hace que las cargas cambien
                charges.append((q, (0, i/(cargastotales-1)*2-1, 0))) #Imanes colineales horizontales
        
        elif seleccion == '3':
            for i in range(cargastotales):
        
                q = i%2 * 2 - 1 #Esto hace que las cargas cambien
                charges.append((q, (np.cos(2*np.pi*i/cargastotales), np.sin(2*np.pi*i/cargastotales)))) #Circular
        
        elif seleccion == '4' and cargastotales == 1:
            q = -1
            charges.append((q,(0,0)))
    
        elif seleccion == '5' and cargastotales == 1:
            q = 1
            charges.append((q,(0,0)))
    
        elif seleccion == '6':
            for i in range(cargastotales):
                q = i%2 * 2 - 1 
                charges.append((q, (i/(cargastotales-1)*2-1, i/(cargastotales-1)*2-1))) #Imanes colineales diagonales
        
        ###############self.E(q,r0,x,y)       
                ###POR ARREGLAR###
        elif seleccion == '7':
            print('Ingrese la distancia de las placas')
            distancia = float(input())
            for i in range(cargastotales):
                charges.append((1, (i/(cargastotales-1)*2-1, -distancia/2)))
                charges.append((-1, (i/(cargastotales-1)*2-1, distancia/2)))
        

        for charge in charges:

            ex, ey = self.E(*charge, x=X, y=Y) #Asigno un valor a cada punto de la matriz
    
            Ex += ex #Variable recursiva para la suma de campos
    
            Ey += ey 
    
        fig = plt.figure()

        ax = fig.add_subplot(111)

#Dibujar las líneas de flujo con mapa de colores y estilos

        color = 2 * np.log(np.hypot(Ex, Ey)) #Cambia según el largo

        ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno, #Crea las líneas del gráf

                    density=2, arrowstyle='->', arrowsize=1.5) #Crea las líneas del gráf; Ex, Ey, mallas relacionadas a x, y
            
#Agregar círculos para las cargas
        charge_colors = {True: '#aa0000', False: '#0000aa'}

        for q, pos in charges:
                ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0])) #Para lograr el dibujo de círculo para la carga
        
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_xlim(-2,2)
        ax.set_ylim(-2,2)
        ax.set_aspect('equal')
        plt.show()


# In[81]:


c1=MetodosNumericos()


# In[84]:


c1.CamposElectricos()


# In[ ]:





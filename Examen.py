#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np


# In[62]:


def f(x):
    return np.cos(x) - pow(x,3)


# In[63]:


def Biseccion(a,b,TOL,N0=100):
    for i in range(N0):
        distanciaMedia = (b-a)/2
        p = a+distanciaMedia
        f_p = f(p)
        f_a = f(a)
        print("a:{}\nb:{}\np:{}\n".format(f_a,b,f_p))
        if (p==0) or ((b-a)/2 < TOL):
            print("Valor p: {:.3f}".format(p))
            return float("{:.3f}".format(p))
        if (f_a * f_p > 0):
            a=p
        else:
            b=p
    return "El metodo fracaso"


# In[64]:


def encontrar_raices_biseccion(f, a, b, TOL=1e-6):
    raices = []
    x = np.linspace(a, b, 1000)
    for k in range(len(x) - 1):
        if np.sign(f(x[k])) != np.sign(f(x[k+1])):
            raiz = Biseccion(f, x[k], x[k+1], TOL)
            raices.append(raices)
    return raices


# In[65]:


raices = encontrar_raices_biseccion(f, a, b, TOL)


# In[66]:


print("Raíces encontradas:", raices)


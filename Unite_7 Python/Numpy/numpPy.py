# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np

a= np.array([2,3,4])
print(a)
print (a.dtype)

#incrementation de array

a= np.array([2,3,4])
 
b= np.array([12,23,3])
##Les tableaux doivent etre de la ême taille
c=a+b
print(c)
c=b-a
print(c)
c=a*2
print(c)

##boucle sur array
for bla in a:
    print(bla)

##OPERATION STATIRQTIQUES SUR LES ARRAY

#SUM
print("SOMME")
print(sum(a))
print("MAX")
print(max(a))
print("MIN")
print(min(a))
print("Moyenne")
print(np.mean(a))

a=np.arange(12).reshape(3,4)
print(a)
print("Moyenne selon ligne")
print(np.mean(a,axis=0))
print("Moyenne selon colonnee")
print(np.mean(a,axis=1))
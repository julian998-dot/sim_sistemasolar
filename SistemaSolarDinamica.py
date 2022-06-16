# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:00:40 2020

@author: Julian

UNNIVERSIDAD MILITAR NUEVA GRANADA
TRABAJO FINAL DINAMICA APLICADA 1er Corte
Integrantes: DAVID GARCIA- JULIAN CORTES
Codigos 1803346- 1803147

Nota:
  1.  El codigo debe correr un timpo(7000 iteraciones ) y cerrarse el entorno tk
para que se muesre la grafica de la magnitud V y Energias en la consola.

  2. Este es un modelo aproximado que no muestra las trayecorias reales de los planetas.
  se realizo con fines educativos en un trabajo de Dinamica Aplicada en la UMNG.
  
"""

from tkinter import *; import math; import random; import time; import numpy as np
import matplotlib.pyplot as plt# SE IMPORTAN LIBRERIAS NECESARIAS O UTILES.

root=Tk()
root.geometry("2366x820")# SE CREA EL AMBIENTE MEDIANTE UNA RESOLUCION DESEADA, ESTA VARIA DEPENDIENDO DE LA PANTALLA USADA
# Se recomienda usar una pantalla de 1920 pixeles por 1080.
SolY, SolX = 337.5,762.5# POSICION DEL SOL DENTRO DEL ESPACIO TK
ObjectMass,Objectx,Objecty, Objectxvel, Objectyvel =[],[],[],[],[]# SE CREAN LISTAS DE LOS ATRIBUSTOS DE CADA PLANETA
V=[]# LISTA PARA LA MAGNITUD DEL VECTOR VELOCIDAD
E_k=[]
E_p=[]
E_T=[]
cont=-1# Contador usado para llenar el vector V
MasaSol=1100000000 # Masa del Sol en el programa ( NO REAL )
ObjectMass=[1100,1100,1400,1350,1600,1500,1500,1500,1500]# MASAS DE LOS PLANETAS (NO REAL)
ObjectR=[9*2,10*2,14.5*2,13*2,25*2,22*2,15*2,13*2,10*2]# Radios de los planetas
#ObjectR=[10,10,10,10,10,10,10,10,10]# Radios de los planetas para graficar orbitas
for i in range(9):   # Numero planetas
    
    Objectx.append(i*40+1200)#Posiciones de los planetas separados linealmente
    Objecty.append(337.5)# Posisicones en Y iguales para todos los planetas
    Objectxvel.append(0)#Velocidad inicial en x =0 para todos los planetas                
    Objectyvel.append(0.12)# Velocidad incial en y=0.12 
    ObjectMass.append(i)#Define las masas de los planetas
    ObjectR.append(i)# Define los radios de cada planeta

for k in range(7000):#Se crea una istancia de 7000 iteraciones para llenar el vector V y Energias ver la velocidad de la tierra
    V.append(k)
    E_k.append(i)
    E_p.append(i)
    E_T.append(i)
    
canvas=Canvas(root, bg="black")# Se crea el 'Canvas' con sus caracteristicas
canvas.pack(fill="both", expand=True)
Planetas,Vectors=[],[]
G = 6.67428e-11# Se define la contante de gravitacion universal
Color=["grey","orange","cyan","red","red","brown","blue","blue","white"]# Colores de los planetas
Time=np.arange(0,7000,1)# Vector de tiempo de 7000 unidades para ver la velocidad V
while True:# Se crea un bucle infinito
    SolY, SolX = 337.5,762.5
    
    canvas.delete("all")# si se quiere ver la orbita planetaria comentaree esta linea 8 no s evrea la grafica de V
    cont=cont+1# El conatdor aumenta de forma entera en cada iteracion
    
    for Num in range(len(Objectx)):#Recorre todos los planetas : 9
        angle = math.atan2(SolY-Objecty[Num], SolX -Objectx[Num])#Se halla en angulo que hay entre la posicion del sol y el planeta
        distance = math.sqrt( ((SolX-Objectx[Num])**2) + ((SolY-Objecty[Num])**2) )
        Objectxvel[Num] += math.cos(angle) * G * ObjectMass[Num] * MasaSol / (distance ** 2)
        Objectyvel[Num] += math.sin(angle) * G * ObjectMass[Num] * MasaSol / (distance ** 2)
        Objectx[Num] += Objectxvel[Num] 
        Objecty[Num] += Objectyvel[Num]
        if distance < 20: # Se definen instancias para aumnetar o decrecer la veocidad dependiendo la distancia
            if distance < 15:
                Objectx[Num] -= Objectxvel[Num] * 1.5
                Objecty[Num] -= Objectyvel[Num] * 1.5
                Objectxvel[Num] = 0
                Objectyvel[Num] = 0
            else:
                Objectx[Num] -= Objectxvel[Num] * 1.01
                Objecty[Num] -= Objectyvel[Num] * 1.01
                Objectxvel[Num] = 0
                Objectyvel[Num] = 0         

        for Num2 in range(len(Objectx)):# Se crea lo mismo dentro del for principal para que a cada iteracion se haga simultaneo 
            # la evaluacion de velocidad para todos los planetas
            angle = math.atan2(     Objectx[Num]-Objecty[Num2], Objecty[Num]-Objectx[Num2]  )
            distance = math.sqrt( ((Objectx[Num]-Objectx[Num2])**2) + ((Objecty[Num]-Objecty[Num2])**2) )
            try:
                Objectxvel[Num] += math.cos(angle) * G * ObjectMass[Num] * ObjectMass[Num2] / (distance ** 2)
                Objectyvel[Num] += math.sin(angle) * G * ObjectMass[Num] * ObjectMass[Num2] / (distance ** 2)
            except:
                pass
            Objectx[Num] += Objectxvel[Num] 
            Objecty[Num] += Objectyvel[Num]
            if distance < 20 and distance > 0:
                try:
                    Objectx[Num] -= Objectxvel
                    Objecty[Num] -= Objectyvel
                except:
                    pass
        if cont < 7000: #Si Aun no hay datos suficientes halle el modulo con Vx y Vy y guardelo
            V[cont]=((Objectxvel[3])**2+(Objectyvel[3])**2)**0.5  
            E_k[cont]=(1400*(V[cont])**2)/2
            if distance>0:
                E_p[cont]=-(G*1400*MasaSol)/distance
                E_T[cont]=E_p[cont]+E_k[cont]
        if cont == 7000:# Si el contador llega a 7000 interacion del bucle infinito grafica ( hay datos suficientes )
            #SE HACEN LAS GRAFICAS DE V, E_k, E_p y E_T
             plt.plot(V)
             plt.title('Velocidad tierra')
             plt.ylabel('m/s')
             plt.xlabel('Iteraciones')
             plt.show()
             plt.plot(E_k)
             plt.title('Energia cinetica')
             plt.ylabel('Joules')
             plt.xlabel('Iteraciones')
             plt.show()
             plt.plot(E_p)
             plt.title('Energia potencial')
             plt.ylabel('Joules')
             plt.xlabel('Iteraciones')
             plt.show()             
             plt.plot(E_T)
             plt.title('Energia total')
             plt.ylabel('Joules')
             plt.xlabel('Iteraciones')
             plt.show() 
             
        sc = 100 # Escala para el "vector velocidad"
        #Dentro del for cada itracion elimina todo del canvas, por lo que en cada iteracion crea todo de nuevo
        #pero con los nuevos parametros de posicion y velociad
        x, y, r, vx, vy = Objectx[Num], Objecty[Num], ObjectR[Num]//2, Objectxvel[Num], Objectyvel[Num] 
        canvas.create_oval(x+r, y+r, x-r, y-r, fill=Color[Num], width=0)# Crea el planeta
        canvas.create_line(x, y, x+sc*vx, y+sc*vy, arrow=LAST)# Genera el vetor velocidad del planeta
        
    oval1=canvas.create_oval(800, 300, 725, 375, fill="yellow", width=0)# Crea el Sol fuera del ciclo For
    root.update()#Actualiza el mundo

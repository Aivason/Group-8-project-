"""
Group 8 project Assignment
Contributors:
PUT YOUR NAME HERE.
"""

##This is a programme for pH calculations and its titration plot.

####

import math
import tkinter
from tkinter import *

while True:
    print('Acid or Base ? Put your input as acid, or base')
    acba=input()
    print('Strong or Weak ? Put your input as strong or weak')
    strength=input()
    print('Prvide the volume of solution in ml')
    svol=(float(input()))/1000
    print('Provide the molarity')
    mol=float(eval(input()))
    if strength=="weak":
        if acba=="acid":
            print('Provide the Ka Value.')
        if acba=="base":
            print('Provide the is the Kb Value.')
        kval=(input())
        kval=eval(kval)
    if acba=="acid":
        print('Provide the added volume for strong base in ml')
    else:
        print('Provide the added volume for strong base in ml')
    vol2=input()
    vol2=float(vol2)/1000
    print("what is the Molarity of the titrating solution?")
    mol2=input()
    mol2=float(mol2)
    pointlist=[]
    therange=svol*2
    truevol=vol2
    test=truevol
    vol2=0
    xcoord=[]
    ycoord=[]
    while vol2<therange:
        if True:
            
####            
            if strength=="strong":
                comparemole=(((svol)*mol) - (((vol2)*mol2)))
                if comparemole==(svol*mol):
                    a=0
                    pH=-math.log(mol,10)
                    
                elif comparemole==0:
                    pH=7
                if comparemole<0:
                    OHcon=(-1*comparemole)/((vol2+svol))
                    #print(OHcon)
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                elif comparemole>0:
                    Hcon=comparemole/((vol2+svol))
                    pH=-math.log(Hcon,10)
                
####                
            if strength=="weak":
                comparemole=(((svol)*mol) - (((vol2)*mol2)))
                
                if comparemole==(svol*mol):
                    Hcon=(kval*mol)**0.5
                    pH=-math.log(Hcon,10)
                elif comparemole==0:
                    cbasecon=(svol*mol)/(svol+vol2)
                    Kb=(10**-14)/kval
                    OHcon=(Kb*cbasecon)**0.5
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                elif comparemole>0:
                    molX=(vol2*mol2)
                    molHX=(svol*mol)-(vol2*mol2)
                    Xcon=molX/(svol+vol2)
                    HXcon=molHX/(svol+vol2)
                    Hcon=kval*HXcon/Xcon
                    pH=-math.log(Hcon,10)
                elif comparemole<0:
                    molX=(svol*mol)
                    molOH=(vol2*mol2)-(molX)
                    OHcon=molOH/(svol+vol2)
                    pOH=-math.log(OHcon,10)
                    pH=14-pOH
                    
        if comparemole==0:
            ex=vol2
            ey=pH
        if acba=="base":
            pH=14-pH
        xcoord.append(vol2)
        ycoord.append(pH)
        if vol2==(test):
            print("pH=",pH)
        vol2=vol2+(0.05/1000)
        vol2=round(vol2,5)

###
    graph_window=Tk()
    graph_window.configure(background='#00B88A')
    graph_window.title("Graph")
    graph_window.geometry('600x680+210+35')
    graph_window.resizable(width=FALSE, height=FALSE)
    canvus_1 = Canvas(graph_window,height=600,width=600,bg='white')

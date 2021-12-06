"""
Group 8 project Assignment
Contributors:
PUT YOUR NAME HERE.
"""

##This is a programme for pH calculations and its titration plot.

weakacids = {'Oxalic Acid': 1.27,'Sulfurous Acid': 1.85,'Phosphoric Acid':2.16,
             'Nitrous Acid': 3.25,'Hydrofluoric Acid':3.20,'Methanoic Acid':3.75,
             'Benzoic Acid':4.204 ,'Acetic Acid':4.75,'Formic Acid':3.75
             }
#dictionary of weakacids and their pka values

weakacidslist = list(weakacids.keys())
for c in range(len(weakacidslist)):
    print(c+1,':',weakacidslist[c])

#prints a list of all weakacids for user to choose from

strongacids = {'Hydrochloric Acid':'-6.3','Nitric Acid':'-1.5','Sulfuric Acid':'-3', 
               'Hydrobromic Acid': '-8.7','Hydroiodic Acid':'-9.3',
               'Perchloric Acid':'-8','Chloric Acid': '1.0'
                  }
#dict of strong acids and their pka values
#sulfuric acid is first dissociation

strongacidslist = list(strongacids.keys())
for c in range(len(strongacidslist)):
    print(c+10,':',strongacidslist[c])
#prints a list of all strong acids for user to choose from

acidnum = int(input('What acid would you like to use? (enter the number beside the acid): '))
try:
    if acidnum>10:
        acidindex = (acidnum-10)
        acid = strongacidslist[acidindex]
        print(acid)
    else:
        acid = weakacidslist[acidnum-1]
        print(acid)
except:
    print('Error! Please enter a number between 1 and 16!')

#asks user for input number
#tells user to trpe another number if its out of range
#if in range, prints acid. Able to use acid variable for calculations and recieve the pka from the dictionary



####

import math


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


###This is a test
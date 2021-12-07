###############################################################################
import helps
import math 

print("If you would like to see a load of definitions that are essetial\n"
      "to your understanding type ' i(b) ' to see a list of definitions\n"
      "into an empty console input")

dvi= int(input("enter ' 1 ' for pH calculator: strong acid vs strong base \n"
           "enter ' 2 ' for pH calculator: strong acid vs weak acid .etc \n"
           ":"))

if dvi == 1:


# user enters values for moles of the base and acid,
# and those values are stored in basemol and acidmol
    
    
    
    
    print(" This is the pH calculator strong acid vs strong base ")
    basemol= float(input("enter moles of your strong base : "))
    acidmol= float(input("enter moles of your strong acid : "))

# user enters values for moles of the base and acid,
# and those values are stored in basev and acidv

    basev= float(input("enter volume of your base: "))
    acidv= float(input("enter volume of your acid: "))

# Here if the moles of the base " basemol " is larger than moles of the acid
# " acidmol " it will subtract acidmol from base mole, to get the final moles
# of the base " basemol2 "
# next it it adds the volume of base and acid together (total volume).
# final moles of base is divided the total volume to get the concentration(basec)
# get the pOH by -logging the conc to the base of 10
# finally subtracting poH from pKW to get the pH, printing the answer to 5 decimal spaces

    if basemol>acidmol:
        basemol2= basemol-acidmol
        basec= basemol2/(basev + acidv)
        basePOH= (-math.log(basec, 10))
        PH1= 14-basePOH
        print("This is the pH of your final solution: ", "{:.5f}".format(PH1))
    
# The same as the one above except its for the acid and there's no subtracting
# from pKW   
    
    else:
        acidmol2= acidmol-basemol
        acidc= acidmol2/acidv
        acidPH= (-math.log(acidc, 10))
        print("This is the pH of your final solution: ", "{:.5f}".format(acidPH))
        print("If you would like to see a load of definitions that are essetial\n"
              "to your understanding type ' i(b) ' to see a list of definitions")
        
    
    
if dvi == 2:  
    
    print("This is the pH calculator strong acid vs weak acid .etc ")
    tri=int(input("enter ' 1 ' for stong acid vs weak base\n"
              "enter ' 2 ' fro strong base vs weak acid"
              ": "))
    
    if tri == 1:
        
        #so far only works when the moles of the weak base is larger than 
        # the moles of the stong acid 
        
        wbasemol= float(input("enter the moles of the weak base: "))
        sacidmol= float(input("enter the moles of the strong acid: "))
        pKa= float(input("enter the pKa of the weak base: "))
        
        # im not explaining this mess to anyone
        
        if wbasemol > sacidmol:
            conacid= sacidmol
            wbasemol2= wbasemol - sacidmol
            wc= wbasemol2 / conacid
            logwc= math.log(wc, 10)
            pH= pKa + logwc
            print("This is the pH of your final solution: ", "{:.5f}".format(pH))
 




###############################################################################    
###
###
###
#Titration curve programme



import math


while True:
    print('Acid or Base ? Put your input as acid, or base')
    acba=input()
    print('Strong or Weak ? Put your input as strong or weak')
    strength=input()
    print('Provide the volume of solution in ml')
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



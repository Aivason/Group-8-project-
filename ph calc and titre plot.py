###############################################################################
"""defines the essentials 
"""

acid= "-An acid is a proton donor."

base= "-A base is a proton acceptor." 

ph= "-pH = -log10[H^+]."

stongacid= "-A strong acid is one which completely dissociates in aqueous solution."

weakacid= "-A weak acid is one which partially dissociates in aqeuous solution."

conjugate_acid_base_pair= "-A conjugate acid base pair has its base and its conjugate acid\n or an acid and its conugate base."

Ka= "-Ka is how readily the acid dissociates. (high Ka= high pH)"

b=[acid, base, ph, stongacid, weakacid, conjugate_acid_base_pair, Ka]

def i(n):
    for b in n:
        print(b)

#
#
#

'''the ph calc'''
        
import math 

print('Please type 1 for ph calculation , 2 for titration solution ')
useranswer=int(input())
if useranswer==1:

    print('Welcome to the pH calculator!')
    print('-----------------------------')
    
    print("If you would like to see a load of definitions that are essetial\n"
          "to your understanding type ' i(b) ' to see a list of definitions\n"
          "into an empty console input")
    
    dvi= int(input("Enter ' 1 ' for pH calculator: strong acid vs strong base \n"
               "Enter ' 2 ' for pH calculator: strong acid vs weak acid .etc \n"
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
#                         line 97-134 is chris's part        
        print("This is the pH calculator strong acid vs weak acid .etc ")
        e=input('Is the excess reactant the acid or the base? ')
        s=input('Is it strong or weak? ')
        if s=='strong':
            m=float(input('From the chemical equation, how many molecules of the excess? '))
            c=float(input('What is the concentration of the acid in molar? '))
            v=float(input('What is the volume in mL? '))
            n=c*(v/1000)
            C=float(input('What is the concentration of the base in molar? '))
            V=float(input('What is the volume of the base in mL? '))
            N=C*(V/1000)
            if e=='acid':
                a=math.log((n-(N*m))/((v+V)/1000),(10))*-1
                print('pH =' ,a)
            elif e=='base':
                a=14-math.log((N-(n*m))/((v+V)/1000),(10))*-1
                print('pH =' ,a)
    
        elif s=='weak':  
    
            q=input('Do you know the concentration of the excess? (y/n) ')
            if q=='n':
                m=float(input('What is the mass of the excess in g? '))
                M=float(input('What is the gram formula mass? '))
                n=m/M
                v=float(input('What is the volume in mL? '))
                c=n/v
            elif q=='y':
                c=float(input('What is the concentration in molar? '))
    
            if e=='acid':
                K=float(input('What is the pKa?'))
                a=-1*math.log(math.sqrt((10**-K)*c),(10))
                print('pH =' ,a)
            elif e=='base':
                K=float(input('What is the pKb?'))
                a=14-math.log(math.sqrt((10**-K*c)),(10)*-1)
                print('pH =' ,a)
 


#Titration curve programme

else:
    import math
    import tkinter
    from tkinter import *
#Receive necessary inputs from the user.
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
                print('Provide the Ka Value.','in the format of 6.6*10**-6')
            if acba=="base":
                print('Provide the Kb Value.','in the format of 6.6*10**-6')
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
        therange=svol*2
        truevol=vol2
        test=truevol
        vol2=0
        while vol2<therange:
            if True:
                
    #### Strong acid - Strong base titrating            
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
                    
    #### Weak acid - Strong base titrating                
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
                pH=14-pOH
            if vol2==(test):
                print('pH=',pH)
            vol2=vol2+(0.05/1000)
            vol2=round(vol2,5)

#Plotting titration curve -> need to be improved.
        root=Tk()
        root.configure(background='#00B88A')
        root.title("Graph")
        root.geometry('600x680+210+35')
        root.resizable(width=FALSE, height=FALSE)
        canvus_1 = Canvas(root,height=600,width=600,bg='white')
        root.mainloop()

# idiek sau kaskaip:
# klase ir objektu ir biblioteka
# failus ir funkcias
# zodyna ir sprendimus
# sarasa ir kilpos

###############################################################################

import math 

dvi= int(input("enter ' 1 ' for pH calculator: strong acid vs strong base \n"
           "enter ' 2 ' for pH calculator: strong acid vs weak acid .etc"
           ))

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
    



    
###############################################################################    
    
if dvi == 2:  
    
    print("This is the pH calculator strong acid vs weak acid .etc ")
    

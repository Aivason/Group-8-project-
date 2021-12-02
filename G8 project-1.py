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

#get inputs from user

print('Acid or Base ? Put your input as acid, or base')
acba=input()
print('Strong or Weak ? Put your input as strong or weak')
strength=input()
print('Prvide the volume of solution in Litre')
svol=float(input())/1000
print('Provide the molarity')
mol=float(input())
if strength == "weak":
    if acba == "acid":
        print('Provide tthe Ka Value.')
    if acba == "base":
        print('Provide the Kb value.')
    valuek=input()
if acba =="acid":
    print('Provide the added volume for strong base in Litre')
else:
    print('Provide the added volume for strong acid in Litre')
vol=float(input())/1000
print('Provide the molarity of the titrating solution')
tmol=float(input())

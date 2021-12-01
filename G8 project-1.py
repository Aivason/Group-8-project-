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



import pylab


####

##example of the programme of the titration curve
##titration of 100ml of 2M hcl with 1M NaOH

a1,b1,a2=2,0.1,1
c,b2=a1*b1,a1*b1/a2

n,eps=50,1.e-10
db = b2/n

bs1=pylab.linspace(db,b2,n)
bs2=pylab.linspace(b2,2*b2,n)

as1=-pylab.log10((c-a2*bs1+eps)/(b1+bs2))
as2=14+pylab.log10((a2*bs2-c+eps)/(b1+bs2))

pylab.plot(bs1,as1,color='r')
pylab.plot([bs1[-1],bs2[1]],[as1[-1],as2[1]],color='r')
pylab.plot(bs2[1:],as2[1:],color='r')

pylab.title('titration curve')
pylab.xlabel('vol of naoh added')
pylab.ylabel('pH')
pylab.grid()

pylab.show()

##I tried to commit it locally

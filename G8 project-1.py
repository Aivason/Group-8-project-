"""
Group 8 project Assignment
Contributors:
PUT YOUR NAME HERE.
"""

##This is a programme for pH calculations and its titration plot.
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
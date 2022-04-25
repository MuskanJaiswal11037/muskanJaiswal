import numpy as np
import matplotlib.pyplot as plt
#The given function is to check whether the roots provided by user satisfies the equation 4x*x-5x-3 or not.
def ret(a):
   #The steps given below are to find the roots of the given equation upto 2 decimal places.
    P=[4,-5,-3]
    [t,p]=np.roots(P)
    t1="{:.2f}".format(t)
    p1="{:.2f}".format(p)
    z=0
    
    if(float(a)==float(t1) or float(a)==float(p1)):
       return 0
     else:
         return 1
a=input(" Enter the root of the given equation upto two decimal places")
b=input(" Enter another root of the equation upto two decimal places")

if(ret(a)==0 and ret(b)==0):
   print("Both are the roots of the given equation ")
else
   print("Both are not roots of the given equation ") 

#The code provided below is to plot the graph of the given function


plt.annotate("x1=(1.69,0)",(t1,z))
plt.annotate("x2=(-0.44,0)",(p1,z),(-0.5,0))
x=np.linspace(-2,2.05,20)
y=4*x*x-5*x-3
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter([p1,t1],[z,z])
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.show()
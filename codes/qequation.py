import math
#The given function is to check whether the roots provided by user satisfies the equation 4x*x-5x-3 or not.
def ret(a):
    #The steps given below are to find the roots of the given equation upto 2 decimal places.
    t=float((5+math.sqrt(73))/8)
    p=float((5-math.sqrt(73))/8)
    t1=int(t*100+0.5)
    p1=int(p*100-0.5)
    p=float(p1/100)
    t=float(t1/100)
    if(float(a)==t or float(a)==p):
        return 0
     else:
         return 1
a=input(" Enter the root of the given equation")
b=input(" Enter another root of the equation")

if(ret(a)==0 and ret(b)==0):
   print("Both are the roots of the given equation")
else:
    print("Both are not roots of the given equation") 
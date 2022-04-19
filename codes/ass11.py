import numpy as np
import matplotlib.pyplot as plt


plt.annotate("x1=(1.69,0)",(1.69,0))
plt.annotate("x2=(-0.44,0)",(-0.44,0),(-0.5,0))
x=np.linspace(-2,2.05,20)
y=4*x*x-5*x-3
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.scattre([-0.44,1.69],[0,0])
plt.axhline(0,color='black')
plt.axvhline(0,color='black')
plt.show()
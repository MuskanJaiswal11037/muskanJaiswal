import matplotlib.pyplot as plt

plt.annotate("x1=(1.69,0)",(1.69.0))
plt.annotate("x2=(-0.44,0)",(-0.44,0),(-0.5,0))

x=[-0.44,0,0.2,0.25,0.4,0.5,0.6,0.75,0.8,1,1.2,1.25,1.5,1.6,1.69,1.75,2.00]
y=[0,-3,-3.84,-4,-4.36,-4.15,-4.56,-4.5,-4.44,-4,-3.24,-3,-1.5,-0.76,0,0.53]
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter([-0.44,1.69],[0,0])
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.show()
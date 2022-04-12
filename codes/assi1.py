import matplotlib.pyplot as plt
plt.annotate("x1=(1.69,0)",(1.69,0))
plt.annotate("x2=(-0.44,0)",(-0.44,0))

x=[-0.44,0,0.25,0.5,0.75,1,1.25,1.5,2]

y=[0,-3,-4,-4.5,-4,-3,-1.5,3]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.scatter([-0.44,1.69],[0,0])
plt.show()
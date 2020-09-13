#%matplotlib inline

from matplotlib import pyplot as plt
import numpy as np
import math 

#QUESTION 1(a)

y = [] #  empty list
       

x = np.linspace(-1,2,30) # linspace gives a vector of elements
                      
for i in range(0,30):
    if x[i] < -1:
        y.append(0) #here append add '0' to the end of a list 
    elif -1 <= x[i] <= 2:
        a = (4/15)*(x[i])**3
        y.append(a) #here append add 'a' to the end of a list 
    elif x[i] > 2:
        y.append(0) 
        
plt.plot(x,y, "r")        
plt.title("graph for part (a)")
plt.ylabel("f(u)")
plt.xlabel("u")
plt.grid()

plt.show()

#QUESTION 1(b)
y = []

t = np.linspace(0,3/2,100)

for i in range(0,100):
    if t[i] < 0 or (1/2) < t[i] < 1 or t[i] > 3/2:
        y.append(0)
    else:
        y.append(1)

plt.plot(t,y)
plt.title("graph for part (b)")
plt.ylabel("f(u)")
plt.xlabel("u")
#plt.grid()

plt.show()

# QUESTION 1(c)

y = []

t = np.linspace(0,math.pi/2,100)

for i in range(0,100):
    a = t[i]*(math.sin(t[i]))
    y.append(a)

plt.plot(t,y,'g')

#plt.grid()
plt.title("graph for part (c)")
plt.ylabel("f(u)")
plt.xlabel("u")
plt.show()

# QUESTION 1(d)

y = []

t = np.linspace(-1,1,100)

#for i in range(0,100):
    #a = abs(t[i])
    #y.append(a)
y = abs(t)

plt.plot(t,y,'b')
plt.title("plot for part (d) ")

		
plt.ylabel("f(u)")
plt.xlabel("u")
plt.show()



#QUESTION 8(b)

y = [] 
       

x = np.linspace(-1,2,30) 
                      
for i in range(0,30):
    if x[i] < -1:
        y.append(0) 
    elif -1 <= x[i] <= 2:
        a = ((x[i]+1)**2)/9
        y.append(a) 
    elif x[i] > 2:
        y.append(0) 
        
plt.plot(x,y, "r")        
plt.title("graph for part 8 (b)")
plt.ylabel("F(x)")
plt.xlabel("x")
plt.grid()

plt.show()

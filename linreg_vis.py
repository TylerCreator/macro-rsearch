# import matplotlib.pyplot as plt
# import numpy as np

f = open("data1.txt",'r')
x=[]
y=[]
e=[]
for line in f:
    t = line.split(' ')
    x.append(float(t[0]))
    y.append(float(t[1]))
print(x)
print(y)

# plt.scatter(x,y)
# plt.show()
# length = len(x)
# def jfun(c0, c1):
#     sum = 0    
#     for i in range(length):
#         sum+=(c0 + c1*x[i] - y[i])**2
#     return (sum/(2*length))

# def derivative(_c0, _c1):
#     c0 = 0
#     c1 = 0
#     for i in range(length):
#         c0 = c0 + (_c0 + _c1*x[i] - y[i])
#         c1 = c1 + (_c0 + _c1*x[i] - y[i])*x[i]
#     c0 = c0/length
#     c1 = c1/length
#     return [c0, c1]
# a = 0.01
# c0=0
# c1=1
# J0 = jfun(c0, c1)
# J1=J0-1
# c=0
# while J0-J1>0.000001:
#     d = derivative(c0,c1)
#     d0 = d[0]
#     d1 = d[1]
#     c0 = c0 - a*d0
#     c1 = c1 - a*d1
#     J0 = J1
#     J1 = jfun(c0, c1)  
#     c=c+1
#     e.append(J1)
# print(c1,c0)    
# y1=[]
# for i in range(length):
#     y1.append(c0+c1*x[i])
# plt.plot(x,y1,'r')
# plt.scatter(x,y1, color='r')
# plt.scatter(x,y, color='g')
# plt.show()
# plt.plot(e, 'r')
# plt.show()
import numpy as np
n=int(input("Enter number of elements"))
l=[]
for i in range(0,n):
    l.append(int(input("Enter value")))
a=np.array(l)
print(a[::-1])
print (a)
#1D array
c=np.array([1,3,4,5])
print("####1D####")
print()
print(c*2)

#2d array
a=np.array(([1,2,3],[4,5,6],[1,2,3]))
b=np.array(([1,2,3],[4,5,6],[1,2,3]))
d=np.zeros([3,3],dtype=int)
s=0
for i in range(0,len(a)):
    for j in range(0,len(b[0])):
        for k in range(0,len(d)):
            d[i][j]=d[i][j]+(a[i][k]*b[k][j])
print()
print()
print("####2D####")
print()
print(a)
print("-------")
print(b)
print("-------a.b-------")
print(d)#matrix multiplication
print("------a@b------")
print(a@b)











            

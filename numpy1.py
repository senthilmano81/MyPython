import numpy as np
a = [1,2,3.4,'a',5]
print(a*3)
b = np.array(a)
print(a)
print(b)

print(np.ones(5))
print(np.zeros(6))
print(np.empty(7))
print(np.full(5,'a'))

a = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(a)
print(b)
b[2][2] = 10 
print(b)


a = np.array([1,2,3,4,5])
a = a * 4
print(a)
a = [1,2,3,4,5]
print(a)
print(max(a))
print(min(a))
print(sum(a))

a = np.array([1,2,3,4,5])
bool_ar = a > 2; 
print(bool_ar)
new_ar = a[bool_ar]
print(new_ar)
print(np.where(a>2))



a = np.array([1,2,0,0,4,0])
ind = np.where(a>0)
print(*ind[0])


arr1 = np.arange(1,21,2)
print(arr1)
ind = np.where(arr1%3==0)
print(*ind[0])


arr1 = np.arange(1,11)
arr1[(arr1>=3) & (arr1<=8)] = -1*arr1[(arr1>=3) & (arr1<=8)]
print(len(arr1))
print(*arr1)



age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])
ind = np.where(height>155)

for i in range(len(ind[0])): 
    print(age[ind[0][i]],height[ind[0][i]])
    
arr1 = np.arange(21,1,-1)
arr1 = arr1.reshape(4,5)
print(arr1)
arr2 = arr1[arr1[:,1].argsort()]
print(arr2)
arr1 = [[1,2],[3,4],[5,6]]
arr1 = np.array(arr1)
print(arr1)
arr1.resize(2,2)
print(arr1)

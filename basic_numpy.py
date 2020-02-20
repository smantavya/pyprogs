import numpy as np

# print(np)
# print(dir(np))

t = [1,2,3,4,5]
# print(t)
# print(type(t))

# convert into array
q = np.array(t)
# print(q)
# print(type(q))

# print(q.ndim)
# print(q.shape)
# print(q.sum())
# print(q.max())
# print(q.min())
# print(q.size)

# for multi dimensinal use two square brackets [[],[]]

s = [6,7,8,9,10]
o = np.array([t,s])
# print(o)
# print(o.ndim)

# we cant use range function for float steps

# range(2,10,1.5) is wrong

# t = np.arange(10,100,7.5)
# print(t)

t = np.linspace(10,100)

r = o.reshape((5,2))
# print('r= ',r)
# print('o =',o)
o.resize((10,1))
# print('o =',o)
# print(o.T)

print(np.zeros((5,5)))

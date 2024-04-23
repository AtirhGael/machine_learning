import numpy as np  

# accessing /changing elements in an array
a = np.array([[1,2,3],[2,3,3],[2,4,6],[8,7,9],[9,1,2]])
b = a[:,1]
# print(b)

# initializing different types of arrays
print(np.zeros((2,4)))

# random decimal  numbers
random = np.random.rand(4,4)
print("random array",random)

# random interger numbers
randInt = np.random.randint(7,size=(3,5))

print('rand int',randInt)
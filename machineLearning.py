import numpy as np 
from scipy import sparse
import matplotlib.pyplot as plt 

x = np.linspace(-10,10,100)
y = np.sin(x)
graph =  plt.plot(x,y)

eye = np.eye(4)
sparse_matrics = sparse.csr_matrix(eye)
# x  = np.array([[1,2,1,2],[4,5,6,2]])
# print(graph)

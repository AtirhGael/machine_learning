#%%
import numpy as np 
from scipy import sparse
import matplotlib.pyplot as plt 
import pandas as pd

x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y,marker= "x")

eye = np.eye(4)
sparse_matrics = sparse.csr_matrix(eye)
# x  = np.array([[1,2,1,2],[4,5,6,2]])
# print(graph)

# %%
import pandas as pd
data = {'name':["john",'ana','gael','marry'],
        'location':['bamenda','cameroon','douala','yaounde'],
         'age':[12,21,23,30] }
data_pandas=pd.DataFrame(data)
print(data_pandas.age>20)


# %%
from sklearn.datasets import load_iris

data  = load_iris()
print(data['target_names'])

# %%

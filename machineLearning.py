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
from sklearn.model_selection import train_test_split
import pandas as pd

iris_data  = load_iris()
X_train, X_test,y_train,y_test = train_test_split(iris_data['data'],iris_data['target'],random_state=0)
# print(y_train.shape)
iris_dataframe = pd.DataFrame(X_train,columns=iris_data.feature_names)
print(iris_dataframe)
grr = pd.scatter_matrix(iris_data,c=y_train, figsize=(15,15),marker='0', hist_kwds={'bin':20},s=60,alpha=8,cmap=mglearn.cm3)

# %%

#%%
import mglearn.datasets
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
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import mglearn
import numpy as np

knn = KNeighborsClassifier(n_neighbors=2)

iris_data  = load_iris()
X_train, X_test,y_train,y_test = train_test_split(iris_data['data'],iris_data['target'],random_state=0)
# print(y_train.shape)
iris_dataframe = pd.DataFrame(X_train,columns=iris_data.feature_names)
# print(iris_dataframe)
# grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train, figsize=(15,15),marker='x', hist_kwds={'bins':20},s=60,alpha=8,cmap=mglearn.cm3)
# print(grr)

knn.fit(X_train,y_train) # build the model using the fit method of the K_neighbor
X_new = np.array([[5,2.9,1,0.2]])

prediction = knn.predict(X_new)
# print(iris_data['target_names'][prediction])
y_prediction = knn.predict(X_test)
print(knn.score(X_test,y_test)) # we evaluate the method by calling the score method

# %%
import mglearn
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier


mglearn.plots.plot_knn_classification(n_neighbors=5)

# x,y = mglearn.datasets.make_forge()

# mglearn.discrete_scatter(x[:,0],x[:,1],y)
# plt.legend(["Class 0", "Class 1"], loc=4)
# plt.xlabel("First feature")
plt.ylabel("Second feature")
# print("X.shape: {}".format(x.shape))



# %%
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=3)

X_train,y_train,X_test,y_test = train_test_split(x,y, random_state=0)

clf.fit(X_train,y_train)
print(clf.predict(X_test))



# %%

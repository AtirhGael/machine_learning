from  sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

iris  = datasets.load_iris()

x= iris.data
y = iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

classes = ['Iris Setosa','Iris Versicolour','Iris Virginica']

model = svm.SVC()
model.fit(x_train,y_train)
 
print(model)
prediction = model.predict(x_test)
acc = accuracy_score(y_test,prediction)

print('predictions',prediction)
print('accuracy',acc)

# env\Scripts\activate
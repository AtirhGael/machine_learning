from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


x_train,x_test,y_train,y_test = train_test_split()
# data = load_breast_cancer()
# data = load_breast_cancer(data.data,data.target,test_size=0.33)
print(x_train,x_test,y_train,y_test )
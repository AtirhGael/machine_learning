import tensorflow as tf 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load in the data 
data = pd.read_csv('moore.csv',header=None).to_numpy()
# print(data)
x = data[:,0].reshape(-1,1) # making an N x D matrics 
y = data[:,1]
#plot the data
plt.scatter(x,y)
# the log of an exponential is simple the original thing 
y = np.log(y)
plot =  plt.scatter(x,y)
print(plot)
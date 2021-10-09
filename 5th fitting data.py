import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pd.read_csv('vel_data.csv')
x=data['Time (years)']
y=data[' Observed Velocity (cm/s)']
def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))

    return (B0, B1, reg_line)

N = len(x)
x_mean = x.mean()
y_mean = y.mean()

B1_num = ((x - x_mean) * (y - y_mean)).sum()
B1_den = ((x - x_mean)**2).sum()
B1 = B1_num / B1_den

B0 = y_mean - (B1 * x_mean)
print(B0,B1)
plt.scatter(x,y,s=0.5)
plt.title('Radial velocity of a star with respect '
          'to galactic center over years')
plt.xlabel('TIME in years')
plt.ylabel('RADIAL VELOCITY(cm/s)')
plt.plot(x,B0+B1*x,color="red",linewidth=2)
plt.show()

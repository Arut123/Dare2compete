import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data=pd.read_csv('acc_data.csv')
x=data['Range']
y=data['Probability']

plt.xlabel("Acceleration(cm^-1 year^-1")
plt.ylabel("No. of stars")
plt.title("ACCELERATIONS OF MULTIPLE STARS")
plt.plot(x,y,color='green',linewidth=0.75)
plt.show()
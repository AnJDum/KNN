import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
p1 = pd.read_csv("./data/predict_4.csv", index_col=False)
# p2 = pd.read_csv("./data/predict_4.csv", index_col=False)
p1.sort_values(by="Predict", inplace=True, ascending=True)
p1.index = range(len(p1))

x, y, z = p1['Sepal.Length'], p1['Sepal.Width'], p1['Petal.Length']
ax = plt.subplot(111, projection='3d')
ax.scatter(p1.iloc[0:17, 0], p1.iloc[0:17, 1], p1.iloc[0:17, 2], c='darkslategrey', s=60, label='setosa')
ax.scatter(p1.iloc[18:34, 0], p1.iloc[18:34, 1], p1.iloc[18:34, 2], s=60, c='palevioletred', label='versicolor')
ax.scatter(p1.iloc[35:44, 0], p1.iloc[35:44, 1], p1.iloc[35:44, 2], s=60, c='navy', label='virginica')
plt.legend(loc='upper right')
ax.set_zlabel('Petal.Length')
ax.set_ylabel('Sepal.Width')
ax.set_xlabel('Sepal.Length')
plt.show()

a = 1
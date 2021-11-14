import pandas as pd
import random
iris = pd.read_csv("./data/iris.csv", index_col=False)
train_list = random.sample(range(1, 150), 105)
train = iris[iris['index'].isin(train_list)]
train.drop('index', axis=1, inplace=True)
train.index = range(len(train))
predict = iris[~ iris['index'].isin(train_list)]
predict.drop('index', axis=1, inplace=True)
predict.index = range(len(predict))
predict.loc[predict['Species'] == 'setosa', 'Species'] = 1
predict.loc[predict['Species'] == 'versicolor', 'Species'] = 2
predict.loc[predict['Species'] == 'virginica', 'Species'] = 3

train.loc[train['Species'] == 'setosa', 'Species'] = 1
train.loc[train['Species'] == 'versicolor', 'Species'] = 2
train.loc[train['Species'] == 'virginica', 'Species'] = 3
predict.to_csv('./data/predict.csv', sep=',', index=None, header=None)
train.to_csv('./data/train.csv', sep=',', index=None, header=None)

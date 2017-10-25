import pandas as pd
import numpy as np
from sklearn import cross_validation
from sklearn import avm
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('customers.csv',sep=',',header=None)
df = df.iloc[np.random.permutation(len(df))]
X = df[df.columns[:-1]].values
Y = df[df.columns[-1]].values

cv = 10
print 'linear regression'
lr = LinearRegression()
scores = cross_validation.cross_val_score(lr, X, Y, cv = cv)
print("mean R2: %-.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))
pred = cross_validation.cross_val_predict(lr, X, Y, cv = cv )
print 'error: ", mean_squared_error(Y, pred)

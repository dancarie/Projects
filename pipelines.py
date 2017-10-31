import os
import pandas as pd
import requests
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.svm import LinearSVC

PATH = r'/Users/danka/Projects/datatrfrm'
r =
requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iri
s/iris.data')
with open(PATH + 'iris.data', 'w') as f:
 f.write(r.text)
os.chdir(PATH)
df = pd.read_csv(PATH + 'iris.data', names=['sepal length', 'sepal width',
'petal length', 'petal width', 'class'])

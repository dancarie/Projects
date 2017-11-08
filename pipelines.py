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
import requests
r = requests.get(r"https://api.github.com/users/acombs/starred")
r.json()
plt.style.use('ggplot')

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import
DesiredCapabilities
   from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
%matplotlib inline
Next, we'll set up the code to instantiate the browser object. It is this object that will pull
down the page for us. You can select the airports or regions that you'd like by running a
search in your browser and copying the URL. Here, I'm searching for trips between New
York airports and several cities in Asia:
url =
"https://www.google.com/flights/explore/#explore;f=JFK,EWR,LGA;t=
HND,NRT,TPE,HKG,KIX;s=1;li=8;lx=12;d=2016-04-01"
driver = webdriver.PhantomJS()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0
(Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/46.0.2490.80 Safari/537.36")
driver = webdriver.PhantomJS(desired_capabilities=dcap,
service_args=['--ignore-ssl-errors=true'])
driver.implicitly_wait(20)
driver.get(url)          
driver.save_screenshot(r'flight_explorer.png')
   import gspread
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open(r'/PATH_TO_KEY/KEY.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
json_key['private_key'].encode(), scope)
gc = gspread.authorize(credenti                                          
 
  from sklearn.metrics.pairwise import chi2_kernel
k_sim = chi2_kernel(X[0].reshape(1,-1), X)
kf = pd.DataFrame(k_sim).T
kf.columns = ['similarity']
kf.sort_values('similarity', ascending=False)
   import sys
import pandas as pd
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import
DesiredCapabilities
from selenium.webdriver.common.by import By                    
             

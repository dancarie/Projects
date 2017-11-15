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
 ipos.loc[ipos['Lead Mgr'].str.contains('Leerink'), 'Lead Mgr'] = 'Leerink
Partners'
ipos.loc[ipos['Lead Mgr'].str.contains('Lynch\xca'), 'Lead Mgr'] = 'Merrill
Lynch'
After this process is complete, you can run the following again to see the updated list:
for n in pd.DataFrame(ipos['Lead Mgr'].unique(),
columns=['Name']).sort_values('Name')['Name']:                            
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
   from flask import Flask, request, redirect
import twilio.twiml
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
app = Flask(__name__)
PATH_TO_CSV = 'your/path/here.csv'
df = pd.read_csv(PATH_TO_CSV)
convo = df.iloc[:,0]
clist = []
def qa_pairs(x):
 cpairs = re.findall(": (.*?)(?:$|\n)", x)
 clist.extend(list(zip(cpairs, cpairs[1:])))
convo.map(qa_pairs);
convo_frame = pd.Series(dict(clist)).to_frame().reset_index()
convo_frame.columns = ['q', 'a']
vectorizer = TfidfVectorizer(ngram_range=(1,3))
vec = vectorizer.fit_transform(convo_frame['q'])
@app.route("/", methods=['GET', 'POST'])
def get_response():
 input_str = request.values.get('Body')
 def get_response(q):
 my_q = vectorizer.transform([input_str])
 cs = cosine_similarity(my_q, vec)
 rs = pd.Series(cs[0]).sort_values(ascending=0)
 rsi = rs.index[0]
 return convo_frame.iloc[rsi]['a']
 resp = twilio.twiml.Response()
 if input_str:
 resp.message(get_response(input_str))
 return str(resp)
 else:
 resp.message('Something bad happened here.')
 return str(resp)          
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open(r'/PATH_TO_KEY/KEY.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials
Import re
  plt.style.use('ggplot')
%matplotlib inline
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 100)
pd.set_option("display.precision", 3)
# Use the file location of your Import.io csv
CSV_PATH = r"/Users/alexcombs/Downloads/magic.csv"
df = pd.read_csv(CSV_PATH)
df.columns
# select those listings with a bath
no_baths = su[~(su['propertyinfo_value'].str.contains('ba'))]
# exclude those missing bathroom info
sucln = su[~su.index.isin(no_baths.index)]
Now we can move on to parse out the bedroom and bathroom information:
# split using the bullet
def parse_info(row):
 if not 'sqft' in row:
 br, ba = row.split('')[:2]
 sqft = np.nan
 else:
 br, ba, sqft = row.split('.')[:3]
 return pd.Series({'Beds': br, 'Baths': ba, 'Sqft': sqft})
attr = sucln['propertyinfo_value'].apply(parse_info)
attr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import schedule
import time
import pickle
import json
import gspread
import requests
from bs4 import BeautifulSoup
from oauth2client.client import SignedJwtAssertionCredentials
# create our fetching function
def fetch_news():
 try:
 vect = pickle.load(open(r'/Users/alexcombs/Downloads/
 news_vect_pickle.p', 'rb'))
 model = pickle.load(open(r'/Users/alexcombs/Downloads/
 news_model_pickle.p', 'rb'))
 json_key = json.load(open(r'/Users/alexcombs/Downloads/

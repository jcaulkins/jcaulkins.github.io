try:
	from bs4 import BeautifulSoup
except ImportError as e: 
pass
try:
	!pip install nixtla
except ImportError as e: 
pass
try:
	!pip install pandas_datareader
except ImportError as e: 
pass
try:
	import pandas as pd 
except ImportError as e: 
pass
try:
import pandas_datareader.data as web 
except ImportError as e: 
pass
try:
import datetime 
except ImportError as e: 
pass
try:
from sklearn.model_selection import train_test_split
except ImportError as e: 
pass
try:
from nixtla import NixtlaClient
except ImportError as e: 
pass
try:
import dataframe_image as dfi
except ImportError as e: 
pass











# Set the start and end date for data collection 
start = datetime.datetime(2000, 1, 1) 
end = datetime.datetime.today() 

# Fetch data from FRED (S&P 500, Unemployment Rate, GDP, CPI, etc.) 
data_api_key = 'f991b096176052102274fd6f4bbfef0e' 

sp500 = web.DataReader('SP500', 'fred', start, end, api_key=data_api_key) 
unemployment = web.DataReader('UNRATE', 'fred', start, end, api_key=data_api_key) #updated once in three months 
gdp = web.DataReader('GDP', 'fred', start, end, api_key=data_api_key) #updated once in three months 
cpi = web.DataReader('CPIAUCSL', 'fred', start, end, api_key=data_api_key) #updated once in a month 
interest_rate = web.DataReader('FEDFUNDS', 'fred', start, end, api_key=data_api_key) #updated once in a month 
industrial_production = web.DataReader('INDPRO', 'fred', start, end, api_key=data_api_key) #updated once in a month 
retail_sales = web.DataReader('RSXFS', 'fred', start, end, api_key=data_api_key) #updated once in a month 
# Merge all data into one dataframe 
df = pd.merge_asof(sp500.sort_values('DATE'), unemployment.sort_values('DATE'), on='DATE') df = pd.merge_asof(df.sort_values('DATE'), gdp.sort_values('DATE'), on='DATE') 
df = pd.merge_asof(df.sort_values('DATE'), cpi.sort_values('DATE'), on='DATE') 
df = pd.merge_asof(df.sort_values('DATE'), interest_rate.sort_values('DATE'), on='DATE') 
df = pd.merge_asof(df.sort_values('DATE'), industrial_production.sort_values('DATE'), on='DATE') 
df = pd.merge_asof(df.sort_values('DATE'), retail_sales.sort_values('DATE'), on='DATE') 

# Display the cleaned data 
df_cleaned.head()
dfi.export(df, 'dataframe_image.png')








# Read the HTML file
with open("index.html", "r") as file:
    content = file.read()

# Parse the HTML
soup = BeautifulSoup(content, "html.parser")

# Modify the graphs
import random

graphy = soup.find("img", id="rtgraph") # Find paragraph by id
if graphy:
    graphy.src = "dataframe_image.png”

graphy = soup.find("img", id="rttable") # Find paragraph by id
if graphy:
    graphy.src = "dataframe_image.png”

paragraph = soup.find("p", id="updating") # Find paragraph by id
if paragraph:
    paragraph.string = "Updating Number = " + str(random.randint(1, 227))
    
# Save the changes
with open("index.html", "w") as file:
    file.write(str(soup))

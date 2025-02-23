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
df = pd.merge_asof(sp500.sort_values('DATE'), unemployment.sort_values('DATE'), on='DATE')
df = pd.merge_asof(df.sort_values('DATE'), gdp.sort_values('DATE'), on='DATE')
df = pd.merge_asof(df.sort_values('DATE'), cpi.sort_values('DATE'), on='DATE')
df = pd.merge_asof(df.sort_values('DATE'), interest_rate.sort_values('DATE'), on='DATE')
df = pd.merge_asof(df.sort_values('DATE'), industrial_production.sort_values('DATE'), on='DATE')
df = pd.merge_asof(df.sort_values('DATE'), retail_sales.sort_values('DATE'), on='DATE')

# Clean and interpolate missing values
df_cleaned = df.interpolate(method='linear')

# Display the cleaned data
df_cleaned.head()

from nixtla import NixtlaClient
api_key = 'nixak-S4pOCBGx86tm0CzCBF8Z1LGMstPXwnQ3u8o6IvlWkebsIsrLLIjrRuA8LeJ1g8kmaL0bxF0rGtYw8MHl'
nixtla_client = NixtlaClient(api_key = api_key)
# Forecast using Nixtla
sp500_prediction = nixtla_client.forecast(df=df_cleaned, h=30, finetune_depth=1, finetune_loss="mae", time_col='DATE', target_col='SP500',finetune_steps=15)
sp500_prediction.rename(columns={'TimeGPT':'SP500'}, inplace=True)





import matplotlib. pyplot as plt

#fcst_train
plt.figure(figsize=(14, 7))

# Filter the data for the last year
one_year_ago = pd.to_datetime('today') - pd.DateOffset(years=1)
mask = df_cleaned['DATE'] >= one_year_ago
df_filtered = df_cleaned[mask]

sp500_prediction = pd.concat([df_filtered.tail(1)[['DATE','SP500']], sp500_prediction])

# Plot the filtered data
plt.plot(df_filtered['DATE'], df_filtered['SP500'], color='blue')  # First plot in blue
plt.plot(sp500_prediction['DATE'], sp500_prediction['SP500'], color='red')


# Optionally, add labels and title
plt.xlabel('Date')
plt.ylabel('S&P 500')
plt.title('S&P 500 Data and Prediction')

# Adjust layout to avoid overlap
plt.savefig('updatedGraph.png')










# Read the HTML file
with open("index.html", "r") as file:
    content = file.read()

# Parse the HTML
soup = BeautifulSoup(content, "html.parser")

# Modify the graphs
import random

graphy = soup.find("img", id="rtgraph") # Find paragraph by id
if graphy:
    graphy.src = "updatedGraph.png”

tabley = soup.find("img", id="rttable") # Find paragraph by id
if tabley:
    tabley.src = "updatedTable.png”

paragraph = soup.find("p", id="updating") # Find paragraph by id
if paragraph:
    paragraph.string = "Updating Number = " + str(random.randint(1, 227))
    
# Save the changes
with open("index.html", "w") as file:
    file.write(str(soup))

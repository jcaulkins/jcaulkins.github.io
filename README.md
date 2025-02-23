# Sibyls of S&P - Real-time forecasting of S&P 500 Index 
ML model that forecasts the S&P 500 index for the next 30 days, updating daily.

## Inspiration
One of our team members recently started investing in U.S. stocks but lacks basic knowledge of how economic indexes influence overall stock price trends. Continuously checking the news to predict market movements is also challenging. To make the process easier, we decided to develop a model that incorporates the latest information.

## What it does
Our ML model and website forecast visualize the S&P 500 index for the next 30 days, updating daily. It provides a way for anyone interested in the stock market to easily understand the future direction of the market.
 
## How we built it
Using past and current data on the S&P 500 index, along with key economic indicators (Unemployment Rate, CPI, GDP, Interest Rate, Industrial Production, and Retail Sales) that closely influence it, our model was built using transfer learning from TimeGPT. The visualizations were created using Tableau and the website was created using Python and Javascript.

## Challenges we ran into
It was a little tricky making sure that the website updated itself correctly. There was also the issue of finding workable datasets free of charge, and then cleaning and editing these datasets to be on the same timescale. Since the S&P index is influenced by various complicated factors and has a growing trend, making a model that captures these trends was also challenging. 

## Accomplishments that we're proud of
We are proud of making a website that provides users with real-time predictions for the S&P 500 for the next 30 days. The interactive plots on our website also look really cool!

## What we learned
We learned some useful strategies for updating models and predictions in real-time, as well as how to work on a big project together, finding ways to fit things that people work on individually into one final product. 

## What's next for Sibyls of S&P - Real-time forecasting of S&P 500 Index
We aim to improve the long-term accuracy of our forecast by incorporating additional factors as inputs. Developing a model that predicts long-term changes in other economic indicators alongside the S&P 500 could further enhance our approach. Exploring alternative modeling approaches, such as using other pre-trained models or training from scratch, may also be beneficial.
<img width="1455" alt="image" src="https://github.com/user-attachments/assets/452b8264-df40-4a2b-8210-7abaf7838018" />

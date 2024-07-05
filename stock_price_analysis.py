import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
from warnings import filterwarnings
filterwarnings('ignore')

# Data collection
import glob
glob.glob('individual_stocks_5yr/*csv')

print(len(glob.glob('individual_stocks_5yr/*csv')))

company_list = ['individual_stocks_5yr/AAPL_data.csv',
                'individual_stocks_5yr/AMZN_data.csv',
                'individual_stocks_5yr/GOOG_data.csv',
                'individual_stocks_5yr/MSFT_data.csv']


all_data = pd.DataFrame()

for file in company_list:
    current_df = pd.read_csv(file)

    all_data = pd.concat([all_data, current_df], ignore_index=True)

print(all_data.shape)
print(all_data.head())
tech_list = all_data['Name'].unique()

# Analysing the change in price of the stock over time
print(all_data.isnull().sum())
print(all_data.dtypes)

all_data['date'] = pd.to_datetime(all_data['date'])
print(all_data['date'])

plt.figure(figsize=(20,12))

for index,company in enumerate(tech_list,1):
    plt.subplot(2,2,index)
    filter1 = all_data['Name']==company
    df = all_data[filter1]
    plt.plot(df['date'],df['close'])
    plt.title(company)
    
plt.show()

# Analysing moving average of the various stocks

print(all_data['close'].rolling(window=10).mean().head(15))

new_data = all_data.copy()

ma_day = [10,20,50]

for ma in ma_day:
    new_data['close_'+str(ma)]=all_data['close'].rolling(window=ma).mean()

print(new_data.tail(7))

new_data.set_index('date',inplace=True)

plt.figure(figsize=(20,12))

for index,company in enumerate(tech_list,1):
    plt.subplot(2,2,index)
    filter1 = new_data['Name']==company
    df = new_data[filter1]
    df[['close_10','close_20','close_50']].plot(ax=plt.gca())
    plt.title(company)
    
plt.show()

# observing closing price change in apple stock

apple = pd.read_csv('individual_stocks_5yr/AAPL_data.csv')

apple['daily return(in%)']=apple['close'].pct_change()*100
print(apple.head())

import plotly.express as px

fig = px.line(apple, x='date',y='daily return(in%)')
fig.show()

# resampling analysis

print(apple.dtypes)

apple['date']=pd.to_datetime(apple['date'])
print(apple.dtypes)

print(apple.head())

apple.set_index('date',inplace=True)
print(apple.head())

print(apple['close'].resample('ME').mean())
apple['close'].resample('ME').mean().plot()
plt.show()

print(apple['close'].resample('YE').mean())
apple['close'].resample('YE').mean().plot()
plt.show()

print(apple['close'].resample('QE').mean())
apple['close'].resample('QE').mean().plot()
plt.show()

# Multivariate analysis to understand corelation

app = pd.read_csv(company_list[0])
amzn = pd.read_csv(company_list[1])
google = pd.read_csv(company_list[2])
msft = pd.read_csv(company_list[3])

closing_price = pd.DataFrame()
closing_price['apple_close'] = app['close']
closing_price['amzn_close'] = amzn['close']
closing_price['google_close'] = google['close']
closing_price['msft_close'] = msft['close']

print(closing_price)

sns.pairplot(closing_price)
plt.show()

print(closing_price.corr())

sns.heatmap(closing_price.corr(),annot=True)
plt.show()

# corelation analysis

for col in closing_price.columns:

    closing_price[col + '_pct_change'] = (closing_price[col].shift(1)-closing_price[col])/closing_price[col].shift(1)*100

print(closing_price.columns)

closing_p = closing_price[['apple_close_pct_change', 'amzn_close_pct_change','google_close_pct_change', 'msft_close_pct_change']]

print(closing_p)

g = sns.PairGrid(data=closing_p)
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot)
g.map_upper(sns.kdeplot)

plt.show()

print(closing_p.corr())
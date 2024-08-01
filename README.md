# Stock Market Data Analysis Using Python

## Overview

This project analyzes stock market data for various tech companies over a 5-year period using Python. The goal is to fetch, preprocess, and analyze stock data to identify trends, calculate moving averages, and perform correlation analysis.

## Features

- Fetch and concatenate stock data for multiple companies
- Analyze stock price changes over time
- Calculate and visualize moving averages
- Perform resampling analysis for different time periods
- Conduct multivariate and correlation analysis

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/mangal0130/stock-market-analysis.git

cd stock-market-analysis
```

## Data Collection

The project uses CSV files from the `Data` folder.

## Usage

1. Run the analysis: Execute the code in your Python environment to fetch, preprocess, and analyze the stock data.
2. Visualize the data: Generate plots for stock prices, moving averages, and correlations.
3. Interpret the results: Use the visualizations and analysis to gain insights into stock market trends and relationships.

## Result

1. Change in price of stock over time:
   * by this analysis we can see the change in price over time like is the peak achieved or is it following the linear trend. 
   <img width="1269" alt="Screen Shot 2024-07-05 at 16 27 37" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/ac51d4d0-1698-4ab1-a0f5-8e839be5a987">

3. Moving average of the various stocks:
   * by this analysis we can see the moving average of the window 10,20 and 50 days. if we have more days of windows we will get good result.
   <img width="1223" alt="Screen Shot 2024-07-05 at 16 35 54" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/4298106d-95b1-4ed5-87d7-8d134da672ff">

5. Closing price change in apple stock:
   * by this analysis we can see the price change in percentage by daily basis.
   <img width="1376" alt="Screen Shot 2024-07-05 at 16 38 50" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/4c83c190-40c3-492a-95fd-191d919fc168">

7. Resampling analysis :
   * Monthly Analysis:
      * by this analysis we can see the average closing price by Monthly.
   <img width="612" alt="Screen Shot 2024-07-05 at 16 40 52" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/0636688f-bd1b-4ff4-b8ee-4dc19292d9f4">

   * Yearly Analysis:
      * by this analysis we can see the average closing price by Yearly.
   <img width="621" alt="Screen Shot 2024-07-05 at 16 41 12" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/b81594b4-7513-4980-ad4b-37d28bf9086b">

   * Quaterly Analysis:
     * by this analysis we can see the average closing price by Quarterly.
   <img width="605" alt="Screen Shot 2024-07-05 at 16 41 33" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/aace941a-da9d-4e3e-aff2-8fb5624e6ef1">

8. Multivarient Analysis:
   * pairplot : by this analysis we can see the coorelation between all the companies closing price value.
   <img width="1412" alt="Screen Shot 2024-07-05 at 16 45 17" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/bf9c6cac-abd9-4df6-a6a0-a54cbf7b1bb1">
   * Heatmap : by this analysis we can see the coorelation value among all the closing price.
   <img width="587" alt="Screen Shot 2024-07-05 at 16 45 31" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/ae49f94d-585b-477d-bf31-92b859e09e7c">

10. Corelation analysis:
    * pairgrid : by this analysis we can see the coorelation between all the companies closing price percentages change value.
   <img width="1419" alt="Screen Shot 2024-07-05 at 16 45 57" src="https://github.com/ayushi0130/stock_price_analysis/assets/128896031/1807e378-cd1a-4e04-a589-408425261bf5">

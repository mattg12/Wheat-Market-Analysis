
# Wheat Market Analysis - Initial Proposal

Garton Research & Trading - July 2019

## Business Context

The purpose of this project is to build predictive models for the price of Wheat Futures. There are several business applications of either a regression model which forecasts future prices, or of a classification model that assigns future outcomes into discrete buckets (i.e. up 5%, down 5%, flat). The classic example of course is to aid hedging decisions of both producers and end users of the commodity. Of course, there is an equal and similar demand for such a model from the perspective of a speculator or intermediary looking to place bets or manage risks. The model itself could be an end product in itself, or simply an input to a more comprehensive machine (such as a trading strategy, which may use this model's output as one of many signals).

## Data Understanding

This analysis requires at least four different sources of data: direct financial data (prices and volumes of exchange traded futures contracts), synthetic supply and demand data (commitment of trader reports on futures and options contracts), physical supply and demand data (supply and demand of the crop itself), and weather data for major wheat growing regions.

**Sources**
1. Futures data from quandl: https://www.quandl.com/data/CHRIS-Wiki-Continuous-Futures?keyword=wheat
2. Weather data from NOAA: https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
3. Physical supply and demand data (WASDE reports): https://www.usda.gov/oce/commodity/wasde/
4. Financial supply and demand data (CFTC CoT reports): https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm


## Data Preparation

1. Decide on scope of data required.
2. Write scripts to automate collection of data.
3. Preliminary EDA
4. Data cleaning
5. Construct data pipeline: collect --> clean --> combine --> save

## Modeling

1. ARIMA Models
2. VAR Models
3. FB Prophet Models
4. LSTM Models
5. Classification Models

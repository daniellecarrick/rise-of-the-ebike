# The Rise of Ebikes
This repo was created to explore if the sharp rise in ebike prices (from 0.15/minute in 2022 to .25/minute in 2024) affected the ridership. How much would the price need to be to make riders think twice?

# Getting started
1. To get the data, go to https://s3.amazonaws.com/tripdata/index.html and download and unzip the months of data you are interested in. Place the unzipped csvs inside of the a folder called "data" that you create in the root directory. The python script is designed to combine all of the monthly data files present in the data folder into one dataset.
2. Run `python3 index.py` to output a csv file where each row represents a week and there are two columns, one for the number of ebike rides and one for the number of classic bike rides.

| date     | classic_bike | electric_bike
| ----------- | ----------- | ----------- |
| 1     | 5890       | 9334 |
| 2  | 5216        | 8062 |
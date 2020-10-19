#!/usr/bin/env python3

import os
import pandas as pd

contract_loc = '/home/nikki/data-sc'
contract_files = list(file for file in os.listdir(contract_loc) if file[-3:] == 'csv')
output_loc = '/home/nikki/workspace/trading_evolved/data/sc_vol_adj_futures'

"""
Create a dictionary where the key is the ticker
and the value is a pandas dataframe of the OHLC time series
Run this every weekday at 13:00 GMT+7
"""
data_futures = {}
for file in contract_files:
    data_futures['-'.join(file.split('-')[:-1])] = pd.read_csv(f'{contract_loc}/{file}', usecols=[0, 5], index_col=0, parse_dates=True)

for key, item in data_futures.items():
    item.to_csv(f'{output_loc}/{key}.csv')

#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime

textsize = 28

# Read the CSVs as DataFrames
raw_df = pd.read_csv('date_usd_raw.csv')
log_df = pd.read_csv('date_usd_log.csv')

raw_df['Date'] = [datetime.datetime.strptime(elem, '%Y-%m-%d') for elem in raw_df['Date']]
date = raw_df['Date'].to_numpy()

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the raw data
plt.plot(date, raw_df['USD'].to_numpy(), label='Forward filled')

# Plot the log data
plt.plot(date, log_df['USD'].to_numpy(), label='Log transformed')

# Set title and labels
plt.title('USD forward filled vs log transformed', fontsize=textsize)
plt.xlabel('Date', fontsize=textsize)
plt.ylabel('USD', fontsize=textsize)

# Add legend
plt.legend(fontsize=textsize)

# Set y-axis limits to ensure both data ranges are visible
plt.ylim([min(min(log_df['USD']), min(raw_df['USD'])), 
          max(max(log_df['USD']), max(raw_df['USD']))])

# Increase tick label size
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

# Show the plot
plt.show()


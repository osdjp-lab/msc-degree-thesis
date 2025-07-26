#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import MinMaxScaler

textsize = 28

# Read the CSVs as DataFrames
diff_df = pd.read_csv('date_usd_diff.csv')
normalized_df = pd.read_csv('date_usd_normalized.csv')

diff_df['Date'] = [datetime.datetime.strptime(elem, '%Y-%m-%d') for elem in diff_df['Date']]
normalized_df['Date'] = [datetime.datetime.strptime(elem, '%Y-%m-%d') for elem in normalized_df['Date']]

diff_date = diff_df['Date'].to_numpy()
normalized_date = normalized_df['Date'].to_numpy()

scaler = MinMaxScaler(feature_range=(-1,1))
test = scaler.fit_transform(diff_df['USD'].to_numpy().reshape(-1,1))

# Create a new figure
# plt.figure(figsize=(10, 6))

# Plot the diff data
# plt.plot(diff_date, diff_df['USD'].to_numpy(), label='Differenced')

# Plot the normalized data
plt.plot(normalized_date, normalized_df['USD'].to_numpy(), label='USD')

# Set title and labels
plt.title('Undifferenced USD exchange rate', fontsize=textsize)
plt.xlabel('Date', fontsize=textsize)
plt.ylabel('USD', fontsize=textsize)

# Add legend
plt.legend(fontsize=textsize)

# Set y-axis limits to ensure both data ranges are visible
# plt.ylim([min(min(diff_df['USD']), min(normalized_df['USD'])), 
#           max(max(diff_df['USD']), max(normalized_df['USD']))])

# Increase tick label size
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

# Show the plot
plt.show()

###############################

# Create a new figure
# plt.figure(figsize=(10, 6))

# Plot the diff data
plt.plot(diff_date, diff_df['USD'].to_numpy(), label='USD')

# Plot the normalized data
# plt.plot(normalized_date, normalized_df['USD'].to_numpy(), label='Undifferenced')

# Set title and labels
plt.title('Differenced USD exchange rate', fontsize=textsize)
plt.xlabel('Date', fontsize=textsize)
plt.ylabel('USD', fontsize=textsize)

# Add legend
plt.legend(fontsize=textsize)

# Set y-axis limits to ensure both data ranges are visible
# plt.ylim([min(min(diff_df['USD']), min(normalized_df['USD'])), 
#           max(max(diff_df['USD']), max(normalized_df['USD']))])

# Increase tick label size
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

# Show the plot
plt.show()


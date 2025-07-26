#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime

textsize = 28

# Read the CSVs as DataFrames
normalized_df = pd.read_csv('date_usd_normalized.csv')
standardized_df = pd.read_csv('date_usd_standardized.csv')
unnormalized_df = pd.read_csv('date_usd_unnormalized.csv')

normalized_df['Date'] = [datetime.datetime.strptime(elem, '%Y-%m-%d') for elem in normalized_df['Date']]
date = normalized_df['Date'].to_numpy()

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the normalized data
plt.plot(date, normalized_df['USD'].to_numpy(), label='Normalized')

# Plot the standardized data
plt.plot(date, standardized_df['USD'].to_numpy(), label='Standardized')

# Plot the unnormalized data
plt.plot(date, unnormalized_df['USD'].to_numpy(), label='Unscaled')

# Set title and labels
plt.title('USD feature scaling comparison', fontsize=textsize)
plt.xlabel('Date', fontsize=textsize)
plt.ylabel('USD', fontsize=textsize)

# Add legend
plt.legend(fontsize=textsize)

# Set y-axis limits to ensure both data ranges are visible
plt.ylim([min(min(normalized_df['USD']), min(unnormalized_df['USD']), min(standardized_df['USD'])), 
          max(max(normalized_df['USD']), max(unnormalized_df['USD']), max(standardized_df['USD']))])

# Increase tick label size
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

# Show the plot
plt.show()


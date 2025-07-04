#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime

textsize = 28

# Read the CSVs as DataFrames
nn_fcv = pd.read_csv('nn_feature_cv_scores.csv')
svr_fcv = pd.read_csv('svr_feature_cv_scores.csv')
rf_fcv = pd.read_csv('rf_feature_cv_scores.csv')

count = nn_fcv['number_of_features'].to_numpy()

# Create a new figure
plt.figure(figsize=(10, 6))

plt.plot(count, nn_fcv['cross_validation_score'].to_numpy(), label='Normalized')
plt.plot(count, svr_fcv['cross_validation_score'].to_numpy(), label='Standardized')
plt.plot(count, rf_fcv['cross_validation_score'].to_numpy(), label='None')

# Set title and labels
plt.title('Cross validation scores by number of features', fontsize=textsize)
plt.xlabel('Number of features', fontsize=textsize)
plt.ylabel('Cross validation score', fontsize=textsize)

# Add legend
plt.legend(fontsize=textsize)

# Set y-axis limits to ensure both data ranges are visible
plt.ylim([-2,1])

# Increase tick label size
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

# Show the plot
plt.show()


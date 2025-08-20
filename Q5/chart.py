# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic marketing data
np.random.seed(42)
n = 200
data = pd.DataFrame({
    'Marketing Spend (USD)': np.random.normal(50000, 15000, n).clip(10000, 100000),
    'Customer Acquisitions': np.random.normal(1200, 300, n).clip(100, 2500),
    'Campaign Type': np.random.choice(['Social Media', 'Email', 'TV', 'Radio'], n)
})

# Create figure with exact pixel dimensions
fig = plt.figure(figsize=(8, 8), dpi=64)  # 8 * 64 = 512 pixels

# Create scatterplot
scatter = sns.scatterplot(
    data=data,
    x='Marketing Spend (USD)',
    y='Customer Acquisitions',
    hue='Campaign Type',
    palette='Set2',
    s=100,
    edgecolor='black',
    alpha=0.8
)

# Customize labels and title
plt.title('Marketing Spend vs Customer Acquisitions', fontsize=18)
plt.xlabel('Marketing Spend (USD)', fontsize=14)
plt.ylabel('Customer Acquisitions', fontsize=14)
plt.legend(title='Campaign Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Save the figure without bbox_inches='tight'
plt.savefig('chart.png')  # Will be exactly 512x512 px
plt.close()

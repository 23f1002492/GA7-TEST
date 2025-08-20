import pandas as pd
import matplotlib.pyplot as plt

# Quarterly MRR Growth Data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'MRR_Growth': [3.57, 9.28, 8.93, 12.93],
}

industry_target = 15

df = pd.DataFrame(data)
average_growth = df['MRR_Growth'].mean()

# Line Plot for MRR Growth Trend
plt.figure(figsize=(8, 5))
plt.plot(df['Quarter'], df['MRR_Growth'], marker='o', label='Company MRR Growth')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (15%)')
plt.title('Quarterly MRR Growth vs Industry Target')
plt.xlabel('Quarter')
plt.ylabel('MRR Growth (%)')
plt.legend()
plt.grid(True)
plt.savefig('visuals/mrr_trend.png')

# Bar Chart Comparison
plt.figure(figsize=(6, 5))
bars = plt.bar(df['Quarter'], df['MRR_Growth'], color='skyblue')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (15%)')
plt.title('Quarterly MRR Growth Comparison')
plt.xlabel('Quarter')
plt.ylabel('MRR Growth (%)')
plt.legend()
plt.grid(True)
plt.savefig('visuals/mrr_vs_industry.png')

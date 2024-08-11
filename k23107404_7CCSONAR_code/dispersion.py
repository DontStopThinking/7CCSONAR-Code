# %%
import pandas as pd

# %%
# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Convert the 'dateadded' and 'last_online' columns to datetime
data['dateadded'] = pd.to_datetime(data['dateadded'])
data['last_online'] = pd.to_datetime(data['last_online'])

# %%
# Calculate the lifespan of each URL in seconds
data['url_lifespan'] = (data['last_online'] - data['dateadded']).dt.total_seconds()

# %%
min_lifespan = data['url_lifespan'].min()
max_lifespan = data['url_lifespan'].max()
r = max_lifespan - min_lifespan # Range

print(f'Min lifespan of a URL: {min_lifespan:.2f} seconds')
print(f'Max lifespan of a URL: {max_lifespan:.2f}')
print(f'Range of URL lifespan: {r:.2f} seconds')

# %%
url_lifespan_mean = data['url_lifespan'].mean()
url_lifespan_std = data['url_lifespan'].std() # Standard deviation

# %%
print(f'Mean of URL lifespans: {url_lifespan_mean:.2f} seconds')
print(f'Standard deviation of URL lifespans: {url_lifespan_std:.2f} seconds')

# %%
Q1 = data['url_lifespan'].quantile(0.25) # First quartile
Q3 = data['url_lifespan'].quantile(0.75) # Second quartile
IQR = Q3 - Q1 # Interquartile Range

# %%
print(f'Value of first quartile: {Q1:.2f} seconds')
print(f'Value of third quartile: {Q3:.2f} seconds')
print(f'Interquartile Range: {IQR:.2f} seconds')

# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# %%
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Convert date columns to datetime
data['dateadded'] = pd.to_datetime(data['dateadded'])
data['last_online'] = pd.to_datetime(data['last_online'])

# Calculate lifespan in days
data['lifespan_days'] = (data['last_online'] - data['dateadded']).dt.days

# Calculate number of tags
data['num_tags'] = data['tags'].apply(lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)

# Drop NaN values from the columns
data_clean = data.dropna(subset=['lifespan_days', 'num_tags'])

# %%
x = data_clean[['lifespan_days']].values
y = data_clean[['num_tags']].values

# %%
model = LinearRegression()
model.fit(x, y)

# %%
print(f'R-Squared value for linear regression between URL lifespan and number of tags: {model.score(x, y):.2}')

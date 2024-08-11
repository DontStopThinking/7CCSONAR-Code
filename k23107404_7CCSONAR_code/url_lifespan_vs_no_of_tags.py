# %%
import pandas as pd
import plotly.express as px

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

# %%
fig = px.scatter(
    data,
    x='lifespan_days',
    y='num_tags',
    title='URL Lifespan vs. Number of Tags',
    labels={'lifespan_days': 'Lifespan (days)', 'num_tags': 'Number of Tags'},
    opacity=0.6)

# Show the plot
fig.show()

# %%
fig.write_image('url_lifespan_vs_no_of_tags.svg')

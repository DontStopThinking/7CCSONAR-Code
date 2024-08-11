# %%
import pandas as pd
import plotly.express as px

# %%
# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Convert the 'dateadded' and 'last_online' columns to datetime
data['dateadded'] = pd.to_datetime(data['dateadded'])
data['last_online'] = pd.to_datetime(data['last_online'])

# Calculate the lifespan of each URL in seconds
data['url_lifespan'] = (data['last_online'] - data['dateadded']).dt.total_seconds()

# %%
fig = px.box(data, y='url_lifespan', title='Box Plot of URL Lifespans', labels={'url_lifespan': 'Lifespan (seconds)'})
fig.update_yaxes(type='log')
fig.update_layout(width=800)

# Show the plot
fig.show()

# %%
fig.write_image('dispersion_boxplot.png')
fig.write_image('dispersion_boxplot.svg')
fig.write_html('dispersion_boxplot.html')

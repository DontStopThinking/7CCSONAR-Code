# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Define a custom template with black edges for histogram bars
pt = pio.templates['plotly']
pt.data.histogram[0].marker.line.color = 'black'
pt.data.histogram[0].marker.line.width = 1
pio.templates['custom'] = pt
pio.templates.default = 'custom'

# %%
# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Convert the date columns to datetime objects with the correct format
data['dateadded'] = pd.to_datetime(data['dateadded'], format='%Y-%m-%d %H:%M:%S')
data['last_online'] = pd.to_datetime(data['last_online'], format='%Y-%m-%d %H:%M:%S')

# Calculate the duration each URL was online
data['duration_online'] = (data['last_online'] - data['dateadded']).dt.total_seconds() / 3600  # in hours

# Filter out URLs that are still online
offline_data = data[data['url_status'] != 'online']

# %%
# Plot the distribution of durations using Plotly
fig = px.histogram(
    offline_data,
    x='duration_online',
    nbins=50,
    title='Histogram of Time Taken for URLs to Go Offline',
    labels={'duration_online': 'Time Online (hours)', 'count': 'Number of URLs'}
)

fig.update_traces(
    texttemplate='%{y}',
    textposition='outside'
)

# Update layout for better visualization
fig.update_layout(
    yaxis_title='Number of URLs (Logarithmic Scale)',
    xaxis_title='Time Online (hours)'
)

fig.update_yaxes(type='log')

# Show the plot
fig.show()

# %%
fig.write_image('url_lifespan.svg')
fig.write_image('url_lifespan.png')
fig.write_html('url_lifespan.html')

# %%
# Calculate mean and median lifespan
mean_lifespan = offline_data['duration_online'].mean()
median_lifespan = offline_data['duration_online'].median()

print(f"Mean Lifespan: {mean_lifespan:.2f} hours")
print(f"Median Lifespan: {median_lifespan:.2f} hours")

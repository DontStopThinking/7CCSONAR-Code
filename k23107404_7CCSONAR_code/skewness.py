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
# Convert the 'dateadded' column to datetime format
data['dateadded'] = pd.to_datetime(data['dateadded'], format='%Y-%m-%d %H:%M:%S')

# %%
# Calculate the skewness of our data on the 'dateadded' column
date_skewness = data['dateadded'].value_counts().skew()
print(f"Skewness of 'dateadded' distribution using pandas: {date_skewness:.2f}")

# %% [markdown]
# A value of 5.59 indicates that our dataset is highly skewed towards recent dates.
# This means that the majority of URLs in our dataset have been added recently with some outliers that that were added on
# older dates

# %%
# Plot a histogram to visualize the distribution of 'dateadded'
fig = px.histogram(
    data,
    x='dateadded',
    nbins=30,
    title='Distribution of URLs As Per Their Date Added')
fig.update_traces(
    texttemplate='%{y}',
    textposition='outside'
)
fig.update_layout(
    xaxis_title='Date Added',
    yaxis_title='Frequency (Logarithmic scale)',
    xaxis=dict(tickangle=45),
    yaxis=dict(type='log'), # Since our data is skewed, we use logarithmic scale to better see our histogram.
    width=800)
fig.show()

# %%
fig.write_image('skewness.svg')
fig.write_image('skewness.png')
fig.write_html('skewness.html')

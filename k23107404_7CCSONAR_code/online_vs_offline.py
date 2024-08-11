# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio

# %%
# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Count URLs by their status (online/offline)
url_status_counts = data['url_status'].value_counts()

# %% [markdown]
# # Pie Chart

# %%
fig = px.pie(
    names=url_status_counts.index,
    values=url_status_counts.values,
    title='URL Status Distribution',
    labels={'names': 'Status', 'values': 'Count'}
)

fig.update_layout(width=500)

fig.update_traces(
    textinfo='label+percent',
    textposition='inside'
)

fig.show()

# %%
fig.write_image('url_status_dist_pie.svg', scale=2)

# %% [markdown]
# # Bar Chart

# %%
fig = px.bar(
    x=url_status_counts.index,
    y=url_status_counts.values,
    title='Frequency of URL Status (Online/Offline)',
    labels={'x': 'URL Status', 'y': 'Count'},
    text=url_status_counts.values
)

fig.update_layout(
    xaxis_title='URL Status',
    yaxis_title='Count',
    yaxis=dict(showgrid=True),
    xaxis=dict(showgrid=True),
    width=500
)

fig.update_traces(textposition='outside')

fig.show()

# %%
fig.write_image('url_status_bar.svg')

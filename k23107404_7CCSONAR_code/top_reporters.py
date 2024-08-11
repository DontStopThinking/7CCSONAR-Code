# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Top reporters
number = 7
top_reporters = data['reporter'].value_counts().head(number)

# %% [markdown]
# # Bar Graph

# %%
# Create a bar chart
fig = px.bar(
    x=top_reporters.index,
    y=top_reporters.values,
    title=f'Top {number} Reporters',
    labels={'x': 'Reporter', 'y': 'Number of URLs Reported'}
)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Reporter',
    yaxis_title='Number of URLs Reported',
    xaxis_tickangle=-45,
    yaxis_showgrid=True,
    width=800
)

# Show the plot
fig.show()

# %%
fig.write_image('top_reporters.svg')

# %% [markdown]
# # Pie Chart

# %%
fig = px.pie(
    values=top_reporters.values,
    names=top_reporters.index,
    title=f'Top {number} Reporters Distribution',
    hole=0,  # Use this parameter to make it a donut chart if desired
)

fig.update_layout(width=500)

fig.show()

# %%
fig.write_image('top_reporters_pie.svg')

# %%

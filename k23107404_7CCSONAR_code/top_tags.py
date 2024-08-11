# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Split tags and explode to count each tag individually.
tags_split = data['tags'].str.split(',')
tags_exploded = tags_split.explode()

# Count the frequency of the top 10 tags
tag_counts = tags_exploded.value_counts().head(10)

# %% [markdown]
# # Bar Chart

# %%
fig = px.bar(
    x=tag_counts.index,
    y=tag_counts.values,
    title='Top 10 Tags',
    labels={'x': 'Tag', 'y': 'Frequency'}
)

fig.update_layout(
    xaxis_tickangle=45,
    xaxis=dict(tickmode='linear'),
    yaxis=dict(showgrid=True),
    width=800)

fig.show()

# %%
fig.write_image('top_tags.svg')

# %% [markdown]
# # Pie Chart

# %%
fig = px.pie(
    names=tag_counts.index,
    values=tag_counts.values,
    title='Top 10 Tags Distribution',
    labels={'names': 'Tag'}
)

fig.update_layout(width=500)

fig.show()

# %%
fig.write_image('top_tags_pie.svg')

# %%

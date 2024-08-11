# %%
import pandas as pd
import plotly.express as px

# %%
# Load the dataset
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Ensure all entries in the tags column are strings and handle missing values
data['tags'] = data['tags'].fillna('').astype(str)

# %%
# Split the tags into a list and count the frequency of each unique combination
data['tag_list'] = data['tags'].apply(lambda x: tuple(sorted(x.split(','))))
tag_combinations = data['tag_list'].value_counts().head(10).reset_index()
tag_combinations.columns = ['tag_combination', 'frequency']

tag_combinations['tag_combination_str'] = tag_combinations['tag_combination'].apply(lambda x: ', '.join(x))

print(tag_combinations)

# %%
fig = px.bar(
    tag_combinations,
    x='tag_combination_str',
    y='frequency',
    labels={'tag_combination_str': 'Tag Combination', 'frequency': 'Frequency'},
    title='Frequency of Tag Combinations in Malicious URLs',
    text='frequency')

fig.update_traces(textposition='outside', texttemplate='%{text:.2s}')

fig.update_layout(xaxis_title='Tag Combination', yaxis_title='Frequency', xaxis_tickangle=-45, height=700)

fig.show()

# %%
fig.write_image('tag_combinations.svg')
fig.write_image('tag_combinations.png')
fig.write_html('tag_combinations.html')

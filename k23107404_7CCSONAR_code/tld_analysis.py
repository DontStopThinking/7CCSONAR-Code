# %%
import pandas as pd
import plotly.express as px
from urllib.parse import urlparse

# %%
data = pd.read_csv('dataset.csv', skiprows=8)

# %%
# Extract top-level domains (TLDs) from URLs
def extract_tld(url):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    return domain_parts[-1] if len(domain_parts) > 1 else ''

# %%
# Add TLD column
data['tld'] = data['url'].apply(extract_tld)

# Count frequencies of TLDs
tld_counts = data['tld'].value_counts().reset_index()
tld_counts.columns = ['TLD', 'Count']

# %%
# Plot TLD frequencies
fig = px.bar(tld_counts.head(10), x='TLD', y='Count', title='Top 10 Most Common TLDs in Malicious URLs')
fig.show()

# %%
fig.write_image('tld_analysis.svg')

import pandas as pd
dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)')
df = dfs[0]
data = df.to_json(orient='records')
with open('countries.json', 'w') as f:
    f.write(data)
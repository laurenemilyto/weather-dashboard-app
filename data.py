import pandas as pd

# Read CSV file
df = pd.read_csv('Resources/cities.csv')

# Save to HTML file
df.to_html('data.html', index=False)

# Assign to string
table = df.to_html()
print(table)
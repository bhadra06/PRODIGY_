import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'world_population.csv'
df = pd.read_csv(file_path)

# Sort the data by population in descending order
df = df.sort_values(by='2019', ascending=False)

# Take the top 5 countries by population
top_countries = df.head(5)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country Name'], top_countries['2019'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Top 5 Countries by Population in 2019')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

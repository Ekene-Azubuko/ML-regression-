import matplotlib.pyplot as plt
import pandas as pd

# Assuming the column names in your dataset are 'Butterfly species', 'Day of Year', 'BC Spring Temp (˚C)', 'BC Summer Temp (˚C)', and 'Year'

# Read the dataset
df = pd.read_csv("ea.csv")

# Filter data for Cupido amyntula
cupido_data = df[df['Butterfly species'] == 'Cupido amyntula']

# Plotting the relationship between flight dates and temperatures for Cupido amyntula
plt.figure(figsize=(10, 6))

# Plotting Spring temperatures against flight dates for Cupido amyntula
plt.scatter(cupido_data['BC Spring Temp (˚C)'], cupido_data['Day of Year'], c=cupido_data['Year'], cmap='viridis', label='Spring Temp', marker='o')

plt.xlabel('Temperature (°C)')
plt.ylabel('Day of Year')
plt.title('Relationship between Flight Timing of Cupido amyntula and Spring Temperatures')
plt.colorbar(label='Year')
plt.legend()
plt.xlim(cupido_data['BC Spring Temp (˚C)'].min()-2, cupido_data['BC Spring Temp (˚C)'].max()+2)  # Adjust x-axis limits
plt.grid(True)
plt.show()

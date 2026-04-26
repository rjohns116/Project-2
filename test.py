import plotly.express as px
import pandas as pd

# Sample data: cities with coordinates and population
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Latitude": [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    "Longitude": [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    "Population": [8419600, 3980400, 2716000, 2328000, 1690000]
}

df = pd.DataFrame(data)

# Create bubble map
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    text="City",  # Hover text
    size="Population",  # Bubble size
    size_max=50,  # Max bubble size
    projection="natural earth",
    title="US Cities Population Bubble Map",
    color="Population",  # Bubble color
    color_continuous_scale=px.colors.sequential.Plasma
)

# Show map
fig.show()





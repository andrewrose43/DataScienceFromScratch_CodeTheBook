from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Make a line chart. Years on x-axis, GDP on y-axis.
# Make the line solid and green with "o" markers.
plt.plot(years, gdp, linestyle="dotted", color="red", marker='*')

# Add a title.
plt.title("Nominal GDP")

# Add a y-axis label.
plt.ylabel("Billions of Dollars")

# Show the graph.
plt.show()


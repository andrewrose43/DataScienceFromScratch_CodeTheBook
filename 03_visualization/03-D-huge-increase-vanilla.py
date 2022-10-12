# Note: this one didn't introduce any new material, so I didn't drill myself on it like the other exercises.

from matplotlib import pyplot as plt

# Note: I've used tuples instead of lists; they're faster & more appropriate for immutable data.
mentions = (500, 505)
years = (2017, 2018)

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

# The book said the following line was necessary, but removing it has no effect.
# plt.ticklabel_format(useOffset=False)

# Misleading y-axis.
# plt.axis((2016.5, 2018.5, 499, 506))
# plt.title("Look at the 'Huge' Increase!")

# Honest y-axis.
plt.axis((2016.5, 2018.5, 0, 550))
plt.title("Not So Huge Anymore")

plt.show()

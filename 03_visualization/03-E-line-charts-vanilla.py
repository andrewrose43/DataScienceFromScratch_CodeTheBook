from matplotlib import pyplot as plt

# Note: across this file, I've used tuples instead of lists, which are faster and more appropriate for immutable data. I didn't deem this significant enough of a change to warrant a "variant" file.
variance = (1, 2, 4, 8, 16, 32, 64, 128, 256)
bias_squared = (256, 128, 64, 32, 16, 8, 4, 2, 1)

# Pythonically create a tuple that sums variance and bias_squared
total_error = tuple(x+y for x, y in zip(variance, bias_squared))

# The x-indices to plot the data with
x_inds = tuple(x for x, _ in enumerate(variance))

# We can make multiple calls to plt.plot to show multiple series on the same chart.
plt.plot(x_inds, variance, 'g-', label='variance')  # variance: green solid line
plt.plot(x_inds, bias_squared, 'r.-', label='bias squared')  # bias squared: red dot-dashed line
plt.plot(x_inds, total_error, 'b:', label='total error')  # total error: blue dotted line

plt.legend(loc=9)  # Add a legend in the top middle
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()

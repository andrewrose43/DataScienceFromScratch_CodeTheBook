from matplotlib import pyplot as plt

# Changed to tuples from the book's lists again.
friends = (70, 65, 72, 63, 71, 64, 60, 64, 67)
minutes = (175, 170, 205, 120, 220, 130, 105, 145, 190)
labels = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

# Make the scatter plot
plt.scatter(friends, minutes)

# Label each point, with each label slightly offset.
# Set the offset of the labels to offset-points mode.
for friend_count, minute_count, label in zip(friends, minutes, labels):
    plt.annotate(
        text=label,
        textcoords='offset points',
        xy=(friend_count, minute_count),
        xytext=(5, -5)
    )


plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of Friends")
plt.ylabel("Daily minutes spent on the site")
plt.show()

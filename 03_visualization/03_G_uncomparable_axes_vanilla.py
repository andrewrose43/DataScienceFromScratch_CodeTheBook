from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Comparable (with the plt.axis(\"equal\") call)")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

# This next line is the crux of the example. It causes the x and y axes to have equal ranges.
plt.axis("equal")

plt.show()


from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s.
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)



plt.bar(
    [x+5 for x in histogram],  # locations of bars - shift them half their width to the right so the ticks are on the bars' edges
    [x for x in histogram.values()],  # Number of items in each bucket. This is unnecessarily verbose; histogram.values() would do
    10,  # width of each bar
    edgecolor=(0, 0, 0)  # black edges around bars
)

plt.axis([-5, 105, 0, 5])  # x-axis from -5 to 105; y-axis from 0 to 5

# x - axis labels at 0, 10, ..., 100
plt.xticks([10*i for i in range(11)])  # More bad syntax. range(0, 110, 10) would be better.

plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

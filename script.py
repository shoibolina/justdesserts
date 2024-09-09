######################################################################################
# Strengths:
# The code is easy to read and understand
# The statistics module is used correctly to compute the mean, median, and standard deviation
# The check for an empty list will catch corner cases like division by zero in calculating statistics on an empty list.

# Suggestion for improvement:
# I've re-written one corner case to handle cases when the data points are empty or 1.
# If the data points provided are not int/float, we need to capture that too
######################################################################################

# Simple code to calculate the mean, median, and standard deviation of a list of numbers

import statistics # importing package to use built-in functions

def analyze_data(data):
    # Suggestion1: I've re-written your corner case to handle cases when the data points are empty or 1.
    if len(data) < 2:
        print("The data list need at least two data points to calculate standard deviation!")
        return

    # Suggestion 2: If the data points provided are not int/float, we need to capture that too
    if not all(isinstance(i, (int, float)) for i in data):
        print("The data list must contain only numbers!")
        return

    mean = statistics.mean(data)
    median = statistics.median(data)
    std = statistics.stdev(data)

    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")

arr = [10, 20, 30, 40, 50]
analyze_data(arr)

import statistics

def analyze_data(data):
    if not data:
        print("The data list is empty!")
        return

    mean = statistics.mean(data)
    median = statistics.median(data)
    std = statistics.stdev(data)

    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")

arr = [10, 20, 30, 40, 50]
analyze_data(arr)

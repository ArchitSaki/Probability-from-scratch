import numpy as np

def descriptive_statistics(data):
    # mean
    total = 0
    for i in data:
        total += i
    mean = total / len(data)

    # median
    sort_data = sorted(data)
    n = len(data)
    if n % 2 != 0:  # odd
        median = sort_data[n // 2]
    else:  # even
        median = (sort_data[n // 2 - 1] + sort_data[n // 2]) / 2

    # mode
    mode = data[0]
    max_count = 0
    for i in data:
        count = data.count(i)
        if count > max_count:
            max_count = count
            mode = i

    # variance
    variance = 0
    for i in data:
        variance += ((i - mean) ** 2)
    variance = variance / len(data)

    # standard deviation
    std_dev = np.sqrt(variance)

    # percentiles
    percentiles = []
    percentiles.append(sort_data[int(n * 0.25)])
    percentiles.append(median)
    percentiles.append(sort_data[int(n * 0.75)])

    # interquartile range
    iqr = percentiles[2] - percentiles[0]

    # create dictionary
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance, 4),
        "standard_deviation": np.round(std_dev, 4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }

    return stats_dict

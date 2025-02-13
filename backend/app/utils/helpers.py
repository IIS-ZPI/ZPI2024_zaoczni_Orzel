from collections import Counter
import numpy as np
from app.schemas.response import Statistics, TrendChangesHistogram
from typing import List
import statistics


def generate_trend_changes_histogram(values: List[float]) -> TrendChangesHistogram:
    values = np.array(values)
    q75, q25 = np.percentile(values, [75 ,25])
    iqr = q75 - q25
    bin_width = 2 * iqr * len(values) ** (-1/3)
    bins = max(4, int((values.max() - values.min()) / bin_width)) if bin_width > 0 else 4
    
    hist=np.histogram(values, bins)

    histogram = TrendChangesHistogram(values=hist[0], labels=hist[1])
    return histogram


def calculate_statistics(values: List[float]) -> Statistics:
    if not values:
        raise ValueError("No values provided for statistics calculation.")

    median_val = statistics.median(values)
    mean_val = statistics.mean(values)
    stdev_val = statistics.stdev(values) if len(values) > 1 else 0.0
    coeff_var = stdev_val / mean_val if mean_val != 0 else 0.0
    trend_changes = np.diff(values)
    increasing_trend = trend_changes[trend_changes > 0].size
    decreasing_trend = trend_changes[trend_changes < 0].size
    stable_trends = trend_changes[trend_changes == 0].size
    counter = Counter(values)
    max_count = max(counter.values())
    if max_count == 1:
        dominant = []
    else:
        dominant = [num for num, count in counter.items() if count == max_count]

    stats = Statistics(
        increasingTrend=increasing_trend,
        decreasingTrend=decreasing_trend,
        stableTrends=stable_trends,
        median=median_val,
        coeffOfVariation=coeff_var,
        standardDeviation=stdev_val,
        dominant=dominant
    )

    return stats

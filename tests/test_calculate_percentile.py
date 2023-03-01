from calculate_percentile import calculatePercentileOfDataset, calculatePercentileOfLogNormalDist

def test_calculatePercentileOfDataset_0_to_10():
    dataset = range(0, 10)
    percentile = calculatePercentileOfDataset(dataset, percentile=10, precision=0)
    assert percentile == 1

def test_calculatePercentileOfDataset_with_precision_1():
    dataset = range(0, 100)
    percentile = calculatePercentileOfDataset(dataset, percentile=10, precision=1)
    assert percentile == 9.9

def test_calculatePercentileOfLogNormalDist():
    mean = 3

    percentile = \
      calculatePercentileOfLogNormalDist(
          mean=mean,
          standard_deviation=2,
          sample_count=100_000,
          percentile=10,
          precision=2
      )
    
    assert percentile < mean, "10th percentile is above mean which is highly unlikely!"
    assert percentile > 0
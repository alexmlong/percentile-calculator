import numpy as np

def calculatePercentileOfDataset(dataset, percentile, precision):
  percentile = np.percentile(dataset, percentile)
  rounded_percentile = round(percentile, precision)
  return rounded_percentile

def calculatePercentileOfLogNormalDist(mean=3, standard_deviation=2, sample_count=100_000, percentile=10, precision=2):
  dataset = np.random.lognormal(mean=mean, sigma=standard_deviation, size=sample_count)
  return calculatePercentileOfDataset(dataset, percentile, precision)

if __name__ == '__main__':
  print(calculatePercentileOfLogNormalDist())
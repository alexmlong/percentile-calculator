# Percentile Calculator

This script generates random samples in a lognormal distribution
and then returns a specified percentile given those samples.

It allows for the setting of these parameters:

- Number of samples to generate
- Mean of distribution
- Standard deviation of distribution
- Percentile to calculate
- Precision to return percentile in

# Setup

Install requirements with `pip install -r requirements.txt`

# Running script

Run the calculation with the default parameters with the command `python src/calculate_percentile.py`.

# Running tests

Run `py.test tests/test_calculate_percentile.py` to run tests.

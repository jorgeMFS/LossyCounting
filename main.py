
import os

from algorithm.LossyCounting import LossyCounting
from error.DeterministicAlgorithm import DeterministicAlgorithm
from error.RelativeError import RelativeError
from stream.FileGen import read_to_stream


dir_path = os.path.dirname(os.path.realpath(__file__))
path = 'tests/files'
directory = os.path.dirname(__file__)
filename = os.path.join(directory, path)
os.chdir(filename)
data = read_to_stream("1000stream.txt")

# Define k and epsilon
epsilon = 1 / 20
k = 1/epsilon

# Lossy Counting Algorithm
c = LossyCounting(k)
for elem in data:
    c.counting(elem)
c.__str__()

# Deterministic Counting Algorithm
deterministic_counter = DeterministicAlgorithm()
deterministic_counter.count(data)
deterministic_counter.__str__()

# Relative error Algorithm
relative_error = RelativeError()
relative_error.relative_error(c.get_counters(), deterministic_counter.get_counters())
relative_error.__str__()
print("relative_error : " + str(relative_error.avg_error()))

# Thresholds
'''
for item, count in sorted(c.threshold_rate(0.05), key=lambda x: x[1]):
    print(item, count)
print('\n')
for item, count in sorted(c.apply_threshold(40), key=lambda x: x[1]):
    print(item, count)
'''
"""
Created on 27/12/2016

@author: Jorge Miguel Ferreira da Silva
"""

from error.RelativeError import RelativeError
from algorithm.LossyCounting import LossyCounting
from error.DeterministicAlgorithm import DeterministicAlgorithm
from stream.FileGen import read_to_stream
import os
from matplotlib import pyplot as plt

if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = 'files'
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, path)
    os.chdir(filename)
    test_files = ["10stream.txt", "100stream.txt", "1000stream.txt", "10000stream.txt", "100000stream.txt"]
    relative_error_list = list()

    for file in test_files:
        data = read_to_stream(file)

        # Create Data set
        error = {}

        # Define k and epsilon
        for k in range(1, 1000):

            # Lossy Counting Algorithm
            c = LossyCounting(k)
            for elem in data:
                c.counting(elem)

            # Deterministic Counting Algorithm
            deterministic_counter = DeterministicAlgorithm()
            deterministic_counter.count(data)

            # Relative error Algorithm
            relative_error = RelativeError()
            relative_error.relative_error(c.get_counters(), deterministic_counter.get_counters())
            error[k] = relative_error.avg_error()

        relative_error_list.append(error)

# Plot results

plt.figure(1)
plt.plot(list(relative_error_list[0].keys()), list(relative_error_list[0].values()), c='red', label="10 characters")
plt.plot(list(relative_error_list[1].keys()), list(relative_error_list[1].values()), c='green', label="100 characters")
plt.plot(list(relative_error_list[2].keys()), list(relative_error_list[2].values()), c='blue', label="1000 characters")
plt.plot(list(relative_error_list[3].keys()), list(relative_error_list[3].values()), label="10000 characters"
         , c='brown')
plt.plot(list(relative_error_list[4].keys()), list(relative_error_list[4].values()), c='black'
         , label="100000 characters")


plt.xlabel('Value of k', fontsize=16)
plt.ylabel('Relative Error', fontsize=16)
plt.legend()
plt.show()

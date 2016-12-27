"""
Created on 23/12/2016

@author: Jorge Miguel Ferreira da Silva
"""


class DeterministicAlgorithm(object):
    """
    DeterministicAlgorithm class is a class that counts the exact values of the "stream" in order to determine the error
    """

    def __init__(self):
        """
        Constructor
        """
        self.counter = {}

    def count(self, stream):
        for st in stream:
            if st not in self.counter:
                self.counter[st] = 1
            else:
                self.counter[st] += 1

    def get_counters(self):
        return self.counter

    def __str__(self):
        var = str('Deterministic Counters')
        for key, value in self.counter.items():
            var += str('\n' + str(key) + ' : ' + str(value))
        print(var)

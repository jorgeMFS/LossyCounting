"""
Created on 23/12/2016

@author: Jorge Miguel Ferreira da Silva
"""


class RelativeError(object):
    """
    RelativeError Class is a class designed to determine the relative error of the LossyCounting Algorithm
    """

    def __init__(self):
        """
        RelativeError Constructor
        """
        self.error = {}

    def relative_error(self, lossy_counters, deterministic_counters):
        for a in deterministic_counters:
            if a in lossy_counters:
                self.error[a] = abs(deterministic_counters[a] - lossy_counters[a]) / deterministic_counters[a]
            else:
                self.error[a] = deterministic_counters[a] / deterministic_counters[a]

    def get_error(self):
        return self.error

    def avg_error(self):
        c = 0
        sm = 0
        for a in self.error:
            sm += self.error[a]
            c += 1
        return sm / c

    def __str__(self):
        var = str('Relative Error')
        for key, value in self.error.items():
            var += str('\n' + str(key) + ' : ' + str(value))
        print(var)

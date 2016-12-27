"""
Created on 21/12/2016

@author: Jorge Miguel Ferreira da Silva
"""


class LossyCounting(object):
    """
    LossyCounting is a python class that applies the algorithm Lossy Counting in G. S. Manku.
    Frequency counts over data streams.
    http://www.cse.ust.hk/vldb2002/VLDB2002-proceedings/slides/S10P03slides.pdf, 2002.
    """

    def __init__(self, k):
        """
        LossyCounting Constructor
        """

        self.n = 0
        self.T = list()  # elements considered
        self.delta = 0
        self.counter = {}
        self.k = k

    def get_counters(self):
        return self.counter

    def trim(self):
        self.delta = int(self.ratio())
        for j in self.T:
            if self.counter[j] < self.delta:
                self.T.remove(j)

    def ratio(self):
        return self.n // self.k

    def counting(self, e):

        self.n += 1
        if e in self.T:
            self.counter[e] += 1
        else:
            self.T.append(e)
            self.counter[e] = 1 + self.delta

        if self.ratio() != self.delta:
            self.trim()

    def get_epsilon(self):
        return 1 / self.k

    def __str__(self):
        var = str('Counters')
        for key, value in self.counter.items():
            var += str('\n' + str(key) + ' : ' + str(value))
        print(var)

    def apply_threshold(self, threshold_count):

        assert threshold_count > self.get_epsilon() * self.n, "too small threshold"

        self.trim()
        for elem in self.counter:
            if self.counter[elem] >= threshold_count - self.get_epsilon() * self.n:
                yield [elem, self.counter[elem]]

    def threshold_rate(self, threshold_rate):
        return self.apply_threshold(threshold_rate * self.n)

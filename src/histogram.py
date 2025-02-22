
class Histogram(object):

    def __init__(self, interval_nb, range_min=0, range_max=1):
        self.interval_nb = interval_nb
        self.interval_width = (range_max - range_min) / self.interval_nb
        self.range_min = range_min
        self.range_max = range_max

    def create(self, data):
        hist = [0] * self.interval_nb

        for value in data:
            index = int((value - self.range_min) / self.interval_width)
            if index >= self.interval_nb:
                index = -1

            hist[index] += 1

        return hist
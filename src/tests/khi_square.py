
class KhiSquareTest(object):

    def __init__(self, hist1: [], hist2: []):
        self.hist1 = hist1
        self.hist2 = hist2

    def run(self):
        chi_square = 0
        for o, e in zip(self.hist1, self.hist2):
            if e>0:
                chi_square += (o-e)**2/e

        return chi_square
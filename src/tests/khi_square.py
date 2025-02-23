
class KhiSquareTest(object):

    def from_histograms(self, hist1: [], hist2: []):
        return self.__chi_square_stat(hist2, hist1)

    def from_distribution(self, hist: []):
        interval_nb = len(hist) #compute histogram bins
        total_obs = sum(hist)
        p_i = 1 / interval_nb #proba théorique, loi uniforme
        expected = [total_obs * p_i] * interval_nb

        return self.__chi_square_stat(hist, expected)

    def __chi_square_stat(self, hist, expected):
        chi_square = 0
        for o, e in zip(hist, expected):
            if e > 0:
                chi_square += (o - e) ** 2 / e
        return chi_square
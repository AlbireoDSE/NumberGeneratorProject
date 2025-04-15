class Calculator:

    @staticmethod
    def stirling_number(k, r):
        if k == r == 0:
            return 1
        if k == r or r == 1:
            return 1
        if k == 0 or r == 0 or r > k:
            return 0
        return Calculator.stirling_number(k - 1, r - 1) + r * Calculator.stirling_number(k - 1, r)

    @staticmethod
    def harmonic_number(k):
        """Compute the k-th harmonic number H_k = sum(1/i) pour i de 1 à k"""
        return sum(1 / i for i in range(1, k + 1))

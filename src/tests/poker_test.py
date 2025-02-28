from collections import defaultdict, Counter


class PokerTest:

    @staticmethod
    def count_values(fs: str) -> dict:
        dict = defaultdict(int)
        for n in fs:
            if n not in dict:
                dict[n]
            dict[n] += 1
        return dict

    @staticmethod
    def stirling_number(k, r):
        if k == r or r == 1:
            return 1
        return PokerTest.stirling_number(k - 1, r - 1) + r * PokerTest.stirling_number(k - 1, r)


    @staticmethod
    def run(sample, k=5, d=10):
        formatted_samples = [str(int(val * (10**k))).zfill(k) for val in sample]

        categories = {"Poker": 0, "Square": 0, "Full House": 0, "Brelan": 0, "Two Pairs": 0, "One Pair": 0, "All diff": 0}

        for number in formatted_samples:
            counts = Counter(number)
            counts = sorted(counts.values(), reverse=True)
            print(counts)

            if counts == [5]:
                categories["Poker"] += 1  # Poker
            elif counts == [4, 1]:
                categories["Square"] += 1  # Carré
            elif counts == [3, 2]:
                categories["Full House"] += 1  # Full House
            elif counts == [3, 1, 1]:
                categories["Brelan"] += 1  # Brelan
            elif counts == [2, 2, 1]:
                categories["Two Pairs"] += 1  # Deux Paires
            elif counts == [2, 1, 1, 1]:
                categories["One Pair"] += 1  # Une Paire
            else:
                categories["All diff"] += 1  # Toutes différentes






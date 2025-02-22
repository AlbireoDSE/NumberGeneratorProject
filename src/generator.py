from mpmath import mp


def remarkable_generator(dps_number: int, num_decimals: int = 10):
    """
    Générateur de nombres uniformes dans [0, 1[
    basé sur les décimales de e.

    :param dps_number: Nombre de décimales de e à calculer
    :param num_decimals: Nombre de décimales utilisées pour chaque nombre généré
    """
    mp.dps = dps_number
    e_str = str(mp.e).replace('.', '')
    index = 0
    while True:
        fraction = int(e_str[index:index + num_decimals]) / (10 ** num_decimals)
        index = (index + num_decimals) % (len(e_str) - num_decimals)
        yield fraction


# Exemple d'utilisation
generator = remarkable_generator(2000000, 15)
for _ in range(10):
    print(next(generator))


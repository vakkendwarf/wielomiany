def horner(x, *arguments):

        """
        horner(dwumian, 1szy czynnik wielomianu, 2gi czynnik, 3ci czynnik ... n czynnik)

        Zwraca różnicę dwumianu i wielomianu.
        """
        result = 0
        for coefficient in arguments:
            result = result * x + coefficient
        return result

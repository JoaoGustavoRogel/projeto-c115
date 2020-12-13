import random


class Sensor:
    def __init__(self, name, bounds, integer=False, gauss=False, mean=None, sigma=None):
        self.__name = name
        self.__bounds = bounds
        self.__integer = integer
        self.__gaus = gauss
        self.__mean = mean
        self.__sigma = sigma

    def get_name(self):
        return self.__name

    def read_value(self):
        value = None

        if self.__integer:
            value = random.randint(self.__bounds[0], self.__bounds[1])
        elif self.__gaus:
            value = random.gauss(self.__mean, self.__sigma)
        else:
            value = random.uniform(self.__bounds[0], self.__bounds[1])

        return value

from random import choice, randint
from string import ascii_letters


class StringManager:

    @staticmethod
    def str_rnd(length: int):
        return ''.join(choice(ascii_letters) for _ in range(length))

    @staticmethod
    def num_rnd(length: int):
        return ''.join([str(randint(0, 9)) for _ in range(length)])

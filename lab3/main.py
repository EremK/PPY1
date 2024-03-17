# Task 1
squares_list = [x ** 2 for x in range(1, 11)]
print(squares_list)


# Task 2
def e_squares(start, end):
    return [x ** 2 for x in range(start, end)]


print(e_squares(3, 15))


# Task 3
class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        return [x ** 2 for x in range(start, end)]


# Task 4
import math

list1 = SquareGenerator.e_squares(1, 11)
list2 = [math.pow(x, 2) for x in list1]

print(list2)


# Task 5
class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        if start > end:
            raise ValueError("Start index must be smaller than the end one.")
        return [x ** 2 for x in range(start, end)]


# Task 6
from square_generator import SquareGenerator

try:
    print(SquareGenerator.e_squares(5, 21))
except ValueError as e:
    print(e)

# Task 7
from square_generator.square_generator import SquareGenerator

try:
    print(SquareGenerator.e_squares(5, 21))
except ValueError as e:
    print(e)


# Task 8
class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_cubes(start, end):
        if start > end:
            raise ValueError("Start index must be smaller than the end one.")
        return [x ** 3 for x in range(start, end)]


print(CubicGenerator.e_cubes(1, 11))

# Task 9
class CubicGenerator(SquareGenerator):
    @staticmethod
    def e_squares(start, end):
        if start > end:
            raise ValueError("Start index must be smaller than the end one.")
        return [x ** 2 for x in range(start, end)]


# Task 10
from abc import ABC, abstractmethod


class SquareGenerator(ABC):

    @abstractmethod
    def gen_squares(self, start, end):
        pass


class CubicGenerator(SquareGenerator):

    def gen_squares(self, start, end):
        if start > end:
            raise ValueError("Start index must be smaller than the end one.")
        return [x ** 3 for x in range(start, end)]

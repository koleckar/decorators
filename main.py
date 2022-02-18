from typing import List

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s',
                    handlers=[RotatingFileHandler('pointsLog.log', maxBytes=1000, backupCount=10)],
                    level=logging.INFO)


# def validator(f):
#     def wrapper(*args, **kwargs):
#         ...  # kwargs.get('')
#
#
# def printer(f):
#     print("hi")
#     f()
#     print("done")
#
#
# @printer
# def f():
#     print("yo")


def integer_input_check(f):
    def wrapper(self, x):
        if not isinstance(x, int):
            raise ValueError(f'<class \'int\'> input needed! But type {type(x)} was passed.')
        f(self, x)

    return wrapper


class Points:
    def __init__(self):
        self.__points: List[int] = []
        self.x: List[int] = []
        logging.info(f'Points init.')

    def __repr__(self):
        return f'I contain these points:{self.__points}'

    @integer_input_check
    def append_point(self, x):
        self.points_list.append(x)

    def print_points(self):
        for point in self.points_list:
            print(f"point:{point} printed")

    @property
    def points_list(self):
        return self.__points

    @points_list.setter
    def points_list(self, new_points):
        self.__points = new_points


if __name__ == '__main__':
    t1 = Points()
    t2 = Points()

    t2.print_points()
    t1.x.append(1)
    t1.points_list = [10]
    t2.print_points()
    print(t1.x)

    #
    # try:
    #     t.append_point(-1.0)
    # except ValueError as ve:
    #     print(repr(ve), file=sys.stderr)
    #
    # points = t.points_list
    #
    # t.points_list = [12, 3, 3]
    #
    # t.print_points()
    #
    # print(repr(t))

import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def evenorno(value):
    if (value == "True"):
        print("Парні числа:")
        for figure in range(100):
            if figure %2 == 0:
                print(figure)
    else:
            print("\n Не парні числа:")
            for figure in range(100):
                if figure %2 == 1:
                    print(figure)
evenorno("True")
evenorno("False")
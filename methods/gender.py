from random import randint

from methods.locale import LOCALE


def gender():
    if LOCALE == 'fa_IR':
        return 'مرد' if randint(0, 10) % 2 else 'زن'
    else:
        return 'male' if randint(0, 10) % 2 else 'female'

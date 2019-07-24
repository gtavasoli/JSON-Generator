from faker import Faker

from methods.locale import LOCALE


def first_name():
    fake = Faker(LOCALE)
    return fake.first_name()

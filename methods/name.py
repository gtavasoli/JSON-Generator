from faker import Faker

from methods.locale import LOCALE


def name():
    fake = Faker(LOCALE)
    return fake.name()

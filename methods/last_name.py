from faker import Faker

from methods.locale import LOCALE


def last_name():
    fake = Faker(LOCALE)
    return fake.last_name()

from faker import Faker

from methods.locale import LOCALE


def city():
    fake = Faker(LOCALE)
    return fake.city()

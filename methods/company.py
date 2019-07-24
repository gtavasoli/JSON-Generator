from faker import Faker

from methods.locale import LOCALE


def company():
    fake = Faker(LOCALE)
    return fake.company()
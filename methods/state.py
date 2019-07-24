from faker import Faker

from methods.locale import LOCALE


def state():
    fake = Faker(LOCALE)
    return fake.state()

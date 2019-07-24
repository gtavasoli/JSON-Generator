from faker import Faker

from methods.locale import LOCALE


def email():
    fake = Faker(LOCALE)
    return fake.email()
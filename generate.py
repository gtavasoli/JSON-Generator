import binascii
import json
import os
import random
import time
import uuid

from faker import Faker
import re
import random_object_id

schema = [
    '{{repeat(1)}}',
    {
        "_id": '{{object_id()}}',
        'guid': '{{guid()}}',
        'isActive': '{{bool()}}',
        'eyeColor': '{{choice(["blue", "brown", "green"])}}',
        'balance': '{{floating(1000, 4000, 2)}}',
        'picture': 'http://placehold.it/32x32',
        'age': '{{integer(20, 30)}}',
        'name': '{{name()}}',
        'city': '{{city()}}',
        'state': '{{state()}}',
        'gender': '{{gender()}}',
        'company': '{{company().upper()}}',
        'email': '{{email()}}',
        'phone': '{{phone()}}',
        'latitude': '{{floating(-90.000001, 90)}}',
        'longitude': '{{floating(-180.000001, 180)}}',
        'tags': [
            '{{repeat(3, 7)}}',
            '{{last_name()}}'
        ],
        'friends': [
            '{{repeat(3)}}',
            {
                'id': '{{integer()}}',
                'name': '{{name()}}'
            }
        ]
    }]


def generate(schema):
    if type(schema) == dict:
        obj = {}
        for i in schema.keys():
            obj[i] = generate(schema[i])
        return obj

    if type(schema) == list:
        s = schema[0].find('(') + 1
        e = schema[0].find(')')
        rng = schema[0][s:e].replace(' ', '').split(',')
        if len(rng) > 1:
            repeat = random.randint(int(rng[0]), int(rng[1]))
        else:
            repeat = int(rng[0])
        lst = []
        for i in range(0, repeat):
            lst.append(generate(schema[1]))
        return lst

    if type(schema) == str:
        regex = r"^\{{2}.+\(.*\)\}{2}$"
        matches = re.match(regex, schema)
        if matches is not None:
            k = schema.find('(')
            mod = __import__('methods.' + schema[2:k])
            return eval('mod.{}.{}'.format(schema[2:k], schema[2:-2]))
        else:
            return schema


if __name__ == '__main__':
    # print(generate(schema))
    print(json.dumps(generate(schema), indent=4, sort_keys=True))

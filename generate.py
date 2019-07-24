import binascii
import json
import os
import random
import time
import uuid

from faker import Faker
import re
import random_object_id

schema = {
    "_id": '{{objectId()}}',
    'index': '{{index()}}',
    'guid': '{{guid()}}',
    'isActive': '{{bool()}}',
    'balance': '{{floating(1000, 4000, 2)}}',
    'picture': 'http://placehold.it/32x32',
    'age': '{{integer(20, 40)}}',
    'name': '{{name()}}',
    'gender': '{{gender()}}',
    'company': '{{company().upper()}}',
    'email': '{{email()}}',
    'phone': '{{phone()}}',
}


def generate(schema):
    if type(schema) == dict:
        obj = {}
        for i in schema.keys():
            obj[i] = generate(schema[i])
        return obj
    elif type(schema) == str:
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

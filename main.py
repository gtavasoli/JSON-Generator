import json
import unittest

from generate import generate

template = [
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

if __name__ == '__main__':
    print(json.dumps(generate(template), indent=4, sort_keys=True))

import random

import re


def generate(template):
    if type(template) == dict:
        obj = {}
        for i in template.keys():
            obj[i] = generate(template[i])
        return obj

    if type(template) == list:
        s = template[0].find('(') + 1
        e = template[0].find(')')
        rng = template[0][s:e].replace(' ', '').split(',')
        if len(rng) > 1:
            repeat = random.randint(int(rng[0]), int(rng[1]))
        else:
            repeat = int(rng[0])
        lst = []
        for i in range(0, repeat):
            lst.append(generate(template[1]))
        return lst

    if type(template) == str:
        regex = r"^\{{2}.+\(.*\)\}{2}$"
        matches = re.match(regex, template)
        if matches is not None:
            k = template.find('(')
            mod = __import__('methods.' + template[2:k])
            return eval('mod.{}.{}'.format(template[2:k], template[2:-2]))
        else:
            return template

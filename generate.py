import random

import re


def generate(template):
    if type(template) == dict:
        obj = {}
        for i in template.keys():
            obj[i] = generate(template[i])
        return obj

    if type(template) == list:
        lst = []
        it = iter(template)
        while True:
            r = next(it, None)
            if r is None:
                break
            if type(r) == str:
                regex = r"^\{\{repeat\(\s*\d+\s*,{0,1}\s*\d*\s*\)\}\}$"
                matches = re.match(regex, r)
                if matches is not None:  # Repeat
                    s = template[0].find('(') + 1
                    e = template[0].find(')')
                    rng = template[0][s:e].replace(' ', '').split(',')
                    if len(rng) > 1:
                        repeat = random.randint(int(rng[0]), int(rng[1]))
                    else:
                        repeat = int(rng[0])
                    r = next(it, None)  # Repeat it
                    if r is None:
                        break
                    for i in range(0, repeat):
                        lst.append(generate(r))
                else:
                    lst.append(generate(r))
            else:
                lst.append(generate(r))
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

import json

from generate import generate

if __name__ == '__main__':
    with open('./templates/sample_1.json', 'r') as f:
        s = f.read()
        template = json.loads(s)
        print(json.dumps(generate(template), indent=4))

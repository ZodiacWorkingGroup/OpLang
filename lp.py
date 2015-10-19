from AST import *
from re import *
from sys import stdout
from io import TextIOWrapper

stdout = TextIOWrapper(sys.stdout.detach(), sys.stdout.encoding, 'replace')  # Unicode support (for ? character)

def lp(script):
    script = script.split(';')

    for i in range(len(script)):
        script[i] = script[i].strip()

    parsed = []
    for com in script:
        if compile(r'[^a-zA-Z0-9_][a-zA-Z0-9_]*').match(com):
            parsed.append(com[0], com[1:])

        elif compile(r'[a-zA-Z0-9_]*[^a-zA-Z0-9_]').match(com):
            parsed.append(com[-1], com[:-1])

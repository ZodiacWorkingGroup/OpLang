from AST import *
from re import *
import sys
from string import ascii_letters, digits
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), sys.stdout.encoding, 'replace')  # Unicode support (for ? character)


class LexingException(Exception):
    pass


def lp(script):
    script = script.split(';')
    if script[-1] != '':
        raise LexingException('No semicolon termination')
    script = script[:-1]

    for i in range(len(script)):
        script[i] = script[i].strip()

    parsed = []
    for com in script:
        if compile(r'^[^a-zA-Z0-9_][a-zA-Z0-9_]*$').match(com):
            parsed.append(Prefix(com[0], com[1:]))

        elif compile(r'^[a-zA-Z0-9_]*[^a-zA-Z0-9_]$').match(com):
            parsed.append(Postfix(com[-1], com[:-1]))

        elif compile(r'^[a-zA-Z0-9_]*[^a-zA-Z0-9_][a-zA-Z0-9_]*$').match(com):
            char = ''
            i = 0
            while char in ascii_letters+digits+'_':
                i += 1
                char = com[i]
            parsed.append(Infix(com[i], com[:i], com[i+1:]))
        else:
            raise LexingException('Invalid line encontered: '+com)
    return parsed

print(lp(input()))
class Prefix:
    def __init__(self, op, lhs):
        self.op = op
        self.lhs = lhs
        

class Postfix:
    def __init__(self, op, rhs):
        self.op = op
        self.rhs = rhs
        

class Infix:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
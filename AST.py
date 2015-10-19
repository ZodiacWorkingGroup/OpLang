class Nofix:
    def __init__(self, op):
        self.op = op

    def __repr__(self):
        return self.op


class Prefix:
    def __init__(self, op, rhs):
        self.op = op
        self.rhs = rhs

    def __repr__(self):
        return self.op+self.rhs
        

class Postfix:
    def __init__(self, op, lhs):
        self.op = op
        self.lhs = lhs

    def __repr__(self):
        return self.lhs+self.op
        

class Infix:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return self.lhs+self.op+self.rhs
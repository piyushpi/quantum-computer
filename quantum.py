class qubit:
    """
    Class or a struct in C, for the quantum bits.
    Updated 23rd February 2022.
    """
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one

    def printQubit(self):
        print(self.zero, self.one)

def printQubit(q):
    print(q.zero, q.one)
    
def X(q):
    n = qubit(0*q.zero + 1*q.one, 1*q.zero + 0*q.one)

    return n

q = qubit(1,0)
b = qubit(1,0)
c = qubit(0.5,0.5)

q.printQubit()
c.printQubit()

printQubit(X(q))
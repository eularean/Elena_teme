"""
Tema5 - 30% din nota finala
Moditicati acest iterator astfel incat sa genereze urmatorul numar prim doar atunci cand
este apelata functia next() pe obiectul de tip 'PrimesIter' si nu toate numerele prime atunci cand se instantiaza
Aveti un indiciu cu o geseala mai jos si va trebui sa modificati si constructorul
"""

from time import time


class PrimesIter():
    """"
        O clasa care calculeaza urmatorul numar prim
        ...
        Atributes
        -------------
        max_prime : int
            numarul max pana la care sa calculeze numerele prime
    """
    def __init__(self, max_prime):
        """ Parameters
            -------
            max_prime : int
                numarul max pana la care se calculeaze numerele prime
        """
        self.max_prime = max_prime
        self.start = 1
        self.primes = []
    def __next__(self):
        """
        functie care calculeaza si returneaza urmatorul numar prim cand este apaelata
        :return:int
            reprezinta urmatorul numar prim
        """
        for x in range(self.start, self.max_prime):
            if x == 2:
                self.start = x + 1
                return (f"next prime number {x}")
            else:
                for y in range(2, x):
                    if x % y == 0:
                        break
                    else:
                        self.start = x + 1
                        return x
    def __iter__(self):
        """
        :return: self
            avem nevoie pentru ca e un iterator
        """
        return self

help(PrimesIter)
start = time()
prime = PrimesIter(300000)
stop = time()
assert (stop < start + 1)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))

print(__doc__)

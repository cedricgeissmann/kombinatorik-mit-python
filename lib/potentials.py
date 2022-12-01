from sympy import *
from random import randint, sample, choice


class Exercise:
    def __init__(self, sol=None):
        self.sol = sol # will be set in generate_solution, which is called from generate_exercise
        self.expr = self.generate_exercise()

    def check_solution(self, solution):
        if simplify(solution) == simplify(self.sol):
            display("RICHTIG!!!")
        else:
            display("Leider falsch...", solution, "ist nicht gleich", self.expr)

    def generate_exercise(self):
        if self.sol:
            expr = self.sol
        else:
            expr = self.generate_solution()
        for _ in range(5):
            for _ in range(5):
                expr = expand(expr)
            expr = shrink(expr)
        display("Vereinfache diesen Ausdruck: ", expr)
        return expr

    def generate_solution(self):
        self.sol = Mul(*(create_random_term(nom_lower=1, nom_upper=7, denom_lower=1, denom_upper=1) for _ in range(3)))
        return self.sol

def create_random_term(nom_lower=-5, nom_upper=5, denom_lower=-5, denom_upper=5):
    nom = randint(nom_lower, nom_upper)
    while nom == 0:
        nom = randint(nom_lower, nom_upper)
    denom = randint(denom_lower, denom_upper)
    while denom == 0:
        denom = randint(denom_lower, denom_upper)

    base = choice(symbols("a b c d e f"))
    return Pow(base, Rational(nom, denom))

def term(t):
    return sympify(t, evaluate=False)

def expand(expr):
    ex = create_random_term()
    rand = randint(0,1)
    if rand == 0:
        return Mul(expr, UnevaluatedExpr(ex) / ex)
    elif rand == 1:
        return Mul(expr, ex / UnevaluatedExpr(ex))
    else:
        return Mul(expr, UnevaluatedExpr(ex) / UnevaluatedExpr(ex))

def shrink(expr):
    lower_bound = 3 # sets the bound for the minimum number of elements to be simplified
    upper_bound = 2 # sets the bound for the maximum number of elements to be simplified
    tup = tuple(sample(expr.args, len(expr.args)))
    bound = randint(lower_bound, max(lower_bound, len(tup) - upper_bound))
    first = tup[:bound]
    last = tup[bound:]

    first = simplify(Mul(*first))

    return Mul(first, Mul(*last, evaluate=False), evaluate=False)
import graphviz
from itertools import product
from fractions import Fraction

def repeat(li, times):
    return [li for _ in range(times)]

def _const_node(depth, tup):
    if depth < 0: return ""
    res = ""
    for i in range(depth+1):
        if i > 0:
            res += ","
        res += f"{tup[i]}"
    return res

def _count_levels(Z):
    counter = {}
    for tup in Z:
        for i in range(len(tup)):
            try:
                counter[i].add(tup[i:i+1])
            except(KeyError):
                counter[i] = set()
                counter[i].add(tup[i:i+1])
    return counter

def construct_tree(Z, engine="dot"):
    """
    Erstelle einen Baum aus einem Zustandsraum.

    Es werden folgende Annahmen getroffen:
     - Der Baum hat so viele Ebenen wie es Stellen in einem Ergebnis hat.
     - Die Reihenfolge der Stellen im Ergebnis entsprechen der Reihenfolge der Ebenen im Baum.
     - Stellen im Ergebis haben einen eindeutigen Namen (es gibt keine Duplikate).
     - Alle Kinder eines Knotens sind gleich wahrscheinlich.
    """
    levels_count = _count_levels(Z)
    d = graphviz.Digraph(strict=True, engine=engine)
    for tup in Z:
        for i in range(len(tup)):
            n1 = _const_node(i - 1, tup)
            n2 = _const_node(i, tup)
            if levels_count:
                d.edge(n1, n2, f"1/{len(levels_count[i])}")
            else:
                d.edge(n1, n2)
    return d
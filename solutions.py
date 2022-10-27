def solution_aufgabe_01(callback):
    assert callback(1, 2) == 3
    print("Aufgabe richtig!")


def sol_aufgabe_15(callback):
    for (a, b, c, expect) in [
        (3, 4, 2, 3 * 4 * 2),
        (5, 2, 3, 5 * 2 * 3),
        (8, 7, 1, 8 * 7),
        (13, 4, 3, 13 * 4 * 3),
    ]:
        res = callback(a, b, c)
        if res != expect:
            print(f"Es ist ein Fehler aufgetretten!!!")
            print(f"Für {a}, {b} und {c} wird {expect} erwartet, nicht {res}")
            return
    print("Alles richtig!!!")


def sol_aufgabe_16(callback):
    for (a, b, c) in [
        (12, 4, 20736),
        (2, 6, 64),
        (13, 5, 371293),
        (26, 5, 11881376),
        (52, 5, 380204032),
    ]:
        res = callback(a, b)
        if res != c:
            print(f"Es ist ein Fehler aufgetretten!!!")
            print(f"Für {a} und {b} wird {c} erwartet, nicht {res}")
            return
    print("Alles richtig!!!")


def sol_aufgabe_17(callback):
    for (a, b, c, expect) in [
        (25, 9, 10, 25**2 * 9 * 10),
        (13, 9, 10, 13**2 * 9 * 10),
        (50, 3, 10, 50**2 * 3 * 10),
        (26, 10, 10, 26**2 * 10 * 10),
    ]:
        res = callback(a, b, c)
        if res != expect:
            print(f"Es ist ein Fehler aufgetretten!!!")
            print(f"Für {a}, {b} und {c} wird {expect} erwartet, nicht {res}")
            return
    print("Alles richtig!!!")


def sol_aufgabe_18(callback):
    for (a, expect) in [
        (25, 25 * (25 - 1) / 2),
        (12, 12 * (12 - 1) / 2),
        (31, 31 * (31 - 1) / 2),
        (5, 5 * (5 - 1) / 2),
        (3, 3 * (3 - 1) / 2),
        (250, 250 * (250 - 1) / 2),
    ]:
        res = callback(a)
        if res != expect:
            print(f"Es ist ein Fehler aufgetretten!!!")
            print(f"Für {a} wird {expect} erwartet, nicht {res}")
            return
    print("Alles richtig!!!")


def sol_aufgabe_19(callback):
    for (a, expect) in [
        (
            ["A", "R", "M", "O"],
            (
                24,
                [
                    ("A", "M", "O", "R"),
                    ("A", "M", "R", "O"),
                    ("A", "O", "M", "R"),
                    ("A", "O", "R", "M"),
                    ("A", "R", "M", "O"),
                    ("A", "R", "O", "M"),
                    ("M", "A", "O", "R"),
                    ("M", "A", "R", "O"),
                    ("M", "O", "A", "R"),
                    ("M", "O", "R", "A"),
                    ("M", "R", "A", "O"),
                    ("M", "R", "O", "A"),
                    ("O", "A", "M", "R"),
                    ("O", "A", "R", "M"),
                    ("O", "M", "A", "R"),
                    ("O", "M", "R", "A"),
                    ("O", "R", "A", "M"),
                    ("O", "R", "M", "A"),
                    ("R", "A", "M", "O"),
                    ("R", "A", "O", "M"),
                    ("R", "M", "A", "O"),
                    ("R", "M", "O", "A"),
                    ("R", "O", "A", "M"),
                    ("R", "O", "M", "A"),
                ],
            ),
        ),
    ]:
        res = callback(a)
        if res != expect:
            print(f"Es ist ein Fehler aufgetretten!!!")
            print(f"Für {a} wird {expect} erwartet, nicht {res}")
            return
    print("Alles richtig!!!")

# ABO: compatibilidad simple SIN and/or/not/listas/booleanos (usa flags 0/1 y if anidados)
print("Introduce dos grupos ABO (O, A, B, AB)")
g1 = input("Grupo 1: ").upper()
g2 = input("Grupo 2: ").upper()

comp = 0

# g1 dona a g2
dona12 = 0
t = 0
if g2 == "O":
    t = 1
if t == 0:
    if g2 == "A":
        t = 1
if t == 0:
    if g2 == "B":
        t = 1
if t == 0:
    if g2 == "AB":
        t = 1

if g1 == "O":
    if t == 1:
        dona12 = 1
else:
    if g1 == "A":
        u = 0
        if g2 == "A":
            u = 1
        if u == 0:
            if g2 == "AB":
                u = 1
        if u == 1:
            dona12 = 1
    else:
        if g1 == "B":
            v = 0
            if g2 == "B":
                v = 1
            if v == 0:
                if g2 == "AB":
                    v = 1
            if v == 1:
                dona12 = 1
        else:
            if g1 == "AB":
                if g2 == "AB":
                    dona12 = 1

if dona12 == 1:
    print(g1, "dona a", g2, "(compatible)")
    comp = 1

# g2 dona a g1
dona21 = 0
t = 0
if g1 == "O":
    t = 1
if t == 0:
    if g1 == "A":
        t = 1
if t == 0:
    if g1 == "B":
        t = 1
if t == 0:
    if g1 == "AB":
        t = 1

if g2 == "O":
    if t == 1:
        dona21 = 1
else:
    if g2 == "A":
        u = 0
        if g1 == "A":
            u = 1
        if u == 0:
            if g1 == "AB":
                u = 1
        if u == 1:
            dona21 = 1
    else:
        if g2 == "B":
            v = 0
            if g1 == "B":
                v = 1
            if v == 0:
                if g1 == "AB":
                    v = 1
            if v == 1:
                dona21 = 1
        else:
            if g2 == "AB":
                if g1 == "AB":
                    dona21 = 1

if dona21 == 1:
    print(g2, "dona a", g1, "(compatible)")
    comp = 1

if comp == 0:
    print("No son compatibles")

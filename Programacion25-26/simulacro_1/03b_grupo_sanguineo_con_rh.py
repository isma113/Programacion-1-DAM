# ABO + Rh SIN and/or/not/listas/booleanos
print("Introduce dos grupos con Rh (ej: O-, A+, AB-, B+)")
x1 = input("Grupo 1: ").upper()
x2 = input("Grupo 2: ").upper()

abo1 = x1[:-1]
rh1 = x1[-1:]
abo2 = x2[:-1]
rh2 = x2[-1:]

# ABO 1->2
abo12 = 0
if abo1 == "O":
    t = 0
    if abo2 == "O":
        t = 1
    if t == 0:
        if abo2 == "A":
            t = 1
    if t == 0:
        if abo2 == "B":
            t = 1
    if t == 0:
        if abo2 == "AB":
            t = 1
    if t == 1:
        abo12 = 1
else:
    if abo1 == "A":
        t = 0
        if abo2 == "A":
            t = 1
        if t == 0:
            if abo2 == "AB":
                t = 1
        if t == 1:
            abo12 = 1
    else:
        if abo1 == "B":
            t = 0
            if abo2 == "B":
                t = 1
            if t == 0:
                if abo2 == "AB":
                    t = 1
            if t == 1:
                abo12 = 1
        else:
            if abo1 == "AB":
                if abo2 == "AB":
                    abo12 = 1

# ABO 2->1
abo21 = 0
if abo2 == "O":
    t = 0
    if abo1 == "O":
        t = 1
    if t == 0:
        if abo1 == "A":
            t = 1
    if t == 0:
        if abo1 == "B":
            t = 1
    if t == 0:
        if abo1 == "AB":
            t = 1
    if t == 1:
        abo21 = 1
else:
    if abo2 == "A":
        t = 0
        if abo1 == "A":
            t = 1
        if t == 0:
            if abo1 == "AB":
                t = 1
        if t == 1:
            abo21 = 1
    else:
        if abo2 == "B":
            t = 0
            if abo1 == "B":
                t = 1
            if t == 0:
                if abo1 == "AB":
                    t = 1
            if t == 1:
                abo21 = 1
        else:
            if abo2 == "AB":
                if abo1 == "AB":
                    abo21 = 1

# RH 1->2
rh12 = 0
if rh1 == "-":
    rh12 = 1
else:
    if rh1 == "+":
        if rh2 == "+":
            rh12 = 1

# RH 2->1
rh21 = 0
if rh2 == "-":
    rh21 = 1
else:
    if rh2 == "+":
        if rh1 == "+":
            rh21 = 1

comp = 0
if abo12 == 1:
    if rh12 == 1:
        print(x1, "dona a", x2, "(compatible)")
        comp = 1
if abo21 == 1:
    if rh21 == 1:
        print(x2, "dona a", x1, "(compatible)")
        comp = 1
if comp == 0:
    print("No son compatibles")

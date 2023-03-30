import random

def valasz_beker(prompt, helyes):
    valasz = input(prompt)
    if valasz == helyes:
        print("Helyes válasz!")
        return True
    else:
        print(f"Rossz válasz! A helyes válasz: {helyes}")
        return False

vertanuk = []
with open("nem_vertanu.txt", "r", encoding="utf-8") as f:
    for line in f:
        vertanuk.append(line.strip())

#print(len(vertanuk)
igazi_vertanuk = []
mondatok = {}
with open("utolso_mondatok.txt", "r", encoding="ansi") as f:
    for line in f:
        k, v = line.strip().split(":#")
        igazi_vertanuk.append(k)
        mondatok[k] = v

#print(len(mondatok))
while True:
    pontszam = 0
    # 1. feladat
    print("1. feladat")
    kamu = False
    tmp = igazi_vertanuk.copy()
    kakukktojas = random.choice(vertanuk)
    for n in range(len(tmp)):
        print(tmp.pop(random.randrange(0, len(tmp))))
        if not kamu and random.randint(0, 99) >= 80:
            print(kakukktojas)
            kamu = True

    if not kamu:
        print(kakukktojas)

    if valasz_beker("Válassza ki, melyik NEM vértanú! ", kakukktojas):
        pontszam += 1

    # 2. feladat
    print("2. feladat")
    tmp = igazi_vertanuk.copy()
    for j in range(len(igazi_vertanuk)):
        idezo = False
        k = tmp.pop(random.randrange(0, len(tmp)))
        valaszok = igazi_vertanuk.copy()
        valaszok.remove(k)
        for i in range(random.randint(4, len(valaszok))):
            if idezo:
                print(valaszok.pop(random.randrange(0, len(valaszok))))
            else:
                if random.randint(0, 99) < 80:
                    print(valaszok.pop(random.randrange(0, len(valaszok))))
                else:
                    print(k)
                    idezo = True

        if not idezo:
            print(k)

        if valasz_beker(f'Ki mondta ezt a mondatot: "{mondatok[k]}"? ', k):
            pontszam += 1

    print(f"Helyes válaszok száma: {pontszam}/{1+len(igazi_vertanuk)}")

    akar = input("Szeretne még egyet játszani? (igen / nem) ")
    if akar.lower() == "nem":
        break

print("Viszontlátásra!")

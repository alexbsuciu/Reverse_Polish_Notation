def genp(s):
    # generarea sirului polonez

    nr = []  # lista in care generam
    sm = []  # stiva pentru operatori
    pr = []  # stiva pentru tinut minte prioritatile semnelor

    for i in range(len(s)):
        if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
            nr.append(s[i])
            # daca caracterul este o litera acesta este adaugat in stiva finala
        else:
            if s[i] == ')':
                # daca caracterul este o paranteza inchisa, se goleste stiva de semne pana la paranteza deschisa si se adauga la stiva finala
                for j in range(len(sm)-1, -1, -1):
                    if sm[j] == '(':
                        sm.pop()
                        pr.pop()
                        break
                    nr.append(sm[j])
                    sm.pop()
                    pr.pop()
            else:
                # setam prioritatea semnelor
                prior = 0
                if s[i] == '-' or s[i] == "+" or s[i] == "∨":
                    prior = 1
                elif s[i] == '/' or s[i] == '*' or s[i] == "∧":
                    prior = 2
                elif s[i] == '^':
                    prior = 3
                if prior != 0:
                    while len(pr) != 0 and pr[len(pr)-1] >= prior:
                        nr.append(sm[len(sm)-1])
                        sm.pop()
                        pr.pop()
                sm.append(s[i])
                pr.append(prior)
    for i in range(len(sm)-1, -1, -1):
        nr.append(sm[i])
        # la final golim stiva de semne
    fin = ""
    fin = fin.join(nr)
    print(f"Sirul rezultat este: {fin}")


def evp(s):
    if pasi == "d":
        print("Pasi:")
    # evaluarea sirului polonez

    ec = []  # lista in care generam ecuatia
    pr = []  # stiva cu prioritati ca sa stim sa punem parantezele

    for i in range(len(s)):
        if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
            ec.append(s[i])
            pr.append(0)
            # adaugam literele in stiva
        else:
            prior = 0
            if s[i] == '-' or s[i] == "+" or s[i] == "∨":
                prior = 1
            elif s[i] == '/' or s[i] == '*' or s[i] == "∧":
                prior = 2
            elif s[i] == '^':
                prior = 3
            if pr[len(pr)-1]:
                # in caz ca exista o diferenta de prioritate se pun paranteze
                if pr[len(pr)-1] < prior or pr[len(pr)-1] == prior and s[i] == '-':
                    ec[len(ec) - 1] = '(' + ec[len(ec) - 1] + ')'
            ec[len(ec)-2] = ec[len(ec)-2] + s[i] + ec[len(ec)-1]
            ec.pop()
            pr.pop()
            pr[len(pr)-1] = prior
        if pasi == "d":
            print(ec)
    fin = ec[0]
    if pasi == "d":
        print("---------------")
    print(f"Rezultat final: {fin}")


print("Introduceti sirul:")
sir = input()

print("Alegeti optiunea: Pentru generarea sirului polonez introduceti 1, Pentru evaluarea sirului polonez 2:")
while True:
    x = int(input())
    try:
        assert x == 1 or x == 2
    except AssertionError as error:
        print("Optiune invalida, incercati din nou")
    else:
        if x == 1:
            genp(sir)
        else:
            print("Doriti sa fie afisati si pasii? Introduceti d pentru da, respectiv n pentru nu:")
            pasi = input()
            evp(sir)
        break

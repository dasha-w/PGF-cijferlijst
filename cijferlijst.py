import random


def read_cijfers(file_name):
    cijfers = {}
    with open(file_name) as file:
        for line in file:
            parts = line.strip().split(sep = ',')
            vak = parts[0]
            grade = float(parts[1])
            if vak in cijfers:
                cijfers[vak].append(grade)
            else:
                cijfers[vak] = [grade]
    return cijfers


def maak_cijferlijst(file_name):
    with open(file_name, 'w') as file:
        for i in range(10):
            file.write(f"wiskunde,{random.randint(1, 10)}\n")
            file.write(f"engels,{random.randint(1, 10)}\n")
            file.write(f"nederlands,{random.randint(1, 10)}\n")
        file.close()


def print_cijfers(scores):
    print(f'Statistieken per vak:')
    for vak, cijfer_lijst in scores.items():
        gemiddelde = sum(cijfer_lijst) / len(cijfer_lijst)
        hoogste = max(cijfer_lijst)
        laagste = min(cijfer_lijst)
        print(f'Vak: {vak}, Gemiddelde score: {gemiddelde}, Hoogste score {hoogste}, Laaste score: {laagste}')


def main():
    path = "cijferlijst.txt"
    maak_cijferlijst(path)
    scores = read_cijfers(path)
    print_cijfers(scores)


if __name__ == "__main__":
    main()

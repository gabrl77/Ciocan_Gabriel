import random
import csv
import tkinter as tk
from tkinter import messagebox
import unicodedata


def remove_diacritics(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def genereaza_cnp(sex, an, luna, zi, judet, nnn):
    S = str(sex)
    AA = str(an)[-2:]
    LL = f"{luna:02d}"
    ZZ = f"{zi:02d}"
    JJ = f"{judet:02d}"
    NNN = f"{nnn:03d}"
    cnp_partial = S + AA + LL + ZZ + JJ + NNN
    cifra_control = calcul_cifra_control(cnp_partial)
    return cnp_partial + str(cifra_control)


def calcul_cifra_control(cnp):
    constanta = "279146358279"
    suma = 0
    for i in range(12):
        suma += int(cnp[i]) * int(constanta[i])
    rest = suma % 11
    return 1 if rest == 10 else rest


def genereaza_nume():
    prenume_f = ["Maria", "Ioana", "Elena", "Ana", "Andreea"]
    prenume_m = ["Ion", "Mihai", "Andrei", "Alexandru", "George"]
    nume = ["Stoica", "Florescu", "Dobre", "Constantin", "Muntean", "Oprea", "Popescu", "Ionescu", "Pop", "Stan"]

    if random.random() > 0.5:
        full_name = random.choice(prenume_f) + " " + random.choice(nume)
    else:
        full_name = random.choice(prenume_m) + " " + random.choice(nume)

    return remove_diacritics(full_name)


def genereaza_fisier_csv():
    judete = {
        1: 9.1, 2: 6.3, 3: 5.2, 4: 6.1, 5: 4.8, 6: 4.5, 7: 5.9, 8: 7.2, 9: 6.8,
        10: 10.3, 11: 4.2, 12: 3.9, 13: 5.5, 14: 6.7, 15: 4.1, 16: 5.3, 17: 6.0,
        18: 4.9, 19: 4.4, 20: 3.8, 21: 4.0, 22: 3.7, 23: 5.1, 24: 6.2, 25: 5.8,
        26: 4.7, 27: 3.6, 28: 5.4, 29: 6.5, 30: 5.7, 31: 4.6, 32: 5.6, 33: 3.5,
        34: 4.3, 35: 6.4, 36: 5.0, 37: 6.6, 38: 3.4, 39: 4.9, 40: 3.3, 41: 6.9,
        42: 3.2
    }

    with open('cnpuri.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for _ in range(100000):
            judet = random.choices(list(judete.keys()), weights=list(judete.values()))[0]
            sex = random.choice([1, 2, 5, 6])
            an = random.randint(1901, 2024)
            luna = random.randint(1, 12)
            zi = random.randint(1, 28)
            nnn = random.randint(1, 999)
            writer.writerow([genereaza_cnp(sex, an, luna, zi, judet, nnn), genereaza_nume()])


class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, cnp):
        hash_value = 5381
        for char in cnp:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def insert(self, cnp, nume):
        self.table[self.hash_function(cnp)].append((cnp, nume))

    def search(self, cnp):
        index = self.hash_function(cnp)
        iterations = 0
        for pair in self.table[index]:
            iterations += 1
            if pair[0] == cnp:
                return pair[1], iterations
        return None, iterations


class HashTableGUI:
    def __init__(self, ht):
        self.ht = ht
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Cautare CNP")
        self.root.geometry("350x200")

        tk.Label(self.root, text="Introduceti CNP:", font=('Arial', 12)).pack(pady=5)
        self.entry = tk.Entry(self.root, font=('Arial', 12))
        self.entry.pack(pady=5)

        tk.Button(self.root, text="Cauta", command=self.cauta, font=('Arial', 12)).pack(pady=10)

        self.result = tk.Label(self.root, text="", font=('Arial', 12))
        self.result.pack()

    def cauta(self):
        cnp = self.entry.get().strip()
        if len(cnp) != 13 or not cnp.isdigit():
            messagebox.showerror("Eroare", "CNP invalid!")
            return

        nume, iterations = self.ht.search(cnp)
        if nume:
            self.result.config(text=f"Rezultat: {nume}\nIteratii necesare: {iterations}")
        else:
            self.result.config(text="CNP negasit in baza de date")

    def run(self):
        self.root.mainloop()


def main():
    genereaza_fisier_csv()
    ht = HashTable()

    with open('cnpuri.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            ht.insert(row[0], row[1])

    max_iter = 0
    with open('cnpuri.csv', 'r', encoding='utf-8') as f:
        lines = list(csv.reader(f))
        for line in random.sample(lines, min(1000, len(lines))):
            _, it = ht.search(line[0])
            if it > max_iter:
                max_iter = it

    print(f"Numar maxim de iteratii gasite: {max_iter}")
    HashTableGUI(ht).run()


if __name__ == "__main__":
    main()
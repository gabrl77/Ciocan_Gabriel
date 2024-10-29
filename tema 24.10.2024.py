meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
numar_portii = {produs[0]: 0 for produs in preturi}
initial_portii={produs[0]:  meniu.count(produs[0]) for produs in preturi}
preturii={produs[0]:produs[1] for produs in preturi}


print("Lista cu toate comenzile:")
while studenti:
    student=studenti.pop(0)
    comanda=comenzi.pop(0)
    print(f"Studentul {student} a comandat o portie puternica de {comanda}")
    istoric_comenzi.append([student,comanda])
    tavi.pop()
    while comanda in numar_portii:
       numar_portii[comanda] += 1
       break

print("\nIstoricul comenzilor:")
while istoric_comenzi:
    intrate=istoric_comenzi.pop(0)
    print(f"{intrate[0]} a comandat {intrate[1]}")

print(f"\nS-au comandat {numar_portii['guias']} guias, {numar_portii['ceafa']} cefe, {numar_portii['papanasi']} papanasi")

tavi_ramse=len(tavi)
print(f"\nMai sunt disponibile {tavi_ramse}")

papanasi_disponibil=initial_portii["papanasi"]-numar_portii["papanasi"]
print(f"\nMai exista {papanasi_disponibil} portii de papanasi.")

guias_disponibil=initial_portii['guias']-numar_portii['guias']
print(f"\nMai exista {guias_disponibil} portii de guias.")

cefe_disponibil=initial_portii["ceafa"]-numar_portii["ceafa"]
print(f"\nMai exista {cefe_disponibil} portii de ceafa.")

numar_guias=numar_portii['guias']
numar_ceafa=numar_portii['ceafa']
numar_papanasi=numar_portii['papanasi']
pret_papanasi=preturi[0][1]
pret_ceafa=preturi[1][1]
pret_guias=preturi[2][1]
pret_total=numar_guias*pret_guias+numar_ceafa*pret_ceafa+numar_papanasi*pret_papanasi
print(f"\nCantina a incasat suma superba de: {pret_total}")
print("\nPreturi pana in 7 lei")
if pret_papanasi<=7:
    print("papanasi")
if pret_ceafa<=7:
    print("ceafa")
if pret_guias<=7:
    print("guias")


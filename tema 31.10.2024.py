# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Cuvantul de ghicit:"," ".join(progres))
print(f"Incercari ramase: {incercari_ramase}")

while incercari_ramase > 0 and "_" in progres:
   litera=input("Introdu o litera:").lower()
   if len(litera)!= 1 or not litera.isalpha:
       print("Introdu o litera valida!")
       continue
   if litera in litere_incercate:
       print("Ai incercat deja aceasta litera!")
       continue

   litere_incercate.append(litera)
   if litera in cuvant_de_ghicit:
       print(f"Ai ghicit litera {litera} barosane!")
       #asta l am luat de la dvs ca nu am stiut :))
       for i in range(len(cuvant_de_ghicit)):
           if cuvant_de_ghicit[i]==litera:
               progres[i]=litera
       #---
       print("Ai un progres fenomenal de:","".join(progres))
   else:
       incercari_ramase-=1
       print(f"Litera {litera} din pacate este gresita. Mai ai doar {incercari_ramase} incercari!")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
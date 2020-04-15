# O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile masinilor produse in ziua
# respectiva (seriile sunt numere intregi (int))
# Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
# Obiectul iterat va returna loturile din care fac parte masinile din acea zi, un lot are
# 20 de masini si numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
#
#
# 1)Definire: 40p
#   - Creati o clasa pentru un obiect iterabil
# 	a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (13589, 100) 10p
# 	b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile
# 	cu volan pe stanga 15p
# 	c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
# 2) Executie: 40p
#  - Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
#  - Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
# 3) Documentatie: 20p
#  	a) adaugati type hits 5p
# 	a) documentati modulul 5p
# 	b) documentati clasele 5p
# 	c) documentati metodele 5p

#O clasa care are un constructor
#doua functii pentru masini volan stanga si dreapta
class fabricaAuto():
# initializeaza seria de inceput, volumul si creaza o lista pentru masinile cu volanul pe stanga
# si dreapta si lotul si deschide un fisier pentru a scrie in el
    def __init__(self, serie_inceput,volum):
        self.serie = serie_inceput
        self.vol = volum
        self.stanga = []
        self.dreapta = []
        self.lot = []
        self.file = open("Parcauto.txt","w")
# returneaza lista cu masinile pe dreapta
    def volan_dreapta(self):
        return self.dreapta
# returneaza lista cu masinile pe
    def volan_stanga(self):
        return self.stanga
#parcurge volumul de masini incepand cu seria introdusa , verifica daca sunt cu volan pe stanga/ dreapta si pune lista corecta si returneaza ultimul lot
    def __next__(self):
        for x in range(self.serie, self.vol+ self.serie):
            if x % 2 == 0:
                self.file.write(str(x)) # scrie in fisier masinile cu volan pe dreapta
                self.file.write("\n") #trece la urmatoarea linie in fisier
                self.dreapta.append(x) #salveaza in lista
            else:
                self.file.write(str(x))
                self.stanga.append(x)
        self.lot = int((self.vol + self.serie)/20) #aduna serie_inceput cu volum si /20 sa se afle lotul
        self.file.close() # inchide fisierul
        return self.lot

    def __iter__(self):
        return self

auto = fabricaAuto(314, 90) #creaza var care apeleaza clasa Fabrica


print(next(auto))
print(auto.volan_stanga()) #returneaza lista ptr stanga
print(auto.volan_dreapta()) # #returneaza lista ptr dreapta
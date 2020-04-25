"""O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
Seriile si loturile sunt numere intregi de tip int
Un lot este alcatuit din 20 de masini si primele 10 din lot sunt cu volan pe dreapta iar urmatoarele 10 cu volan pe stanga
Numerotarea loturilor incepe de la prima masina produsa cu seria 0 si lot 0
Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0

Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
1)Definire: 40p
  - Creati o clasa pentru un obiect iterabil
   a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
   b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
   c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
2) Executie: 40p
 - Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
 - Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p

3) Documentatie: 20p
   a) adaugati type hints 5p
   a) documentati modulul 5p
   b) documentati clasele 5p
   c) documentati metodele 5p
"""


class Iterator:
    """
    Un iterator care are doi parametrii: serie , volum
    """
    def __init__(self, serie_inceput, volum):
        """
        Constructor care salveaza parametrii in variabile locale, calculeaza lot inceput lot final , lot curent
        :param serie_inceput: int
        :param volum: int
        """
        self.serie = serie_inceput
        self.vol = volum
        self.lotinceput = self.serie // 20
        self.lotfinal = (self.serie+self.vol) //20
        self.lotcurrent = self.lotinceput -1
    def __iter__(self):
        """
        Un interator avem nevoie de el pentru ca clasa e un iterator
        :return: self
        """
        return self

    def __next__(self):
        """
        Functia next returneaza urmatorul lot , verifica daca lotul curent lot final , daca da returneaza lot
        altfel opreste iteratia
        :return: int
        """
        if self.lotcurrent < self.lotfinal:
            self.lotcurrent +=1
        else:
            raise StopIteration

        return self.lotcurrent


class ParcAuto:
    """
    Clasa OParc auto care contine masinile clasate cu volan pe dreapta si pe stanga, in functie de serie
    """
    def __init__(self, serie, vol):
        """
        Apeleaza iterotorul si clasifica masinile in volan pe stanga si dreapta
        :param serie: int
        :param vol: int
        """
        self.__iter = Iterator(serie, vol)
        self.se = serie
        self.vl = vol
        self.lot = self.se // 20
        self.dreapta = []
        self.stanga = []
        for x in range(self.se, self.vl + self.se):
            if x < 10 + (self.lot*20):
                self.lot = x//20
                self.dreapta.append(x)  # salveaza in lista

            else:
                self.lot = x // 20
                self.stanga.append(x)

    def volan_dreapta(self):
        """
        returneaza o lista cu masinile pe dreapta
        :return: list
        """
        return self.dreapta


    def volan_stanga(self):
        """
        returneaza o lista cu masinile pe dreapta
        :return: list
        """
        return self.stanga

    def __iter__(self):
        """
        un iterator
        :return: self
        """
        print("Class iter")
        return self.__iter;


object = ParcAuto(101, 41)

print(f'Serie cu masini cu volan pe dreapta {object.dreapta}')
print(f'Serie cu masini cu volan pe dreapta {object.stanga}')
with open('Parcauto.txt', 'w+') as file:
    for i in object:
        file.write(str(i)+'\n')
        print(i)

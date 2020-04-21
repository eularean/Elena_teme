# Tema6 - 30% din nota finala
# Creati o clasa care se intantiaza cu o lista de cai de fisiere
# Clasa va avea o metoda create_ordered_log ce va sorta fiecare linie din fisiere pe baza primului cuvant
# Primul cuvant reprezinta data scrisa in formatul UNIX si este un numar
# Fisierele se gasesc in repo.

import os


class LogSorter():
    """
        o clasa care sorteaza linile dupa primul cuvant gasit in fisierele primite ca parametru
        ...
        Atributes:
        ---------
        files : list
            lista de loguri care o sa fie sortata

    """
    def __init__(self, files: list):
        """
        Functie care cauta fisierele primite ca parametru , le deschide , le citeste linie cu linie si le pune intr-o
        lista.

        Parameters:
        --------------
        :param files: list
            lista de loguri care sa fie sortata
        """
        self.files = []
        for file in files:
            path = os.path.join(os.path.dirname(__file__), file + '.log')
            self.files.append(path)
            print(self.files)
        self.file1 = open(self.files[0], "r")
        self.file2 = open(self.files[1], "r")
        self.lista_completa = self.file1.read().splitlines() + self.file2.read().splitlines()
        print(self.lista_completa)
    def create_ordered_log(self, output_file: str):
        """
        Functie care creaza fisierul de output la calea curenta a directorului , deschide si scrie in fisier lista
        ordonata dupa primul cuvant.
        Parameter:
        ---------
        :param output_file: str
        """
        path = os.path.join(os.path.dirname(__file__), output_file)
        self.primul = []
        self.output = open(path, "w")
        self.lista_completa.sort()
        for elem in self.lista_completa:
            self.output.write(str(elem)+ '\n')

        print(self.lista_completa)
help(LogSorter)
log_sorter = LogSorter(['log1', 'log2'])
log_sorter.create_ordered_log('sorted.log')
"""
Tema4 - 40% din nota finala
Creati o functie care poate lua ca argument un obiect iterabil ce poate contine alte obiecte iterabile sau
ne iterabile. Se va itera peste toate obiectele iterabile de la orice nivel si se va crea o lista cu toate obiectele
ce nu pot si iterte sau in cazul string-urilor daca lungimea lor este 1
Nu uitati ca puteti folosi recursivitate
ex:
funtia primeste: [(1, 5), 'abc', {'x': 'y'}, [[[3]]], set()]
funtia returneaza [1, 5, 'a', 'b', 'c', 'x', 'y', 3]
"""
input = [(1, 5), 'abc', {'x': 'y'},'t', [[[3]]], set()]
output = [1, 5, 'a', 'b', 'c', 'x', 'y', 3]
result = []
not_iterate = []
def flatten(data):
    for onedata in data:
        if not hasattr(onedata, '__iter__'):
            result.append(onedata)
        elif isinstance(onedata, dict):
            for key, value in onedata.items():
                result.append(key)
                result.append(value)
        elif isinstance(onedata,str):
            if len(onedata) == 1:
                not_iterate.append(onedata)
            else:
                for elem in onedata:
                    result.append(elem)
        elif isinstance(onedata,list):
            for elem in onedata:
                if isinstance(elem,int):
                    result.append(elem)
                else:
                    flatten(elem)
        elif isinstance(onedata,tuple):
            for elem in onedata:
                result.append(elem)
        else:
            #presupunem ca restul nu pot fi iterate
            not_iterate.append(onedata)
    return result

#print(flatten(input))
assert flatten(input) == output
import numpy as np
'''
Numpy - dlaczego jest szybsze niż zwykłe listy?

1. Zapisuje liczby jedynie jako int32, bez jakichkolwiek innych wartości (listy posiadają różne wartośći przypisane do liczb,
więc na ogół ważą dużo więcej)

2. Contiguous memory - sprawia że informacje (liczby) z list zapisywane są obok siebie, przez co procesor przetwarza
wszystkie dane na raz, zamiast każdą informację pojedynczo.

3. Efektwniejsze używanie pamięci cache (poprzez poprzedni punkt)

ciekawy przykład:
a = [1,3,5]
b = [1,3,5]
print(a*b) = error

a = np.array([1,3,5])
b = np.array([1,3,5])
print(a*b) = [ 1 9 25 ]


NumPy jest backbonem najważniejszych bibliotek używanych do analizy danych i data science;
- Pandas
- Matplotlib

Jest on bardzo przydatny do pracy na macierzach, gdziekolwiek mialyby ci się przydać
'''


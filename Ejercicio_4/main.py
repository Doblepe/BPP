
lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

for sublist in lista:
    print(max(sublist))



def check_even(number):
    if number % 2 != 0:
        return True
    else:
        return False


lista_2 = [3, 4, 8, 5, 5, 22, 13]

# if an element passed to check_even() returns True, select it
lista_primos = filter(check_even, lista_2)

# converting to list
lista_primos = list(lista_primos)

print(lista_primos)



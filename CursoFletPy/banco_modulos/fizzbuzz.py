fuzz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# paso 1 : iterar sobre la lista
for num in fuzz:
    # paso 2: revisar si el numero actual es divisible entre 3 o 5
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)



D = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}
print(D)
print(list(D.keys()))

for key in D:
    print(key, '=>', D[key])

# Квадраты чисел
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
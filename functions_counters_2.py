"""
Допиши функцию number_of_occurrences() так, чтобы она сосчитала,
сколько раз в строке string встречается буква, переданная в параметр char.
"""
def number_of_occurrences(char, string):
    count = 0
    for letter in string:
        if letter == char:
            count += 1
    print('Исходная строка:', string)
    print('Количество вхождений символа', char, 'составляет:', count)

phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
number_of_occurrences('е', phrase)

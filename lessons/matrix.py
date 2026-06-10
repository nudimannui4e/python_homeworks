"""
Нужно вывести таблицу умножения
1	2	3	4	5	6	7	8	9
2	4	6	8	10	12	14	16	18
3	6	9	12	15	18	21	24	27
4	8	12	16	20	24	28	32	36
5	10	15	20	25	30	35	40	45
6	12	18	24	30	36	42	48	54
7	14	21	28	35	42	49	56	63
8	16	24	32	40	48	56	64	72
9	18	27	36	45	54	63	72	81
"""

def matrix(count_number):
    """
    :param count_number: число-граница для таблицы
    :return: таблица умножения от 1 до count_number включительно
    """
    for i in range(1, count_number + 1): # строки
        for j in range(1, count_number + 1): # столбцы
            print(i*j, end='\t')
        print() # перенос строки итерации внешнего цикла

def main():
    #count_number = 10
    while True:
        """
        Enter a number: 0.1 <-------
        ValueError: invalid literal for int() with base 10: '0.1'
        https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
        """
        try:
            count_number = int(input('Enter a number: '))
            if count_number > 0:
                matrix(count_number)
            else:
                print('Only positive numbers!')
        except ValueError as e:
            print(f'Incorrect input, try again: {e}')
            continue

        answer = input('Again? (y,n): ').strip().lower()
        if answer not in ('y', 'yes', 'н'):
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(f'\nCTRL+C pressed, exit...')

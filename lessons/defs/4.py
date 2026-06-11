
square_of_room = [22.2, 55,5, 16.85, 4.52, 22.19, 7.78, 29.84, 22.19]

count = 0
square = 22.19

for i in square_of_room:
    if i == square:
        count += 1

print(f'Кол-во помещений площадью {square} = {count}')
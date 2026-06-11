def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print(f'У тебя {friends_count} друг')
    elif 2 <= friends_count <= 4:
        print(f'У тебя {friends_count} друга')
    elif 5 <= friends_count <= 20:
        print(f'У тебя {friends_count} друзей')
    else:
        print('Ого, как у тебя много друзей')

for friends_count in range(0,22):
    print_friends_count(friends_count)


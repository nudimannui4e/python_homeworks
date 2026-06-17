favorite_songs = {
    'Звезда по имени солнце': 'Кино',
    'Тополиный пух': 'Иванушки',
    'Город золотой': 'Аквариум',
}

for song, performer in favorite_songs.items(): # key, value
    print('Песню', song, 'исполняет', performer)

for music in favorite_songs.keys(): # key
    print('Я каждый день по три раза слушаю песню', music)

for singer in favorite_songs.values(): # value
    print('Я больше не могу слушать исполнителя', singer)


playlist_1 = {
    'снежинка',
    'три белых коня'
}
playlist_2 = {
    'happy new year',
    'снежинка'
}

#debug
print(playlist_1, playlist_2)

playlist_diff = playlist_2.difference(playlist_1)
print(playlist_diff)

playlist_x = playlist_1.intersection(playlist_2)
print(playlist_x)
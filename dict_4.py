english = {
    'нога': 'leg',
    'питон': 'python',
}

print(english)

english['рука'] = 'arm'

print(english)

english['нога'] = 'foot'
print(english)

new_words = {
    'мозг': 'brain',
    'логика': 'logic',
}

english.update(new_words)
print(english)
# вложенный словарь
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

print(f"Full name: {rec['name']}")
print(f"Only last: {rec['name']['last']}")
print(f"Jobs: {rec['jobs']}")
print(f"Indexing: {rec['jobs'][-1]}")
rec['jobs'].append('janitor')
print(f"Add job: {rec['jobs'][-1]}")
print(rec)

# rec сейчас занимает определенную ОЗУ, можем посмотреть:
import sys
print(f"Размер словаря {sys.getsizeof(rec)} байт")
print("Очищаем занимаемую память...")
rec = None
print(f"Размер словаря {sys.getsizeof(rec)} байт")
"""
Размер покажет условно 232 байта, хотя значения ключей
занимают больше.
Секрет в том, что словарь хранит ссылки, а не сами значения и объекты.
"""

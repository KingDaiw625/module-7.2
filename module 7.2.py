info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    strings_position = {}
    position = 1
    file = open(file_name, 'w', encoding= 'utf-8')
    for string in strings:
        strings_position[(position, file.tell())] = string
        file.write(string + '\n')
        position += 1
    file.close()
    return strings_position


result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



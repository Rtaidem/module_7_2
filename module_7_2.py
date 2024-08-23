def custom_write(file_name, strings):
    strings_positions = {}
    
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            position = file.tell()
            strings_positions[(i, position)] = string
            file.write(string + '\n')
    
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

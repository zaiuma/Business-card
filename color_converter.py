# Файл color_converter.py
# Автор: Умалатова Зайнаб Дагировна
# Этот файл является частью проекта 'Business-card'

def rgb_hex():
    print('Конвертер RGB → HEX')
    print('=' * 30)
    red = int(input('Введите значение для красного (R) от 0 до 255: '))
    green = int(input('Введите значение для зеленого (G) от 0 до 255: '))
    blue = int(input('Введите значение для синего (B) от 0 до 255: '))
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        print(f'RGB: ({red}, {green}, {blue})')
        print(f'HEX: #{red:02X}{green:02X}{blue:02X}')
    else:
        print('Ошибка! Число должно быть от 0 до 255')

rgb_hex()
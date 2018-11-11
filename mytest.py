
class Television:
    def __init__(self):
        self.chanel = 1
        self.volume = 5

    def set_chanel(self):
        new_chanel = input('Введите желаемый канал: ')
        if type(new_chanel) is 'int':
            if new_chanel > 0 and new_chanel < 11:
                self.chanel = new_chanel
                print('Теперь вы смотрите канал ', self.chanel)
            else:
                print('Ваш телевизор поддерживает каналы от 1 до 10')
        else:
            print('Вы ввели не число')

    def change_volume(self):
        volume_symbol = input('Введите + или - для изменения уровня громкости: ')
        if volume_symbol == '+':
            self.volume += 1
            print('Громкость увеличена')
        elif volume_symbol == '-':
            self.volume -= 1
            print('Громкость уменьшена')
        else:
            print('Введен неверный символ')

# исдигит, оптимизировать принты
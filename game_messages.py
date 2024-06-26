class GameMessages:
    def __new__(cls, *args, **kwargs):
        return None


class GallowsGameMessages(GameMessages):
    GREETING = '''Добро пожаловать в игру "Виселица"! 
Сейчас программа загадает слово, существительное русского языка. 
Ваша задача отгадать его прежде, чем нарисованный человек окажется на виселице. 
Вы можете играть неограниченное количество раз. Удачи!
'''
    IS_GAME_CONTINUE = 'Если вы хотите сыграть еще раз введите "да": '
    IS_WIN = 'Поздравляю, вы отгадали слово!'
    IS_FAIL = 'Вы проиграли.'
    INPUT_LETTER_MESSAGE = 'Введите букву русского алфавита: '
    CHECK_KEYBOARD_LAYOUT = 'Проверьте раскладку клавиатуры.'
    ANSWER = 'Было загадано слово "{}".'
    WRONG_LETTER = 'К сожалению, буквы "{}" нет в слове.'
    CORRECT_LETTER = 'Да, буква "{}" есть в слове!'
    LENGTH_OF_SECRET_WORD = 'Загаданное слово состоит из {} букв.'
    VERIFIED_LETTER = 'Вы уже проверяли наличие буквы "{}" в слове.'
    CONTINUE = 'Продолжим!'

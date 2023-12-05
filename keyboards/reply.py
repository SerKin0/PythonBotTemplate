from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main import logger  # Импорт логгера из другого модуля


def sort_keyboard_button(array: list, row_width=1):
    # Функция для разделения списка кнопок на строки заданной ширины
    return [array[i: i + row_width] for i in range(0, len(array), row_width)]


def creat_reply_keyboard(buttons: list, row_width_center=2, add_first=0, row_width_up=1, add_last=0, row_width_down=1):
    # Функция для создания обычной(Reply) клавиатуры с заданными кнопками
    # buttons: список названий кнопок
    # row_width_center: ширина строки для центральных кнопок
    # add_first: количество кнопок, добавляемых в начало
    # row_width_up: ширина строки для верхних кнопок
    # add_last: количество кнопок, добавляемых в конец
    # row_width_down: ширина строки для нижних кнопок

    # Если список кнопок пуст, генерируем предупреждение через логгер и возвращаем None
    if not buttons:
        logger.warning("В reply клавиатуру введен пустой массив buttons")
        return None

    # Если параметры add_last и add_first введены некорректно, генерируем предупреждение через логгер и возвращаем None
    if len(buttons) < add_last + add_first:
        logger.warning(f"В reply клавиатуру введены некорректные данные:\n"
                       f"add_last ({add_last}) и add_first ({add_first})")
        return None

    # Преобразуем названия кнопок в объекты KeyboardButton
    buttons = list(map(lambda x: KeyboardButton(text=x), buttons))

    # Формируем разметку клавиатуры
    keyboard = [
        *sort_keyboard_button(buttons[:add_first], row_width=row_width_up),
        *sort_keyboard_button(buttons[add_first: -add_last] if add_last != 0 else buttons[add_first:],
                              row_width=row_width_center),
        *sort_keyboard_button(buttons[-add_last:] if add_last != 0 else [], row_width=row_width_down)
    ]

    # Создаем разметку ReplyKeyboardMarkup
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return markup

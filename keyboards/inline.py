# Импортируем необходимые для создания inline-клавиатуры элементы из библиотеки aiogram.types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Импортируем функцию sort_keyboard_button из модуля keyboards.reply
from keyboards.reply import sort_keyboard_button


def creat_inline_keyboard_index(buttons: list, index: str, add_last=0, row_width=2):
    # Функция для создания inline-клавиатуры с переданными кнопками и их индексами
    # buttons: список названий кнопок
    # index: строка, которая будет добавлена к индексу кнопки
    # add_last: количество дополнительных кнопок, которые добавляются в конец
    # row_width: количество кнопок в строке

    if add_last > len(buttons):
        # Если количество дополнительных кнопок больше чем имеющиеся кнопки, возвращаем None
        return None
    else:
        # Формируем разметку
        markup = [
            *sort_keyboard_button(list(
                map(lambda button: InlineKeyboardButton(text=button, callback_data=f"{index}_{button}"),
                    buttons if add_last == 0 else buttons[:-add_last])
            ), row_width),
            *sort_keyboard_button(list(
                map(
                    lambda button: InlineKeyboardButton(text=button, callback_data=f"{index}_{button}"),
                    [] if add_last == 0 else buttons[-add_last:]
                )
            ), row_width=1)
        ]
        return InlineKeyboardMarkup(inline_keyboard=markup)

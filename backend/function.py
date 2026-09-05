import customtkinter as ctk

import backend.RandomDice as rd

# сборщик подтверждений с чекбоксов
def active_item( list_check_box, textbox) -> list | None:
    textbox.configure(state = 'normal')
    try:
        active = list_check_box.get()  # запрашиваем у чекбоксов список
        return active

    except Exception:
        textbox.insert('end', 'Для броска, выберите кубы')
        textbox.configure(state='disable')
        return None

# обработчик бросков кубов
def throw_dice(data: list):
    result_list = []  # список результатов на вывод

    for val in data:
        result = rd.random_dice(val)

        dice_values = ({
            "Дайс": val,
             "Результат": result
        })
        result_list.append(dice_values)

    return result_list

# распаковщик словарей
def unpacking(data, textbox):
    textbox.configure(state='normal')  # разрешение на редактирование
    textbox.delete('1.0', 'end')  # очищаем вывод

    # проходим по массиву
    for item in data:
        # список нужен для добавления распакованной части
        item_list = []
        # items() позволяет автоматически сопоставлять ключи со значениями
        for key, value in item.items():
            item_list.append(f'{key.capitalize()}: {value}')

        new_text = " | ".join(item_list) + "\n"
        textbox.insert('end', new_text)

    textbox.configure(state='disable')


def dice_roll(list_check_box, textbox):
    data = active_item(list_check_box, textbox)

    #print("DATA:", data)
    #print("TYPE:", type(data))

    if data is None:
        return

    roll_result = throw_dice(data)

   # print("RESULT:", roll_result)

    unpacking(roll_result, textbox)
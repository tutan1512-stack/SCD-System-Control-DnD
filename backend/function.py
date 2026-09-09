import customtkinter as ctk

import backend.RandomDice as rd

# сборщик подтверждений с чекбоксов
def active_item( list_check_box, textbox) -> list | None:
    textbox.configure(state = 'normal')
    try:
        active = list_check_box.get()  # запрашиваем у чекбоксов список
        new_active = []

        for item in active: # проходим по списку
            dice = rd.Dice(name=item, multiplier=1) # новый объект
            new_active.append(dice)  # список объектов

        textbox.configure(state='disable')
        return new_active


    except ValueError:
        textbox.insert('end', 'Для броска, выберите кубы')
        textbox.configure(state='disable')
        return None


# обработчик бросков кубов
def throw_dice(data: list):
    result_list = []

    for value in data: # объект списка
        #передаем куб и получаем куб
        final_dice = rd.random_dice(value)
        # передаем куб в список
        result_list.append(final_dice)

    return result_list

# распаковщик словарей
def unpacking(list, textbox, sumbox):
    textbox.configure(state='normal')  # разрешение на редактирование
    textbox.delete('1.0', 'end')  # очищаем вывод

    sumbox.configure(state='normal')  # разрешение на редактирование
    sumbox.delete('1.0', 'end')  # очищаем вывод

    summ = 0
    # проходим по массиву
    for obj in list: # список объектов
        # список нужен для добавления распакованной части
        name = obj.get_name()
        result = obj.get_result()
        summ = summ + result

        new_text = f"{name} | {result}\n"
        textbox.insert('end', new_text)

    sumbox.insert('end', summ, 'center')
    textbox.configure(state='disable')
    sumbox.configure(state='disable')


def dice_roll(list_check_box, textbox, sumbox):
    data = active_item(list_check_box, textbox)

    #print("DATA:", data)
    #print("TYPE:", type(data))

    if data is None:
        return

    roll_result = throw_dice(data)

   # print("RESULT:", roll_result)

    unpacking(roll_result, textbox, sumbox)
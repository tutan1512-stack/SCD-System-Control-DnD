import random
 # генератор случайных бросков дайсов
# должен получать тип дайса
# должен выдавать случайный результат данного типа

# условно: "введите дайс для броска: д20" -> генерит результат из 20 вариантов
class Dice():
    def __init__(self, name, multiplier = None, result = None):
        self.name = name # название куба
        self.multiplier = multiplier # множитель броска
        self.result = result # результат броска

    def get_multiplier(self):
        return  self.multiplier

    def get_name(self):
        return self.name

    def get_result(self):
        return  self.result

    def set_result(self, value):
        self.result = value


def random_dice(type_dice):
    try:
        name = type_dice.get_name() # имя куба
        edge = int(name[1:]) # число для границ бросков
        multiplier = type_dice.get_multiplier() # кол-во бросков
        result_list = []

        for i in range(multiplier):
            result = random.randint(1, edge)
            result_list.append(result)
            type_dice.set_result(result_list)

        return type_dice # возвращаем объект

    except ValueError:
        print("[!] Неправильный тип данных")


# сборщик подтверждений с чекбоксов
def active_item( list_check_box, textbox, multiplier) -> list | None:
    textbox.configure(state = 'normal')
    try:
        active = list_check_box.get()  # запрашиваем у чекбоксов список
        new_active = []

        for item in active: # проходим по списку
            dice = Dice(name=item, multiplier=multiplier.get()) # новый объект
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
        final_dice = random_dice(value)
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
        
        for item in result: # берем один результат из списка объекта
            summ = summ + item

        text = ", ".join(str(x) for x in result) # проходим по элементам результата
        new_text = f"{name} | {text}\n"
        textbox.insert('end', new_text)

    sumbox.insert('end', summ, 'center')
    textbox.configure(state='disable')
    sumbox.configure(state='disable')

def dice_roll(list_check_box, textbox, sumbox, multiplier):
    data = active_item(list_check_box, textbox, multiplier)

    #print("DATA:", data)
    #print("TYPE:", type(data))

    if data is None:
        return

    roll_result = throw_dice(data)

   # print("RESULT:", roll_result)

    unpacking(roll_result, textbox, sumbox)



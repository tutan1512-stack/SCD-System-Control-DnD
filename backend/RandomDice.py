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
        name = type_dice.get_name()
        edge = int(name[1:]) # число для границ бросков
        multiplier = type_dice.get_multiplier()

        for i in range(multiplier):
            result = random.randint(1, edge)
            type_dice.set_result(result)

        return type_dice # возвращаем объект

    except ValueError:
        print("[!] Неправильный тип данных")


import random
 # генератор случайных бросков дайсов
# должен получать тип дайса
# должен выдавать случайный результат данного типа

# условно: "введите дайс для броска: д20" -> генерит результат из 20 вариантов

def random_dice(type_dice):
    try:
        dice = type_dice
        if  dice[0].isdigit():
            part = dice.lower().split('d') # 5d20 -> 520
            multiplier = int(part[0]) # 520 -> 5
            edge = int(part[1]) # 520 -> 20
            #print(f'[>] Результат бросков {dice[1:]} ({multiplier}) раз: \n')

            for i  in range(multiplier):
                result = random.randint(1, edge)
                return result
                #print(f'[{i+1}] {randice}')

         #  print(f'\n[>] Сумма бросков: {summ}')

        elif not  dice[0].isdigit():
            edge = int(dice[1:])
            randice = random.randint(1,edge )
            return randice

    except ValueError:
        print("[!] Неправильный тип данных")


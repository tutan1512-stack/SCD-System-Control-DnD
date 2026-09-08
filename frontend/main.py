import customtkinter as ctk
from tkinter import *

import backend.function as func
import backend.RandomDice as rd

# создаем тело программы
class App(ctk.CTk):
    def __init__(self): #  задает свойства новым экземплярам класса
        super().__init__() # задает новые свойства наследственным классам

        # настройки тела
        self.title('"Ваш С.У.Д. - Система Управления ДнД')
        self.geometry('1280x720')

        # футер
        self.version_bar = ctk.CTkFrame(self, height = 25, fg_color = 'transparent')
        self.version_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = 5 )

        # авторы
        self.version_text = ctk.CTkLabel(self.version_bar, text = 'Версия: 1.0.3', font = ('Minecraft RUS', 14), text_color = 'gray')
        self.version_text.pack(side = 'left')

        self.author = ctk.CTkLabel(self.version_bar, text='TerraCorp', font=('Minecraft RUS', 14),text_color='gray')
        self.author.pack(side='right')

        # вкладки
        self.tabview = ctk.CTkTabview(self, width = 20,  height = 20)
        self.tabview.pack(
            padx = 20, # высота бортиков вкладки
            pady = 20,  # ширина бортиков вкладки
            fill = 'both', # автоматическая корректировка бортиков по ширине
            expand = True # автоматическая корректировка бортиков по высоте
        )

        tabDice = self.tabview.add("Кубы")
        tabNPC = self.tabview.add("НПС")
        tabInfo = self.tabview.add("Справочники")

        # Виджеты
        ctk.CTkLabel(master = tabDice, text = ' Бросайте кубы! ').pack(pady = 20)
        ctk.CTkLabel(master = tabNPC, text = ' Выбирайте персонажей!').pack(pady = 20)
        ctk.CTkLabel(master = tabInfo, text = 'Освежите память!').pack(pady = 20)

        # Фреймы
        self.dice_frame = ctk.CTkFrame(tabDice)
        self.dice_frame.pack(
            padx = 20,
            pady = 20,
            fill = 'both',
            expand = True,
        )
        self.dice_frame.grid_columnconfigure(0, weight = 1) # левая часть
        self.dice_frame.grid_columnconfigure(1, weight = 1) # правая часть


        # правый фрейм
        # --------------------------------
        self.control_frame = ctk.CTkFrame(self.dice_frame, width = 200, height = 200)
        self.control_frame.grid(row = 0, column = 1, padx = 50, pady = 5, columnspan = 1, sticky = 'ns') # последний атрибут отвечает за растяжение по направлениям

        # кубы
        self.dice_checkbox =  ControlBoxFrame(
            self.control_frame,
            values = ['1d100','1d20','1d12','1d10','1d8','1d6','1d4'] )
        self.dice_checkbox.grid(row = 0, column = 0, padx = 10, pady = (10,10), sticky = 'ns')


        # левый фрейм
        # --------------------------------
        self.result_frame = ctk.CTkFrame(self.dice_frame, width = 150, height = 200)
        self.result_frame.grid(row = 0, column =0)

        self.result_frame.columnconfigure(index=0, weight = 1)
        self.result_frame.columnconfigure(index=1,weight=1)
        self.result_frame.rowconfigure(index=0,weight=1)
        self.result_frame.rowconfigure(index=1,weight=0)

        # вывод результата
        self.result_box = ctk.CTkTextbox(self.result_frame, width=150, height = 150, wrap='word',font=('Aria', 14))
        self.result_box.grid(row = 0, column = 0, rowspan=2, padx = (20,20), pady = (20,20),    sticky = 'nsew')


        # вывод суммы
        self.summ_box = ctk.CTkTextbox(self.result_frame, width=60, height=60, font=('Aria', 24))
        self.summ_box.grid(row = 0, column = 1,padx = (20,20), pady = 10, sticky = 's')
        self.summ_box.tag_config("center", justify='center')

        self.summ_label = ctk.CTkLabel(self.result_frame,text="Сумма\n бросков",  justify = 'center')
        self.summ_label.grid(row = 1, column =1, pady= (0,20),sticky = 'n')
       # self.summ_box.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 1, sticky = '')

        # настройки кнопок

        self.button = ctk.CTkButton(
            master = self.dice_frame, # указывает к какому телу будет привязано
            text = ' Бросить кубы! ',
            command = lambda : func.dice_roll(self.dice_checkbox, self.result_box, self.summ_box) # какая команда будет выполнена при нажатии
        ) # lambda тут нужна, чтобы при компиляции код сразу не срабатывал на холостом
        self.button.grid(row = 1, column = 1, padx=20, pady=10)


class ControlBoxFrame(ctk.CTkFrame):
    def __init__(self, master, values ):
        super().__init__(master)
        self.grid_columnconfigure(0, weight = 1)
        self.values = values
        self.checkboxes = [] # список в котором будут храниться боксы

        # # параметр за текст над блоком
        # self.title = ctk.CTkLabel(self, text = self.values, fg_color = 'gray30', corner_radius = 6) # задаем шаблон для чекбоксов
        # self.title.grid(row = 0, column = 0, padx = 10, pady = (10,0), sticky = 'ne' )

        # enumerate является инкреметной функцией, позволяет вести счет операций
        for i, value in enumerate(self.values):
            # создаем перемен ную бокса с нашим текстом
            checkbox = ctk.CTkCheckBox(self, text = value)
            # каждый новый бокс встает под предыдущем
            checkbox.grid(row = i +1, column = 0, padx = 10, pady =(5,5), sticky = 'we')
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1: # если объект включен (пользователь выбрал)
                # вносим в список атрибут текста от каждого бокса
                checked_checkboxes.append(checkbox.cget('text'))
        return checked_checkboxes


# запуск программы
app = App()
app.mainloop()
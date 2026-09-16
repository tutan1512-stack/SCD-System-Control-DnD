import customtkinter as ctk

# Класс отвечающий за генерацию чекбокса
class ControlBoxFrame(ctk.CTkFrame):
    def __init__(self, master, values ):
        super().__init__(master)
        self.grid_columnconfigure(0, weight = 1)
        self.values = values
        self.checkboxes = [] # список в котором будут храниться боксы

        # # параметр за текст над блоком
        # self.title = ctk.CTkLabel(self, text = self.values, fg_color = 'gray30', corner_radius = 6) # задаем шаблон для чекбоксов
        # self.title.grid(row = 0, column = 0, padx = 10, pad
        # y = (10,0), sticky = 'ne' )

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

class SpinBox(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 width = 100,
                 height= 32,
                 step_size: int  = 1,
                 command = None,
                 **kwargs) :
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=('gray78','gray28'))

        self.grid_columnconfigure((0,2), weight=0)
        self.grid_columnconfigure(1,weight=1)

        self.subtrack_button = ctk.CTkButton(self,text = '-',
            width= height - 6, height= height-6,
            command = self.subtrack_button_callback,
        )
        self.subtrack_button.grid(
            row=0,column=0,
            padx=(3,0),pady=3
        )

        self.entry = ctk.CTkEntry(
            self,
            width=width - (2*height), height=height-6,
            border_width=0,
        )
        self.entry.grid(
            row = 0,column=1,
            columnspan = 1,
            padx = 3,pady = 3,
            sticky = 'ew'
        )

        self.add_button = ctk.CTkButton(
            self,
            text = '+',
            width = height - 6, height= height - 6,
            command = self.add_button_callback,
        )
        self.add_button.grid(
            row=0,column=2,
            padx=(0, 3),pady=3)

        self.entry.insert(0, '1 ')

    def add_button_callback(self):
        if self.command is not None: # Если произошел вызов, то вызываем
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size # Прибавляем к текущему числу шаг
            self.entry.delete(0,'end')
            self.entry.insert(0, value) # обновляем отображение
        except ValueError:
            return

    def subtrack_button_callback(self):
        if self.command is not None: # Если произошел вызов, то вызываем
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size # Вычитаем от текущего числа шаг
            self.entry.delete(0,'end')
            self.entry.insert(0, value) # обновляем отображение

            if value <= 1:
                self.entry.delete(0, 'end')
                self.entry.insert(0, 1)  # обновляем отображение

        except ValueError:
            return

    def get(self) -> int| None:
        try:
            return int(self.entry.get())

        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0,'end')
        self.entry.insert(0, str(int(value))) # обновление отображения
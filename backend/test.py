import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")

# --- КОД ДЛЯ ОТОБРАЖЕНИЯ СЕТКИ ---
# Шаг сетки в пикселях (например, каждые 50 пикселей)
GRID_STEP = 50

# Создаем холст на заднем фоне
canvas = ctk.CTkCanvas(app, width=600, height=400, bg=app.cget("bg"), highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Рисуем вертикальные и горизонтальные линии
for x in range(0, 600, GRID_STEP):
    canvas.create_line(x, 0, x, 400, fill="gray", dash=(2, 2)) # Пунктир
for y in range(0, 400, GRID_STEP):
    canvas.create_line(0, y, 600, y, fill="gray", dash=(2, 2))
# ---------------------------------

# Вали элементы интерфейса (размещайте как обычно)
btn = ctk.CTkButton(app, text="Тестовая кнопка")
btn.place(x=150, y=100)

btn2 = ctk.CTkButton(app, text="Тестовая кнопка")
btn2.place(x=0, y=50)

app.mainloop()

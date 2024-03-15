import tkinter as tk
from tkinter import messagebox
import qrcode
import pyperclip

def generate_qr_code():
    link = link_entry.get()
    if link:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Сохраняем изображение QR-кода в файл
        filename = "qr_code.png"
        img.save(filename)

        messagebox.showinfo("Готово", "QR-код успешно создан!")
    else:
        messagebox.showwarning("Предупреждение", "Введите ссылку!")

def paste_text():
    text = pyperclip.paste()
    link_entry.insert(tk.END, text)

# Создаем основное окно
root = tk.Tk()
root.title("Генератор QR-кода")

# Создаем метку и поле для ввода ссылки
link_label = tk.Label(root, text="Введите ссылку:")
link_label.pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack()

# Создаем кнопку для вставки текста из буфера обмена
paste_button = tk.Button(root, text="Вставить текст", command=paste_text)
paste_button.pack()

# Создаем кнопку для генерации QR-кода
generate_button = tk.Button(root, text="Создать QR-код", command=generate_qr_code)
generate_button.pack()

# Запускаем главный цикл программы
root.mainloop()

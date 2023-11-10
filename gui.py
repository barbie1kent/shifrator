import tkinter as tk
from tkinter import *
from tkinter import ttk
import pyperclip
from PIL import *
from tkinter.messagebox import showinfo


alphabet_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
morse_code = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-',
    'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.',
    'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.',
    'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--',
    'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-'
}

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShifroBoom")
        self.root.geometry('965x600+400+200')


        # Создание элементов интерфейса
        self.copyright = Label(root, text="©Бобренев Даниил, ИСП321-п")
        self.label_input = Label(root, text="Исходный текст:", font="helvetica 15", foreground="#004D40")
        self.label_output = Label(root, text="Результат:", font="helvetica 15", foreground="#004D40")
        self.entry_input = Text(root,width=70, cursor="plus")
        self.text_output = Text(root, width=70, cursor="plus")
        self.button_copy = Button(root, text="Копировать", font="helvetica 13", cursor="center_ptr", foreground="#008000",bg = "#FFFF99", command=self.copy_output)
        self.button_clear_input = Button(root, text="Очистить поле ввода", font="helvetica 13",cursor="center_ptr", foreground="#FF0000",bg = "#FFFF99", command=self.clear_input)
        self.button_clear_output = Button(root, text="Очистить поле вывода", font="helvetica 13",cursor="center_ptr", foreground="#FF0000",bg = "#FFFF99", command=self.clear_output)
        self.button_paste = Button(root, text="Вставить", font="helvetica 13",cursor="center_ptr", foreground="#004FAA",bg = "#FFFF99", command=self.paste_text)
        self.button_caesar_encoder = Button(root, text="Шифр Цезаря \nшифровать", font="helvetica 15", cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.caesar_cipher_encoder)
        self.button_caesar_decoder = Button(root, text="Шифр Цезаря \nдешифровать", font="helvetica 15",cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.caesar_cipher_decoder)
        self.button_vigenere_encoder = Button(root, text="Шифр Виженера \nшифровать", font="helvetica 15",cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.vigenere_cipher_encoder)
        self.button_vigenere_decoder = Button(root, text="Шифр Виженера \nдешифровать", font="helvetica 15",cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.vigenere_cipher_decoder)
        self.button_morse_encoder = Button(root, text="Азбука Морзе \nшифровать", font="helvetica 15",cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.morse_cipher_encoder)
        self.button_morse_decoder = Button(root, text="Азбука Морзе \nдешифровать", font="helvetica 15",cursor="exchange", foreground="#004D40",bg = "#FF6666", command=self.morse_cipher_decoder)
        #self.button_shift_plus = Button(root, text="+",font="helvetica 15", width=2, cursor="plus", command=self.increase_shift)
        #self.button_shift_minus = Button(root, text="-",font="helvetica 15", width=2, cursor="dot", command=self.decrease_shift)
        self.entry_shift = Entry(root, width=5)
        self.label_shift = Label(root, text="Сдвиг:", font="helvetica 15", foreground="#004D40")
        self.entry_key =  Entry(root, width=40)
        self.label_key = Label(root, text="Ключ:", font="helvetica 15", foreground="#004D40")
        self.button_info = Button(root, text="Информация", font="helvetica 15", command=self.information, cursor="right_ptr", foreground="#004D40", bg = "#FFFF00")
        self.quitee = Button(root, text="Выход", font="helvetica 15", foreground="#004D40",bg = "#66FF33", command=self.quit)



        # Упаковка элементов интерфейса
        self.quitee.place(x= 0, y= 560)
        self.copyright.place(x= 785, y= 580)
        self.label_input.place(width=160, height=30, x= 20, y= 80)#
        self.label_output.place(width=160, height=30, x= 5, y= 240)# "результат"
        self.entry_input.place(width=565, height= 150, x = 185, y = 30)#ввод
        self.text_output.place(width=565, height=150, x= 185, y= 200)#вывод
        self.button_copy.place(width=100, height= 35, x = 185, y = 350) #копировать
        self.button_clear_input.place(width=180, height= 35, x = 380, y = 385) #очистить
        self.button_clear_output.place(width=180, height= 35, x = 380, y = 350) #очистить
        self.button_paste.place(width=100, height= 35, x = 650, y = 350) # вставить
        #self.button_shift_plus.place(width=30, height=30, x= 830, y= 110) #плюс один
        #self.button_shift_minus.place(width=30, height=30, x= 870, y= 110)#минус один
        self.entry_shift.place(width=30, height=30, x= 850, y= 70)#сдвиг
        self.label_shift.place(width=70, height=30, x= 765, y= 70)# "сдвиг"
        self.entry_key.place(width=110, height= 35, x = 830, y = 200)# ключ
        self.label_key.place(width=70, height= 35, x = 750, y = 200)# "ключ"
        self.button_caesar_encoder.place(width=150, height= 48, x = 150, y = 420)# цезарь
        self.button_caesar_decoder.place(width=150, height= 48, x = 150, y = 480)
        self.button_vigenere_encoder.place(width=170, height= 48, x = 385, y = 420)# виженер
        self.button_vigenere_decoder.place(width=170, height= 48, x = 385, y = 480)
        self.button_morse_encoder.place(width=150, height= 48, x = 630, y = 420)# морзе
        self.button_morse_decoder.place(width=150, height= 48, x = 630, y = 480)# морзе
        self.button_info.place(width=130, height= 48, x = 835, y = 0)
        # TODO:
        # 1. ДОПИСАТЬ БЛЯДСКИЕ БАТТОНЫ
        # 2. ИНСТУКЦИЮ ЕБАНА ЖИЗЕНЬ
        # 3. ВРЕМЯ
        # 4. РЕЧЬ

    def copy_output(self):
        output_text = self.text_output.get("1.0", END).strip()
        pyperclip.copy(output_text)

    def clear_input(self):
        self.entry_input.delete("1.0", END)

    def clear_output(self):
        self.text_output.delete("1.0", END)

    def paste_text(self):
        clipboard_text = pyperclip.paste()
        self.entry_input.delete("1.0", END)
        self.entry_input.insert("1.0", clipboard_text)

    def increase_shift(self):
        current_shift = int(self.entry_shift.get())
        self.entry_shift.delete("1.0", END)
        self.entry_shift.insert("1.0", str(current_shift + 1))

    def decrease_shift(self):
        current_shift = int(self.entry_shift.get())
        self.entry_shift.delete("1.0", END)
        self.entry_shift.insert("1.0", str(current_shift - 1))

    def caesar_cipher_encoder(self):
        input_text = self.entry_input.get("1.0", END).lower()
        shift = int(self.entry_shift.get())
        encrypted_text = ""
        for char in input_text:
            if char.isalpha():
                if char in alphabet_rus:
                    encrypted_text += alphabet_rus[(alphabet_rus.index(char) + shift) % 33]
                elif char in alphabet_eng:
                    encrypted_text += alphabet_eng[(alphabet_eng.index(char) + shift) % 26]
            else:
                encrypted_text += char
        self.text_output.delete("1.0", END)
        self.text_output.insert(END, encrypted_text)

    def caesar_cipher_decoder(self):
        input_text = self.entry_input.get("1.0", END).lower()
        shift = int(self.entry_shift.get())
        encrypted_text = ""
        for char in input_text:
            if char.isalpha():
                if char in alphabet_rus:
                    encrypted_text += alphabet_rus[(alphabet_rus.index(char) - shift) % 33]
                elif char in alphabet_eng:
                    encrypted_text += alphabet_eng[(alphabet_eng.index(char) - shift) % 26]
            else:
                encrypted_text += char
        self.text_output.delete("1.0", END)
        self.text_output.insert(END, encrypted_text)

    def vigenere_cipher_encoder(self):
        input_text = self.entry_input.get("1.0", END).strip()
        key = 'YOUR_KEY'
        ciphertext = ""
        index = 0
        for char in input_text:
            if char.isalpha():
                char_num = ord(char)
                key_num = ord(key[index % len(key)].lower())
                if char.islower():
                    base_num = ord('а')
                else:
                    base_num = ord('А')
                encrypted_num = (((char_num - base_num) + (key_num - base_num)) % 33) + base_num
                encrypted_char = chr(encrypted_num)
                ciphertext += encrypted_char
                index += 1
            else:
                ciphertext += char
        self.text_output.delete('1.0', END)
        self.text_output.insert('1.0', ciphertext)


    def vigenere_cipher_decoder(self):
        ciphertext = self.entry_input.get("1.0", END).strip()
        key = 'YOUR_KEY'
        plaintext = ""
        index = 0
        for char in ciphertext:
            if char.isalpha():
                char_num = ord(char)
                key_num = ord(key[index % len(key)].lower())
                if char.islower():
                    base_num = ord('а')
                else:
                    base_num = ord('А')
                decrypted_num = (((char_num - base_num) - (key_num - base_num)) % 33) + base_num
                decrypted_char = chr(decrypted_num)
                plaintext += decrypted_char
                index += 1
            else:
                plaintext += char
        self.text_output.delete('1.0', END)
        self.text_output.insert('1.0', plaintext)

    def morse_cipher_encoder(self):
        input_text = self.entry_input.get("1.0", END).strip()
        ciphertext = ""
        for char in input_text:
            if char.lower() in morse_code:
                ciphertext += morse_code[char.lower()] + " "
            else:
                ciphertext += char
        self.text_output.delete('1.0', END)
        self.text_output.insert('1.0', ciphertext)

з
    def morse_cipher_decoder(self):
        ciphertext = self.entry_input.get("1.0", END).strip()
        input_text = ""
        morse_code_inv = {value: key for key, value in morse_code.items()}
        for word in ciphertext.split(" "):
            if word in morse_code_inv:
                input_text += morse_code_inv[word]
            else:
                input_text += word
        self.text_output.delete('1.0', END)
        self.text_output.insert('1.0', input_text)


    def information(self):
        showinfo(title="INFORMATION", message = "Приветствую в приложении ShifroBoom\n"
                                                "1. Вы можете написать в первое поле сообщение, которое хотите зашифровать или же дешифровать\n"
                                                "2. Далее снизу находятся кнопки шифрации и дешифрации представленных шифров\n"
                                                "3. ВАЖНО!!! Для шифра Цезаря нужно вводить нужный сдвиг после слова 'Сдвиг', а для шифра Виженера необходимый ключ после поля 'Ключ'\n"
                                                "4. Для удобства есть кнопки копирования, вставки и очистки полей, не забывайте ими пользоваться")
    def quit(self):
        root.quit()

root = tk.Tk()

root.config(cursor="heart")
app = CipherApp(root)
root.mainloop()
import requests
from tkinter import Tk, Label, Entry, Button, messagebox, END
from PIL import Image, ImageTk
import os
import datetime

root = Tk()
root.title('Загрузчик фото/аудио/видео')
root.geometry('700x500+300+230')
root.resizable(False, False)
root.attributes("-alpha", 0.95)
root['bg'] = 'DarkOliveGreen3'

lbl1 = Label(text='Вставьте ссылку вашего фото/аудио/видео (обязательно с форматом файла):', bg='DarkOliveGreen3',
             font=('Ariel', 11))
lbl1.place(relx=0.10, rely=0.10)

ent = Entry(width=72, font=('Ariel', 11))
ent.place(relx=0.07, rely=0.15)
ent.focus()

url, path, name = '', '', ''

lbl2 = Label()

img3 = Image.open('gom.jpg')
img3tk = ImageTk.PhotoImage(img3)
lbl4 = Label(image=img3tk, bg='DarkOliveGreen3')
lbl4.image = img3tk
lbl4.place(relx=0.46, rely=0.008)

root.iconbitmap('gomer.ico')


def view_done(num):
    img2 = Image.open('done.jpg')
    img2tk = ImageTk.PhotoImage(img2)
    lbl3 = Label(image=img2tk)
    lbl3.image = img2tk
    lbl3.place(relx=num, rely=0.23)


def del_done(num):
    lbl3 = Label(bg='DarkOliveGreen3')
    lbl3.place(relx=num, rely=0.23, relwidth=0.05, relheight=0.06)


def logic():
    global url, path, name
    url = ent.get()
    try:
        if url.rfind('.jpg') != -1 or url.rfind('.jpeg') != -1 or url.rfind('.png') != -1 or url.rfind('.bmp') != -1:
            name = datetime.datetime.today().strftime('%Y.%m.%d-%H.%M.%S')
            name = str(name) + '.jpg'
            r = requests.get(url)
            with open(name, 'wb') as code:
                code.write(r.content)

            img = Image.open(name)
            w, b = img.size
            w1 = w / 630
            b1 = b / 325
            if w1 <= 1 and b1 <= 1:
                img = img.resize((w, b), Image.BILINEAR)
            elif w1 > b1:
                img = img.resize((int(w / w1), int(b / w1)), Image.BILINEAR)
            else:
                img = img.resize((int(w / b1), int(b / b1)), Image.BILINEAR)
            imgtk = ImageTk.PhotoImage(img)
            lbl2 = Label(image=imgtk, bg='DarkOliveGreen3')
            lbl2.image = imgtk
            lbl2.place(relx=0.05, rely=0.31, relwidth=0.9, relheight=0.65)
            view_done(0.56)
            del_done(0.77)

        elif url.rfind('.mp4') != -1 or url.rfind('.3gp') != -1 or url.rfind('.avi') != -1 or url.rfind(
                '.mpg') != -1 or url.rfind('.mov') != -1 or url.rfind('.wmv') != -1:
            name = datetime.datetime.today().strftime('%Y.%m.%d-%H.%M.%S')
            name = str(name) + '.mp4'
            r = requests.get(url)
            with open(name, 'wb') as code:
                code.write(r.content)
            view_done(0.56)
            del_done(0.77)

        elif url.rfind('.mp3') != -1 or url.rfind('.wav') != -1 or url.rfind('.wma') != -1 or url.rfind(
                '.aac') != -1 or url.rfind('.flac') != -1:
            name = datetime.datetime.today().strftime('%Y.%m.%d-%H.%M.%S')
            name = str(name) + '.mp3'
            r = requests.get(url)
            with open(name, 'wb') as code:
                code.write(r.content)
            view_done(0.56)
            del_done(0.77)
        else:
            name = datetime.datetime.today().strftime('%Y.%m.%d-%H.%M.%S')
            name = str(name)
            r = requests.get(url)
            with open(name, 'wb') as code:
                code.write(r.content)
            view_done(0.56)
            del_done(0.77)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    except:
        pass


btn1 = Button(text='Скачать', width=14, font=('Ariel', 11), command=logic)
btn1.place(relx=0.35, rely=0.23)


def vopros():
    messagebox.showinfo('Вопросы?', '1. Все файлы сохраняются туда, где и находится данная программа.\n'
                                    '2. Чтобы получить URL фото необходимо, нажать правой кнопкой на '
                                    'элемент и выбрать \"Копировать адрес изображения\".\n'
                                    '3. Чтобы получить URL фото/видео из инстаграмма необходимо выбрать \"'
                                    'Просмотр кода элемента\" и найти ссылку с .jpg либо .mp4 нажав \'Ctrl+F\'.\n'
                                    '4. Чтобы можно было скачать видео с вк, необходимо перейти в мобильную версию '
                                    'добавив \'m\' перед доменом vk.com.\n'
                                    '5. Чтобы скачать видео с Youtube необходимо перед его доменом добавить'
                                    '\'ss\' и перейти по ссылке, где можно будет найти URL видео.\n'
                                    '6. В большистве случаев файл необходимо искать через \'Просмотр кода элемента\'.\n\n'
                                    'Кнопка \'Удалить\' удаляет скачанный файл на компьютере.')


btn2 = Button(text='?', font=('Ariel', 13), command=vopros)
btn2.place(relx=0.95, rely=0.135)


def delt():
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
        os.remove(path)
        lbl2 = Label(bg='DarkOliveGreen3')
        lbl2.place(relx=0.05, rely=0.31, relwidth=0.9, relheight=0.65)
        del_done(0.56)
        view_done(0.77)
    except:
        pass


btn3 = Button(text='Удалить', font=('Ariel', 11), command=delt)
btn3.place(relx=0.65, rely=0.23)


def delete():
    ent.delete(0, END)
    del_done(0.77)
    del_done(0.56)


btn4 = Button(text='x', font=('Ariel', 8), command=delete)
btn4.place(relx=0.904, rely=0.1462)

root.mainloop()
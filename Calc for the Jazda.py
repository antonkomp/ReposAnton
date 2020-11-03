# my calculator for the Jazda exe
from tkinter import *
from tkinter import messagebox
import math
from PIL import ImageTk, Image
import requests
import os

# кофигурации основного окна
root = Tk()
root.title('Calculator for the Jazda ')
root.geometry('360x460+450+250')
root.resizable(False, False)
root.attributes("-alpha", 0.93)
root["bg"] = "gray70"
ii = False
if ii == False:
    url = "https://vk.com/doc17835239_551527778?hash=7ab6ff1aeefe1bac4f&dl=3f69f04ddc37f6803c"
    r = requests.get(url)
    with open("re.ico", "wb") as code:
        code.write(r.content)
    root.iconbitmap("re.ico")
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 're.ico')
    os.remove(path)
    ii = True


# ответ на окно слата
def clicked():
    messagebox.showinfo('Одобрено Слатом!', 'Все верно        ')


# вывод нового окна
def show_message():
    result = messagebox.askyesno("Риторический вопрос", 'Слат питух!                 ')
    if result == True:
        clicked()
    else:
        show_message()


# конпка про слата
but_o_progr = Button(text='Слат питух?', command=show_message, bg="grey70", fg="grey20", font=('Comic Sans MS', 8))
but_o_progr.place(x=3, y=2)


# ответ на окно гайда
def gaide():
    messagebox.showinfo('Гайд по пасхалочкам', 'Правила: ответом может быть как и число, так и какое-то слово (чаще), '
                                               'сочетание слов, символ, сочетание кнопок. Пасхалочки в основном для'
                                               ' \'язды\' но бонусом будут и другие.\nЕсли кто-то был'
                                               ' найден, будет появляться фото того перса. На некоторых может быть '
                                               'несколько (до 2) пасхалочек. Все не так просто, но ответы почти всем знакомые,'
                                               ' удачки)))\n\n'
                                               '1. Найдите зрителя Макса (這個號碼)\n'
                                               '2. Найдите в общем (и целом) Лёшу\n'
                                               '3. Найдите порочного Диму (с напитком)\n'
                                               '4. Найдите провинциального из деревни "51" Андрея\n'
                                               '5. Найдите старого инопланетного Артема\n'
                                               '6. Найдите отстойного Антона с рудиментом\n'
                                               '_______________________________________________________\n'
                                               '7. Найдите Слата (без комментариев)\n'
                                               '8. Найдите взрослую Алину\n'
                                               '9. Найдите молодого горячего Рому (دروسالب)\n'
                                               '10. Найдите беларуса Руса\n'
                                               '11. Найдите решительного Владика\n'
                                               '12. Найдите выращивающего рис Кутю\n'
                                               '_______________________________________________________\n'

                                               '13.*** Найдите интеллектуальную Язду!!!\n\n'
                                               'P.S. регистр не важен, может быть на английском/русском. Для'
                                               ' облегчения на одну пасхалочку может быть несколько ответов.\n'
                                               'Всего пасхалочек 23)\n\n'
                                               'P.P.S. если открыть хотя бы 15 пасхалочек, появится тайный босс '
                                               'имеющий что-то даже большее, чем Антона ореол!\n\n'
                                               'Для примера, посмотреть как все работает, можно написать - \"Путин молодец\".\n\n'
                                               'Фото можно сохранять, если в памяти будут три семерки ☺')


# кнопка гайд по пасхалочкам
but_gaide = Button(text='Гайд по пасхалочкам', command=gaide, bg="grey70", fg="grey20", font=('Comic Sans MS', 8))
but_gaide.place(x=230, y=2)

suprise = 0


# знак равно посредством нажатия Энтер на клавиатуре
def inLabel(event):
    if event.keysym == 'Return':
        if text.get(1.0) == "0" and text.get(2.0) != '.':
            try:
                text.delete(1.0)
            except:
                pass
        text1 = "-+*./0123456789()"
        if text.get(1.0) not in text1:
            text.insert(END, "Первый символ не число!")
        try:
            result = eval(text.get('1.0', END))
            text.insert(END, "=\n" + str(result))
        except:
            text.insert(END, "Error!")


# Энтер после отжатия
def inLabel1(event):
    if event.keysym == 'Return':
        pr_num = '3.' + str(len(text.get(1.0, END)) - 2)
        text.delete(pr_num)


# удаление всего с клавиатуры после нажатия цифр
def dele(event):
    if (str(text.get(1.0, END))).find('=') == -1:
        pass
    else:
        list_d = '1.' + str((text.get(1.0, END)).rfind('=') + 2)
        text.delete(1.0, list_d)
        text.delete(1.0)


# удаление всего с клавиатуры
def de(event):
    text.delete(1.0, END)


# конфигурации текстового поля (с 3 событиями)
text = Text(width=23, height=3, bg="gray70", fg='gray15', bd=0, font=('Comic Sans MS', 19))
text.focus()
text.place(x=2, y=30)
text.bind('<KeyPress>', inLabel)
text.bind('<KeyRelease>', inLabel1)
text.bind('<Delete>', de)
for i in range(0, 10):
    text.bind(i, dele)

# написание метки над кнопками
my_lbl = Label(text='Бесполезная реклама. Жми!', bg="gray70", fg="grey20", font=('Comic Sans MS', 7))
# my_lbl.place(relx=0, rely=0.30)

tt = ['π', 'CE', 'C', '←',
      '1/x', 'xⁿ', '√х', '/',
      '7', '8', '9', 'X',
      '4', '5', '6', '-',
      '1', '2', '3', '+',
      '+/-', '0', '.', '=']
rx = [0, 0.25, 0.5, 0.75]
ry = [0.34, 0.45, 0.56, 0.67, 0.78, 0.89]


# отображение кнопок
def show_button():
    count = 0
    for k in ry:
        for j in rx:
            if k == 0.89 and j == 0.75:
                cmd = lambda x=count: calc(x)
                but = Button(root, text=tt[count], bg="skyblue3", fg="gray5", command=cmd, font=('arial', 20),
                             overrelief=SUNKEN)
                but.place(relx=[j], rely=[k], height=49, width=88)
                count += 1
            elif k in ry and j == 0.75 or k in [0.34, 0.45] and j in rx:
                cmd = lambda x=count: calc(x)
                but = Button(root, text=tt[count], bg="gray78", fg="gray35", command=cmd, font=('Comic Sans MS', 13),
                             overrelief=RIDGE)
                but.place(relx=[j], rely=[k], height=49, width=88)
                count += 1
            else:
                cmd = lambda x=count: calc(x)
                but = Button(root, text=tt[count], bg="gray92", fg="gray18", command=cmd,
                             font=('Comic Sans MS', 14, "bold"),
                             overrelief=FLAT)
                but.place(relx=[j], rely=[k], height=49, width=88)
                count += 1


show_button()


# отображение кнопок Memory
def show_button_M():
    count = [0, 1, 2, 3, 4]
    rex = [0, 0.25, 0.5, 0.75, 0.873]
    tekst = ['тух', 'MC', 'MR', 'M+', 'M-']
    for i in range(5):
        if i == 3 or i == 4:
            cmdM = lambda x=count[i]: Memory(x)
            but = Button(root, text=tekst[i], bg='gray63', fg='gray3', command=cmdM,
                         font=('Comic Sans MS', 8), overrelief=FLAT)
            but.place(relx=rex[i], rely=0.295, height=20, width=44)
        else:
            cmdM = lambda x=count[i]: Memory(x)
            but = Button(root, text=tekst[i], bg='gray63', fg='gray3', command=cmdM,
                         font=('Comic Sans MS', 8), overrelief=FLAT)
            but.place(relx=rex[i], rely=0.295, height=20, width=88)


Mem = 0


# логика кнопок Memory
def Memory(key):
    global Mem
    all = text.get(1.0, END)
    if key == 0:  # About
        if text.get(1.0, END) == pi:
            text.insert(END, "тух")
        else:
            pass
    elif key == 1:  # MC
        Mem = 0
    elif key == 2:  # MR
        if '=' in all or max(all.rfind('+'), all.rfind('-'), all.rfind('*'),
                             all.rfind('/'), all.rfind('**')) == -1:
            text.delete(1.0, END)
            text.insert(1.0, Mem)
        else:
            list_s = '1.' + str(max(all.rfind('+'), all.rfind('-'), all.rfind('*'), all.rfind('/'),
                                    all.rfind('**')) + 1)
            text.delete(list_s, END)
            text.insert(END, Mem)
    elif key == 3:  # M+
        if text.get(1.0) == "0" and text.get(2.0) != '.':
            try:
                text.delete(1.0)
                Mem += eval(text.get(1.0, END))
            except:
                pass
        elif "=" in all:
            all3 = all.split('\n')
            Mem += eval(all3[1])
        else:
            try:
                result = eval(all)
                Mem += result
            except:
                pass

    elif key == 4:  # M-
        if text.get(1.0) == "0" and text.get(2.0) != '.':
            try:
                text.delete(1.0)
                Mem -= eval(text.get(1.0, END))
            except:
                pass
        elif "=" in all:
            all4 = all.split('\n')
            Mem -= eval(all4[1])
        else:
            try:
                result = eval(all)
                Mem -= result
            except:
                pass

    # запись памяти в калькуляторе
    my_lbl2 = Label(
        text='Memory = ' + str(Mem) + '                                                                              ',
        bg="gray70", fg="grey20", font=('Comic Sans MS', 8))
    my_lbl2.place(relx=0.55, rely=0.25)


show_button_M()
pi = ''


# логика кнопок калькулятора
def calc(key):
    a = text.get(1.0, END)
    global pi
    if key == 23:  # кнопка равно =
        if text.get(1.0) == "0" and text.get(2.0) != '.':
            try:
                text.delete(1.0)
            except:
                pass
        text1 = "-+*./0123456789()"
        if text.get(1.0) not in text1:
            text.insert(END, "Первый символ не число!")
        try:
            result = eval(text.get('1.0', END))
            text.insert(END, "=\n" + str(result))
        except:
            text.insert(END, "Error!")

    elif key == 2:  # кнопка С очистки всего
        text.delete(1.0, END)

    elif key == 20:  # кнопка +/- смена знака
        if "=" in text.get(1.0, END):
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(1.0, '-')
        else:
            if max(a.rfind('+'), a.rfind('-'), a.rfind('*'), a.rfind('/'), a.rfind('**')) != -1:
                list_c = '1.' + str(max(a.rfind('+'), a.rfind('-'), a.rfind('*'), a.rfind('/'), a.rfind('**')))
                try:
                    if text.get(list_c) == "-":
                        text.delete(list_c)
                        if list_c != '1.0':
                            text.insert(list_c, '+')
                    elif text.get(list_c) == '+':
                        text.delete(list_c)
                        text.insert(list_c, '-')
                    else:
                        list_s = '1.' + str(max(a.rfind('+'), a.rfind('-'), a.rfind('*'), a.rfind('/'),
                                                a.rfind('**')) + 1)
                        text.insert(list_s, '(-')
                        text.insert(END, ')')
                except IndexError:
                    pass
            else:
                if text.get(1.0) == '-':
                    text.delete(1.0)
                else:
                    text.insert(1.0, '-')

    elif key == 0:  # кнопка пи
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, 3.14)
            pi = text.get(1.0, END)
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, 3.14)

    elif key == 6:  # кнопка корня
        if (str(text.get(1.0, END))).find('=') == -1:
            try:
                text.delete(1.0, END)
                text.insert(END, '√' + (str(a))[0:-1] + '=\n' + str(math.sqrt(float(a))))
            except:
                pass
        else:
            list_k = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_k)
            text.delete(1.0)
            c = text.get(1.0, END)
            text.delete(1.0, END)
            text.insert(END, "√" + (str(c))[0:-1] + '=\n' + str(math.sqrt(float(c))))

    elif key == 22:  # кнопка . точки
        text.insert(END, '.')
    elif key == 15:  # кнопка - знака минус
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, '-')
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, '-')
    elif key == 19:  # кнопка + знака плюс
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, '+')
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, '+')
    elif key == 11:  # кнопка * знака умножить
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, '*')
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, '*')
    elif key == 7:  # кнопка / знака деления
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, '/')
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, '/')
    elif key == 3:  # кнопка <-- стрелки (удаление последнего знака)
        pr_num = '1.' + str(len(text.get(1.0, END)) - 2)
        text.delete(pr_num)
    elif key == 1:  # кнопка СЕ
        list_c = '1.' + str(max(a.rfind('+'), a.rfind('-'), a.rfind('*'), a.rfind('/'), a.rfind('**')) + 1)
        text.delete(list_c, END)
    elif key == 4:  # кнопка -1 степени (1/ )
        if (str(text.get(1.0, END))).find('=') == -1:
            try:
                text.delete(1.0, END)
                text.insert(END, "1/" + (str(a))[0:-1] + '=\n' + str(1 / float(a)))
            except:
                pass
        else:
            try:
                list_d = '1.' + str(a.rfind('=') + 1)
                text.delete(1.0, list_d)
                text.delete(1.0)
                b = text.get(1.0, END)
                text.delete(1.0, END)
                text.insert(END, "1/" + (str(b))[0:-1] + '=\n' + str(1 / float(b)))
            except:
                pass
    elif key == 5:  # кнопка ** (возведение в n степень)
        if (str(text.get(1.0, END))).find('=') == -1:
            text.insert(END, '**')
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, '**')
            # кнопки цифр
    elif key == 8 or 9 or 10 or 12 or 13 or 14 or 16 or 17 or 18 or 21:
        if "=" in text.get(1.0, END):
            text.delete(1.0, END)
            if key == 8:
                text.insert(END, '7')
            elif key == 9:
                text.insert(END, '8')
            elif key == 10:
                text.insert(END, '9')
            elif key == 12:
                text.insert(END, '4')
            elif key == 13:
                text.insert(END, '5')
            elif key == 14:
                text.insert(END, '6')
            elif key == 16:
                text.insert(END, '1')
            elif key == 17:
                text.insert(END, '2')
            elif key == 18:
                text.insert(END, '3')
            elif key == 21:
                text.insert(END, '0')
        elif key == 8:
            text.insert(END, '7')
        elif key == 9:
            text.insert(END, '8')
        elif key == 10:
            text.insert(END, '9')
        elif key == 12:
            text.insert(END, '4')
        elif key == 13:
            text.insert(END, '5')
        elif key == 14:
            text.insert(END, '6')
        elif key == 16:
            text.insert(END, '1')
        elif key == 17:
            text.insert(END, '2')
        elif key == 18:
            text.insert(END, '3')
        elif key == 21:
            text.insert(END, '0')


mak, leh, dim, art = False, False, False, False
ant, andk, rus, sla2 = False, False, False, False
vla, ali, sla, rom = False, False, False, False
kut, jaz, ant2, art2 = False, False, False, False
dim2, rom2, kut2, leh2 = False, False, False, False
andru, mar, mak2 = False, False, False
andk2, put, mon = False, False, False


# поиск пасхалочек
def supr():
    global suprise, mak, leh, dim, art, ant, andk, rus, vla, ali, sla, rom, kut, jaz, dim2, rom2, kut2, leh2
    global ant2, art2, sla2, andru, mar, mak2, andk2, put, mon, Mem
    alls = (text.get(1.0, END)).lower().split()
    if (alls == ['лучший'] or alls == ['идеальный']) and ant == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-TMYLXkAAH7dk?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Андожка.jpg", "wb") as code:
            code.write(r.content)
        root2 = Toplevel(root)
        root2.title("Андожка")
        img = Image.open("Андожка.jpg")
        w, h = img.size
        root2.geometry(("%dx%d+300+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root2, image=imgtk)
        label.image = imgtk
        label.pack()
        ant = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Андожка.jpg')
        if ant == True and Mem != 777:
            os.remove(path)
    elif (alls == ['14'] or alls == ['fourteen']) and mak == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5oifXYAMcY7B?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Максончык.jpg", "wb") as code:
            code.write(r.content)
        root1 = Toplevel(root)
        root1.title("Максончык")
        img = Image.open("Максончык.jpg")
        w, h = img.size
        root1.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root1, image=imgtk)
        label.image = imgtk
        label.pack()
        mak = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Максончык.jpg')
        if mak == True and Mem != 777:
            os.remove(path)
    elif (alls == ['битка'] or alls == ['куколд']) and mak2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5iOGWsAE_dDJ?format=jpg&name=small'
        r = requests.get(url)
        with open("Мааакс.jpg", "wb") as code:
            code.write(r.content)
        root3 = Toplevel(root)
        root3.title("Я Мааааааааакс, люблю смотреть")
        img = Image.open("Мааакс.jpg")
        w, h = img.size
        root3.geometry(("%dx%d+370+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root3, image=imgtk)
        label.image = imgtk
        label.pack()
        mak2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Мааакс.jpg')
        if mak2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['с++'] or alls == ['по', 'сути'] or alls == ['c++'] or alls == ['си', 'плюс',
                                                                                   'плюс']) and leh == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5iPUWsAAK4Qa?format=jpg&name=small'
        r = requests.get(url)
        with open("Леша.jpg", "wb") as code:
            code.write(r.content)
        root4 = Toplevel(root)
        root4.title("Лёша")
        img = Image.open("Леша.jpg")
        w, h = img.size
        root4.geometry(("%dx%d+330+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root4, image=imgtk)
        label.image = imgtk
        label.pack()
        leh = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Леша.jpg')
        if leh == True and Mem != 777:
            os.remove(path)
    elif (alls == ['¿'] or alls == ['mr', 'крючетти']) and leh2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-T4roXYAIXsWS?format=jpg&name=small'
        r = requests.get(url)
        with open("Лешка.jpg", "wb") as code:
            code.write(r.content)
        root5 = Toplevel(root)
        root5.title("Лёшка")
        img = Image.open("Лешка.jpg")
        w, h = img.size
        root5.geometry(("%dx%d+400+70") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root5, image=imgtk)
        label.image = imgtk
        label.pack()
        leh2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Лешка.jpg')
        if leh2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['no', 'sex', 'club'] or alls == ['virgin', 'club'] or alls == ['club']) and dim == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5dmtXYAIvXVF?format=jpg&name=small'
        r = requests.get(url)
        with open("Димочка.jpg", "wb") as code:
            code.write(r.content)
        root6 = Toplevel(root)
        root6.title("Дима, голубые глаза")
        img = Image.open("Димочка.jpg")
        w, h = img.size
        root6.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root6, image=imgtk)
        label.image = imgtk
        label.pack()
        dim = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Димочка.jpg')
        if dim == True and Mem != 777:
            os.remove(path)
    elif (alls == ['крыница'] or alls == ['балдеж'] or alls == ['балдёж']) and dim2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5oi0X0AAaW-o?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Балдеж.jpg", "wb") as code:
            code.write(r.content)
        root7 = Toplevel(root)
        root7.title("Балдежненько")
        img = Image.open("Балдеж.jpg")
        w, h = img.size
        root7.geometry(("%dx%d+420+5") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root7, image=imgtk)
        label.image = imgtk
        label.pack()
        dim2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Балдеж.jpg')
        if dim2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['ливерпуль'] or alls == ['костел'] or alls == ['ореол']) and ant2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5tUKWoAAmzpz?format=jpg&name=small'
        r = requests.get(url)
        with open("Антон.jpg", "wb") as code:
            code.write(r.content)
        root8 = Toplevel(root)
        root8.title("Эт я")
        img = Image.open("Антон.jpg")
        w, h = img.size
        root8.geometry(("%dx%d+380+20") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root8, image=imgtk)
        label.image = imgtk
        label.pack()
        ant2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Антон.jpg')
        if ant2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['старый', 'грег'] or alls == ['art969'] or alls == ['гражданин', 'земли']) and art2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5dm1XQAAV9CA?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Art969.jpg", "wb") as code:
            code.write(r.content)
        root9 = Toplevel(root)
        root9.title("Citizen of the Earth")
        img = Image.open("Art969.jpg")
        w, h = img.size
        root9.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root9, image=imgtk)
        label.image = imgtk
        label.pack()
        art2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Art969.jpg')
        if art2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['дагестан'] or alls == ['шалом'] or alls == ['врач'] or alls == ['диагност']) and rus == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5ojPX0AYAnDI?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Рус.jpg", "wb") as code:
            code.write(r.content)
        root10 = Toplevel(root)
        root10.title("Рус")
        img = Image.open("Рус.jpg")
        w, h = img.size
        root10.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root10, image=imgtk)
        label.image = imgtk
        label.pack()
        rus = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Рус.jpg')
        if rus == True and Mem != 777:
            os.remove(path)
    elif (alls == ['секретные', 'материалы'] or alls == [
        'боб', 'фоссил'] or alls == ['27']) and andk == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5dmtXkAEbP8T?format=jpg&name=small'
        r = requests.get(url)
        with open("Андрей.jpg", "wb") as code:
            code.write(r.content)
        root11 = Toplevel(root)
        root11.title("Боб Фоссил")
        img = Image.open("Андрей.jpg")
        w, h = img.size
        root11.geometry(("%dx%d+420+20") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root11, image=imgtk)
        label.image = imgtk
        label.pack()
        andk = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Андрей.jpg')
        if andk == True and Mem != 777:
            os.remove(path)
    elif (alls == ['денди'] or alls == ['столичный', 'денди'] or alls == ['мочеступ']) and andk2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-T8OBWkAkUuWK?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Андрюшка.jpg", "wb") as code:
            code.write(r.content)
        root111 = Toplevel(root)
        root111.title("Андрюшка")
        img = Image.open("Андрюшка.jpg")
        w, h = img.size
        root111.geometry(("%dx%d+280+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root111, image=imgtk)
        label.image = imgtk
        label.pack()
        andk2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Андрюшка.jpg')
        if andk2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['илистоп'] or alls == ['колбаска'] or alls == ['или', 'стоп']) and vla == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5tVXX0AEECGz?format=jpg&name=small'
        r = requests.get(url)
        with open("Владик.jpg", "wb") as code:
            code.write(r.content)
        root12 = Toplevel(root)
        root12.title("Владик")
        img = Image.open("Владик.jpg")
        w, h = img.size
        root12.geometry(("%dx%d+380+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root12, image=imgtk)
        label.image = imgtk
        label.pack()
        vla = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Владик.jpg')
        if vla == True and Mem != 777:
            os.remove(path)
    elif (alls == ['маленькая', 'девочка'] or alls == ['сикиляука'] or alls == ['дудец']) and ali == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5iOqXkAAfL8W?format=jpg&name=small'
        r = requests.get(url)
        with open("Алинка.jpg", "wb") as code:
            code.write(r.content)
        root13 = Toplevel(root)
        root13.title("Алинка")
        img = Image.open("Алинка.jpg")
        w, h = img.size
        root13.geometry(("%dx%d+380+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root13, image=imgtk)
        label.image = imgtk
        label.pack()
        ali = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Алинка.jpg')
        if ali == True and Mem != 777:
            os.remove(path)
    elif (alls == ['коричневый'] or alls == ['slut'] or alls == ['гибнут', 'туи']) and sla == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5dmuXgAAtWZx?format=jpg&name=small'
        r = requests.get(url)
        with open("Никита.jpg", "wb") as code:
            code.write(r.content)
        root14 = Toplevel(root)
        root14.title("Сладкий")
        img = Image.open("Никита.jpg")
        w, h = img.size
        root14.geometry(("%dx%d+410+20") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root14, image=imgtk)
        label.image = imgtk
        label.pack()
        sla = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Никита.jpg')
        if sla == True and Mem != 777:
            os.remove(path)
    elif (alls == ['дед'] or alls == ['батон'] or alls == ['сириец']) and rom == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-TXzKX0AQ-uIB?format=jpg&name=small'
        r = requests.get(url)
        with open("Рома.jpg", "wb") as code:
            code.write(r.content)
        root15 = Toplevel(root)
        root15.title("Рома")
        img = Image.open("Рома.jpg")
        w, h = img.size
        root15.geometry(("%dx%d+420+40") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root15, image=imgtk)
        label.image = imgtk
        label.pack()
        rom = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Рома.jpg')
        if rom == True and Mem != 777:
            os.remove(path)
    elif (alls == ['remember'] or alls == ['холодный']) and rom2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-TXxuWkAEGwXV?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Remember.jpg", "wb") as code:
            code.write(r.content)
        root16 = Toplevel(root)
        root16.title("Remember")
        img = Image.open("Remember.jpg")
        w, h = img.size
        root16.geometry(("%dx%d+330+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root16, image=imgtk)
        label.image = imgtk
        label.pack()
        rom2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Remember.jpg')
        if rom2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['кутикс'] or alls == ['кутия']) and kut == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-TXywXYAEC92v?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Кутитич.jpg", "wb") as code:
            code.write(r.content)
        root17 = Toplevel(root)
        root17.title("Кутя")
        img = Image.open("Кутитич.jpg")
        w, h = img.size
        root17.geometry(("%dx%d+280+40") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root17, image=imgtk)
        label.image = imgtk
        label.pack()
        kut = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Кутитич.jpg')
        if kut == True and Mem != 777:
            os.remove(path)
    elif (alls == ['живот', 'болит'] or alls == ['ховард'] or alls == ['кутитич']) and kut2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5oiBXgAkSALn?format=jpg&name=900x900'
        r = requests.get(url)
        with open("ХовардМун.jpg", "wb") as code:
            code.write(r.content)
        root18 = Toplevel(root)
        root18.title("Кутитич")
        img = Image.open("ХовардМун.jpg")
        w, h = img.size
        root18.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root18, image=imgtk)
        label.image = imgtk
        label.pack()
        kut2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ХовардМун.jpg')
        if kut2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['47']) and jaz == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-Tch2XkAYjyD5?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Язда.jpg", "wb") as code:
            code.write(r.content)
        root19 = Toplevel(root)
        root19.title("Язда")
        img = Image.open("Язда.jpg")
        w, h = img.size
        root19.geometry(("%dx%d+280+40") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root19, image=imgtk)
        label.image = imgtk
        label.pack()
        jaz = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Язда.jpg')
        if jaz == True and Mem != 777:
            os.remove(path)
    elif (alls == ['3.14тух']) and sla2 == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5iO8XYAI9sNr?format=jpg&name=small'
        r = requests.get(url)
        with open("Сладость.jpg", "wb") as code:
            code.write(r.content)
        root20 = Toplevel(root)
        root20.title("Сладость")
        img = Image.open("Сладость.jpg")
        w, h = img.size
        root20.geometry(("%dx%d+380+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root20, image=imgtk)
        label.image = imgtk
        label.pack()
        sla2 = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Сладость.jpg')
        if sla2 == True and Mem != 777:
            os.remove(path)
    elif (alls == ['лук'] or alls == ['onion']) and art == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY-TMWHXkAYgAn6?format=jpg&name=small'
        r = requests.get(url)
        with open("Тема.jpg", "wb") as code:
            code.write(r.content)
        root21 = Toplevel(root)
        root21.title("Тёма")
        img = Image.open("Тема.jpg")
        w, h = img.size
        root21.geometry(("%dx%d+430+80") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root21, image=imgtk)
        label.image = imgtk
        label.pack()
        art = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Тема.jpg')
        if art == True and Mem != 777:
            os.remove(path)
    elif (alls == ['путин', 'молодец']) and put == False:
        url = 'https://pbs.twimg.com/media/EY-T4sWWsAMOUIQ?format=jpg&name=900x900'
        r = requests.get(url)
        with open("WellDone.jpg", "wb") as code:
            code.write(r.content)
        root25 = Toplevel(root)
        root25.title("Роиииссия!")
        img = Image.open("WellDone.jpg")
        w, h = img.size
        root25.geometry(("%dx%d+350+160") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root25, image=imgtk)
        label.image = imgtk
        label.pack()
        put = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'WellDone.jpg')
        if put == True and Mem != 777:
            os.remove(path)
    elif (alls == ['мармыли'] or alls == ['мармули']) and mar == False:
        suprise += 1
        url = 'https://pbs.twimg.com/media/EY_5tVnX0AMvfcI?format=jpg&name=small'
        r = requests.get(url)
        with open("Мармули.jpg", "wb") as code:
            code.write(r.content)
        root22 = Toplevel(root)
        root22.title("Мармули")
        img = Image.open("Мармули.jpg")
        w, h = img.size
        root22.geometry(("%dx%d+420+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root22, image=imgtk)
        label.image = imgtk
        label.pack()
        mar = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Мармули.jpg')
        if mar == True and Mem != 777:
            os.remove(path)
    elif (alls == ['сиськи', 'андрея'] or suprise == 15) and andru == False:
        url = 'https://pbs.twimg.com/media/EY-TumAX0AELFSP?format=jpg&name=900x900'
        r = requests.get(url)
        with open("Сиськи.jpg", "wb") as code:
            code.write(r.content)
        root23 = Toplevel(root)
        root23.title("Андрюшка")
        img = Image.open("Сиськи.jpg")
        w, h = img.size
        root23.geometry(("%dx%d+250+50") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root23, image=imgtk)
        label.image = imgtk
        label.pack()
        andru = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Сиськи.jpg')
        if andru == True and Mem != 777:
            os.remove(path)
    elif (alls == ['моника']) and mon == False:
        url = 'https://cdn.fishki.net/upload/post/201512/24/1788337/tkdcnzn0kog.jpg'
        r = requests.get(url)
        with open("Моника.jpg", "wb") as code:
            code.write(r.content)
        root29 = Toplevel(root)
        root29.title("Моника")
        img = Image.open("Моника.jpg")
        w, h = img.size
        root29.geometry(("%dx%d+400+30") % (w, h))
        imgtk = ImageTk.PhotoImage(img)
        label = Label(root29, image=imgtk)
        label.image = imgtk
        label.pack()
        mon = True
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Моника.jpg')
        if mon == True and Mem != 777:
            os.remove(path)

    text.after(450, supr)
    # написание метки по гайду
    gaide_lbl = Label(text='Найдено ☺ = ' + str(suprise) + ' (23)', bg="gray70", fg="grey20", font=('Comic Sans MS', 9))
    gaide_lbl.place(x=100, y=3)

    
# функция для поиска П
supr()

root.mainloop()

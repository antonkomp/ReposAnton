# my calculator exe
from tkinter import *
from tkinter import messagebox
import math

# кофигурации основного окна
root = Tk()
root.title('My calculator')
root.geometry('360x460+450+250')
root.resizable(False, False)
root.attributes("-alpha", 0.92)
root["bg"] = "gray70"
message = StringVar()


# вывод нового окна
def show_message():
    messagebox.showwarning("Риторический вопрос", 'Слат питух!                 ')


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


# конпка про слата
but_o_progr = Button(text='Слат питух?', command=show_message, bg="grey70", fg="grey20", font=('Comic Sans MS', 8))
# but_o_progr.place(x=3, y=2)

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
                but = Button(root, text=tt[count], bg="gray82", fg="gray35", command=cmd, font=('Comic Sans MS', 13),
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
    tekst = ['About', 'MC', 'MR', 'M+', 'M-']
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
        text.delete(1.0, END)
        text.insert(1.0, "This is the program of          Anton Baranau.                      Do not mention it!")
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
        bg="gray70", fg="grey20", font=('Comic Sans MS', 11))
    my_lbl2.place(relx=0, rely=0)


show_button_M()


# логика кнопок калькулятора
def calc(key):
    a = text.get(1.0, END)
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
            text.insert(END, math.pi)
        else:
            list_d = '1.' + str(a.rfind('=') + 1)
            text.delete(1.0, list_d)
            text.delete(1.0)
            text.insert(END, math.pi)

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


root.mainloop()

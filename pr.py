from tkinter import Tk, Button, Label, SUNKEN, LEFT, \
    StringVar, Radiobutton, RIDGE, GROOVE, messagebox, Toplevel, \
    Canvas, CENTER, Text, END, Scrollbar, Y, FLAT
import random
import re
import math
import requests
import os

def main():  # главная функция
    rootM = Tk()
    rootM.title('Экзаменационный тест СофтКорп')
    rootM.geometry('1000x700')
    rootM.state('zoomed')
    rootM['bg'] = 'gray80'
    rootM.iconbitmap('iconframe.ico')

    def test():  # логика всего теста
        rootM.destroy()
        WindowTest = Tk()
        WindowTest.title('Тест')
        WindowTest.geometry('1000x700')
        WindowTest.state('zoomed')
        WindowTest.iconbitmap('iconframe.ico')
        WindowTest['bg'] = 'gray94'

        # array - список с вопросами
        # array2 - список с вариантами ответа
        with open('que.txt', 'r') as quest:
            array = quest.read().split('\n')
        main_list = []
        all_ques = 100
        while len(main_list) < all_ques:  # записываем рандомные не повторяющиеся вопросы
            Number = random.randrange(0, 400)
            if array[Number] not in main_list:
                main_list.append(array[Number])

        result = []  # номер вопроса
        for i in range(all_ques):
            len_row = 124
            if len(main_list[i]) >= 124:
                indents = len(main_list[i]) // len_row  # количество строк в вопросе
                for j in range(indents):  # создаем перенос строк
                    num_space = main_list[i][:len_row].rfind(' ')
                    main_list[i] = main_list[i][:num_space] + '\n' + main_list[i][num_space:]
                    len_row += 124
            else:
                main_list[i] = main_list[i] + '\n'

            result.append(re.match(r'\d{,3}\W', main_list[i]))
            main_list[i] = '    ' + re.sub(result[i].group(0), (str(i + 1) + '.'), main_list[i])
            # созданы итоговые вопросы с нумерацией от 1 в main_list[i]

        with open('ans.txt', 'r') as ans:  # считываем варианты ответа
            array2 = ans.read().split('\n')
        resfind = []
        resnext = []
        search_index = []
        differ = []
        next_index = []

        for i2 in range(all_ques):
            resfind.append(result[i2].group(0)[:-1] + '***')  # записываем все строки с нужным номером вопроса и '***'
            search_index.append(array2.index(resfind[i2]))  # поиск индекса нужного вопроса в списке вариантов
            resnext.append(str(int(result[i2].group(0)[:-1]) + 1) + '***')  # записываем следующий номер с '***'
            if resnext[i2] in array2:  # есть ли next вопрос в списке вариантов, если да:
                next_index.append(array2.index(resnext[i2]))  # индекс следующего вопроса
                differ.append(next_index[i2] - search_index[i2] - 1)
            else:
                differ.append(3)
                next_index.append(-1)

        QuesLabel = Label(WindowTest, text=main_list[0], bg='gray94', font=('Ariel', 14), justify=LEFT)
        QuesLabel.place(relx=0.03, rely=0.04, relwidth=0.94)

        SI = search_index[0]
        rely1 = 0.25
        var = StringVar(value='404')

        MemoryTrue = 0
        MemoryFalse = 0
        dict_test_true = {}
        dict_test_false = {}
        main_list_edit = main_list[:]

        def exit():
            label.destroy()
            total = Toplevel(WindowTest)
            total.title("Результаты теста")
            total.geometry('500x600+400+90')
            total.resizable(False, False)
            total['bg'] = 'gray90'
            res_label = Label(total, text='''                \nРезультаты теста''', font=('Ariel', 17),
                              bg='gray90')
            res_label.pack()
            text_res = '\nПоздравляю, Вы набрали ' + str(len(dict_test_true)) + ' из 100\n\n'
            res_label = Label(total, text=text_res, font=('Ariel', 15),
                              bg='gray90')
            res_label.pack()
            c = Canvas(total, width=330, height=230, bg='gray83')
            c.pack()
            c.create_oval(20, 20, 210, 210, fill='lightgrey', outline='white')
            right = len(dict_test_true) * 3.6
            c.create_arc(20, 20, 210, 210, start=0, extent=right, fill='green2')
            wrong = 0 - (360 - right)
            c.create_arc(20, 20, 210, 210, start=0, extent=wrong, fill='red')

            c.create_oval(235, 50, 250, 65, fill='green2')
            opred1 = '- ' + str(len(dict_test_true)) + '\n  верно'
            c.create_text(275, 66, text=opred1, justify=CENTER, font="Verdana 11")
            c.create_oval(235, 110, 250, 125, fill='red')
            opred2 = ' - ' + str(100 - len(dict_test_true)) + '\n не верно'
            c.create_text(275, 126, text=opred2, justify=CENTER, font="Verdana 11")
            unsure = (MemoryTrue - len(dict_test_true)) + (MemoryFalse - len(dict_test_false))
            opred3 = '* неуверенных\n ответов - ' + str(unsure)
            c.create_text(260, 195, text=opred3, justify=CENTER, font="Verdana 11")

            def show_right_answer():
                Win_correct = Toplevel(total)
                Win_correct.title('Correct answers')
                Win_correct.geometry('1000x700')
                Win_correct.state('zoomed')
                Win_correct['bg'] = 'gray90'
                text1 = Text(Win_correct, width=88, height=51, bg="gray95", fg='gray15', bd=1, font=('Ariel', 12))
                text1.focus()
                text1.place(relx=0.202, rely=0.02)
                text1.insert(1.0,
                             '\n     №               Вопрос             >             ВЕРНЫЙ ОТВЕТ ПОЛЬЗОВАТЕЛЯ\n\n')
                for key, val in dict_test_true.items():
                    variable = ('{} > {}\n\n'.format(key, val.upper()))
                    text1.insert(END, variable)
                scrollbar1 = Scrollbar(Win_correct)
                scrollbar1.pack(side='right', fill=Y)
                scrollbar1.config(command=text1.yview)
                text1.config(yscrollcommand=scrollbar1.set)
                Win_correct.mainloop()

            right_answer = Button(total, text='Show correct answers', font=('Comic Sans MS', 13),
                                  bg='green yellow', command=show_right_answer, overrelief=SUNKEN, cursor='hand2')
            right_answer.place(x=40, y=440)

            def show_wrong_answer():
                Win_wrong = Toplevel(total)
                Win_wrong.title('Wrong answers')
                Win_wrong.geometry('1000x700')
                Win_wrong.state('zoomed')
                Win_wrong['bg'] = 'gray90'
                text2 = Text(Win_wrong, width=88, height=51, bg="gray95", fg='gray15', bd=1,
                             font=('Ariel', 12))
                text2.focus()
                text2.place(relx=0.202, rely=0.02)
                text2.insert(1.0,
                             '\n     №               Вопрос             >             НЕВЕРНЫЙ ОТВЕТ ПОЛЬЗОВАТЕЛЯ\n\n')
                for key, val in dict_test_false.items():
                    variable = ('{} > {}\n\n'.format(key, val.upper()))
                    text2.insert(END, variable)
                scrollbar2 = Scrollbar(Win_wrong)
                scrollbar2.pack(side='right', fill=Y)
                scrollbar2.config(command=text2.yview)
                text2.config(yscrollcommand=scrollbar2.set)
                Win_wrong.mainloop()

            wrong_answer = Button(total, text='Show wrong answers', font=('Comic Sans MS', 13),
                                  bg='firebrick2', command=show_wrong_answer, overrelief=SUNKEN, cursor='hand2')
            wrong_answer.place(x=280, y=440)

            def main_again():
                WindowTest.destroy()
                main()

            start = Button(total, text='Start again', font=('Comic Sans MS', 13),
                           bg='gray95', command=main_again, overrelief=SUNKEN, cursor='hand2')
            start.place(x=203, y=505)

            total.mainloop()

        def rad_def():
            nonlocal MemoryTrue, MemoryFalse, Nomer, dict_test_true, dict_test_false, main_list_edit
            Zna = var.get()
            NumberDog = Zna.find('@') + 1
            RX = [(0.01 + i * 0.032) for i in range(25)] * 4
            RY = [0.752] * 25 + [0.798] * 25 + [0.844] * 25 + [0.89] * 25

            while main_list_edit[Nomer].find('\n') != -1:
                Sleshn = main_list_edit[Nomer].find('\n')
                main_list_edit[Nomer] = main_list_edit[Nomer][:Sleshn] + main_list_edit[Nomer][Sleshn + 1:]
            if '\t\t' in Zna:
                MemoryTrue += 1
                cmd = lambda x=Nomer: question(x)
                AnsButton = Button(WindowTest, text=count_but[Nomer], bg='green3', command=cmd,
                                   font=('Ariel', 11), overrelief=RIDGE, cursor="hand2")
                AnsButton.place(relx=RX[Nomer], rely=RY[Nomer], height=35, width=40)
                if main_list_edit[Nomer] in dict_test_false:
                    del dict_test_false[main_list_edit[Nomer]]
                    dict_test_true[main_list_edit[Nomer]] = Zna[NumberDog:-2]
                else:
                    dict_test_true[main_list_edit[Nomer]] = Zna[NumberDog:-2]
            else:
                MemoryFalse += 1
                cmd = lambda x=Nomer: question(x)
                AnsButton = Button(WindowTest, text=count_but[Nomer], bg='green3', command=cmd,
                                   font=('Ariel', 11), overrelief=RIDGE, cursor="hand2")
                AnsButton.place(relx=RX[Nomer], rely=RY[Nomer], height=35, width=40)

                if main_list_edit[Nomer] in dict_test_true:
                    del dict_test_true[main_list_edit[Nomer]]
                    dict_test_false[main_list_edit[Nomer]] = Zna[NumberDog:]
                else:
                    dict_test_false[main_list_edit[Nomer]] = Zna[NumberDog:]

            if len(dict_test_true) + len(dict_test_false) == 100:
                exit()

        SI_T = search_index[0]
        for k in range(differ[0]):
            SI += 1
            val = (str(SI_T) + '@' + array2[SI])
            radiobut = Radiobutton(WindowTest, text=array2[SI], activebackground='gray94', wraplength=1130,
                                   variable=var, value=val, bg='gray94', font=('Ariel', 14),
                                   command=rad_def, indicatoron=2)

            radiobut.place(relx=0.05, rely=rely1)
            rely1 += 0.05
        Nomer = 0

        def question(num):
            nonlocal Nomer
            Nomer = num
            l1 = 0.04
            text_clear = '  ' * 210
            for clear in range(6):
                labl_clear = Label(WindowTest, text=text_clear, bg='gray94')
                labl_clear.place(relx=0.01, rely=l1)
                l1 += 0.02

            QuesLabel = Label(WindowTest, text=main_list[num], bg='gray94', font=('Ariel', 14), justify=LEFT)
            QuesLabel.place(relx=0.03, rely=0.04, relwidth=0.94)
            rely1 = 0.25
            r1 = 0.26
            SI = search_index[num]
            SI_T = search_index[num]

            for clear in range(13):
                radb_clear = Label(WindowTest, text=text_clear, bg='gray94')
                radb_clear.place(relx=0.05, rely=r1)
                r1 += 0.02
            for k in range(differ[num]):
                SI += 1
                val = (str(SI_T) + '@' + array2[SI])
                radiobut = Radiobutton(WindowTest, text=array2[SI], activebackground='gray94', wraplength=1130,
                                       variable=var, value=val, bg='gray94', font=('Ariel', 14), command=rad_def)
                radiobut.place(relx=0.05, rely=rely1)
                rely1 += 0.05

        # функция показа кнопок вопросов
        count_but = [str(i) for i in range(1, 101)]
        rx = [(0.01 + i * 0.032) for i in range(25)]
        ry = [0.752, 0.798, 0.844, 0.890]

        def ShowAnsButton():
            count = 0
            for k in ry:
                for j in rx:
                    cmd = lambda x=count: question(x)
                    AnsButton = Button(WindowTest, text=count_but[count], bg='red', command=cmd,
                                       font=('Ariel', 11), overrelief=RIDGE, cursor="hand2")
                    AnsButton.place(relx=[j], rely=[k], height=35, width=40)
                    count += 1

        ShowAnsButton()

        # метка линия снизу
        LineString = '_' * 280
        line_labal = Label(WindowTest, text=LineString, bg='gray94')
        line_labal.place(relx=0, rely=0.72)

        # метка линия сверху
        LineString = '_' * 280
        line_labal = Label(WindowTest, text=LineString, bg='gray94')
        line_labal.place(relx=0, rely=0.17)

        # метка линия самая нижняя
        LineString = '_ ' * 180
        line_labal = Label(WindowTest, text=LineString, bg='gray94')
        line_labal.place(relx=0, rely=0.932)

        # метка линия самая нижняя
        LineString = 'SoftCorp'
        line_labal = Label(WindowTest, text=LineString, bg='gray94', font=('Ariel', 12))
        line_labal.place(relx=0.49, rely=0.96)

        def ToChoice():  # кнопка на следующий вопрос
            ToChoiceButton = Button(WindowTest, text='Следующий вопрос', font=('Ariel', 14),
                                    bg='yellow2', fg='green4', overrelief=GROOVE, command=next, cursor="hand2")
            ToChoiceButton.place(anchor='se', relx=0.98, rely=0.82, height=50, width=190)

        def next():
            nonlocal Nomer
            if Nomer < 99:
                Nomer += 1
                l1 = 0.04
                text_clear = '  ' * 210
                for clear in range(6):
                    labl_clear = Label(WindowTest, text=text_clear, bg='gray94')
                    labl_clear.place(relx=0.01, rely=l1)
                    l1 += 0.02

                QuesLabel = Label(WindowTest, text=main_list[Nomer], bg='gray94', font=('Ariel', 14), justify=LEFT)
                QuesLabel.place(relx=0.03, rely=0.04, relwidth=0.94)
                rely1 = 0.25
                r1 = 0.26
                SI = search_index[Nomer]
                SI_T = search_index[Nomer]

                for clear in range(13):
                    radb_clear = Label(WindowTest, text=text_clear, bg='gray94')
                    radb_clear.place(relx=0.05, rely=r1)
                    r1 += 0.02
                for k in range(differ[Nomer]):
                    SI += 1
                    val = (str(SI_T) + '@' + array2[SI])
                    radiobut = Radiobutton(WindowTest, text=array2[SI], activebackground='gray94', wraplength=1130,
                                           variable=var, value=val, bg='gray94', font=('Ariel', 14), command=rad_def)
                    radiobut.place(relx=0.05, rely=rely1)
                    rely1 += 0.05
            else:
                pass

        ToChoice()

        def ToEnd():  # кнопка завершить тест
            ToChoiceButton = Button(WindowTest, text='Завершить', font=('Ariel', 14), bg='gray40',
                                    fg='red3', overrelief=SUNKEN, command=Over, cursor="hand2")
            ToChoiceButton.place(anchor='se', relx=0.96, rely=0.91, height=50, width=140)

        def Over():
            def show_ask():
                res = messagebox.askyesno('Тест', 'Вы уверены, что хотите завершить тест раньше?')
                if res == True:
                    exit()
                else:
                    pass

            show_ask()

        ToEnd()

        def Calculator():
            Calc = Button(WindowTest, text='Калькулятор', font=('Ariel', 12), bg='gray94',
                          overrelief=SUNKEN, command=TheCalc, cursor='hand2')
            Calc.place(anchor='center', relx=0.5, rely=0.7)

        def TheCalc():


            # кофигурации основного окна
            root = Tk()
            root.title('Калькулятор')
            root.geometry('360x460+450+250')
            root.resizable(False, False)
            root.attributes("-alpha", 0.94)
            root["bg"] = "gray70"

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
            text = Text(root, width=23, height=3, bg="gray70", fg='gray15', bd=0, font=('Comic Sans MS', 19))
            text.focus()
            text.place(x=2, y=30)
            text.bind('<KeyPress>', inLabel)
            text.bind('<KeyRelease>', inLabel1)
            text.bind('<Delete>', de)
            for i in range(0, 10):
                text.bind(i, dele)

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
                            but = Button(root, text=tt[count], bg="skyblue3", fg="gray5", command=cmd,
                                         font=('arial', 20),
                                         overrelief=SUNKEN)
                            but.place(relx=[j], rely=[k], height=49, width=88)
                            count += 1
                        elif k in ry and j == 0.75 or k in [0.34, 0.45] and j in rx:
                            cmd = lambda x=count: calc(x)
                            but = Button(root, text=tt[count], bg="gray78", fg="gray35", command=cmd,
                                         font=('Comic Sans MS', 13),
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
                tekst = ['None', 'MC', 'MR', 'M+', 'M-']
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
                nonlocal Mem
                all = text.get(1.0, END)
                if key == 0:  # About
                    if text.get(1.0, END) == pi:
                        pass
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
                my_lbl2 = Label(root,
                    text='Memory = ' + str(
                        Mem) + '                                                                              ',
                    bg="gray70", fg="grey20", font=('Comic Sans MS', 8))
                my_lbl2.place(relx=0.55, rely=0.25)

            show_button_M()
            pi = ''

            # логика кнопок калькулятора
            def calc(key):
                a = text.get(1.0, END)
                nonlocal pi
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
                            list_c = '1.' + str(
                                max(a.rfind('+'), a.rfind('-'), a.rfind('*'), a.rfind('/'), a.rfind('**')))
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

            root.mainloop()

        Calculator()

        # функция таймера в тесте
        def show_timeover():
            messagebox.showinfo('Время теста вышло', 'Но можно продолжить!')

        S = 2399
        m = 40
        s = 0

        def tick_tack():
            nonlocal label, S, m, s
            if m == 0 and s == 0:
                show_timeover()
            elif m >= 0 and s >= 10:
                label.config(text='{0}:{1}'.format(m, s))
            elif m >= 0 and s // 10 <= 1:
                label.config(text='{0}:{1}'.format(m, ('0' + str(s))))
            else:
                label.config(text='0:00')
            m = S // 60
            s = S % 60
            S -= 1
            if label.winfo_exists() == 1:
                label.after(1000, tick_tack)

        label = Label(WindowTest, text="00:00", font="Arial 14", bg="gray94", fg="red")  # делаем метку на окне root
        label.place(relx=0.88, rely=0.7)
        label.after_idle(tick_tack)

        WindowTest.mainloop()

    # кнопка начала теста
    MainButton = Button(text='Начать тест', command=test, font=('Ariel', 27),
                        overrelief=SUNKEN, bg='light slate grey', fg='gray94', cursor="hand2")
    MainButton.place(anchor='center', relx=0.5, rely=0.5)

    def Help():
        messagebox.showinfo('Help', '  Тест создан для проверки знаний работников лайва, '
                                    'по вопросам находящихся в общем доступе. Вопросы могут быть не все, '
                                    'например те, что идут с изображением, т.к. их нельзя получить.\n'
                                    '  Программу можно использовать в своих целях на любом компьютере.'
                                    ' Время на тест - 40 минут, но по его окончанию можно продолжить.\n\n'
                                    '  Замечания/предложения пишите на почту: antonkomp@gmail.com.')

    # кнопка Help
    HelpButton = Button(text='Help', command=Help, font=('Ariel', 14), bg='red3', fg='gray94', cursor="hand2")
    HelpButton.place(anchor='se', relx=0.97, rely=0.97, height=40, width=90)

    rootM.mainloop()


if __name__ == "__main__":
    main()

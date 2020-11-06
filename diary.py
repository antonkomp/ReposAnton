from tkinter import Tk, Button, Label, Entry, LabelFrame, W, FLAT, messagebox, Text, END, Listbox, ANCHOR, WORD
import sqlite3
from datetime import datetime


def main():
    # window diary
    def main_window():
        user_login = login.get()
        user_password = password.get()
        root.destroy()
        diary = Tk()
        diary.title('My diary')
        x = (diary.winfo_screenwidth() - 920) / 2
        y = (diary.winfo_screenheight() - 560) / 2
        diary.wm_geometry("+%d+%d" % (x, y))
        diary.geometry('920x560')
        diary.resizable(False, False)
        diary['bg'] = 'gray50'

        table_name = str(user_login) + str(user_password)
        sql_request = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL DEFAULT 1111,
                password TEXT NOT NULL DEFAULT 1111,
                date TEXT,
                name TEXT DEFAULT no_name,
                text TEXT)"""
        cursor.execute(sql_request)
        db.commit()

        list_records = Listbox(diary, width=38, height=18, bg="gray80", bd=1, fg='gray10', font=('Comic Sans MS', 9))
        list_records.place(x=21, y=166)

        count_record = 0
        for i in cursor.execute(f'SELECT id, date, name FROM {table_name}'):
            list_records.insert(0, i)
            count_record += 1

        journal_label = Label(diary, text=f"Журнал записей (всего: {count_record})", bg='gray50',
                              font=('Comic Sans MS', 11))
        journal_label.place(x=26, y=125)

        list_label = Label(diary, text="№                   Дата                  Название", bg='gray50',
                           font=('Comic Sans MS', 7))
        list_label.place(x=22, y=147)

        name_label = Label(diary, text="Название:", bg='gray50', font=('Comic Sans MS', 11))
        name_label.place(x=315, y=125)

        name = Entry(diary, bd=3, bg='gray90', width=58, font=('Comic Sans MS', 12))
        name.place(x=310, y=150)

        text_label = Label(diary, text="Текст:", bg='gray50', font=('Comic Sans MS', 11))
        text_label.place(x=315, y=185)

        text = Text(diary, width=58, height=12, bg="gray90", fg='gray15', bd=3, font=('Comic Sans MS', 12), wrap=WORD)
        text.focus()
        text.place(x=310, y=210)

        def save():
            nonlocal count_record
            time = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
            cursor.execute(f"INSERT INTO {table_name} (login, password, date, name, text) VALUES (?, ?, ?, ?, ?)",
                           (user_login, user_password, time, name.get(), text.get('1.0', END)))
            db.commit()
            list_records.delete(0, END)
            count_record = 0
            for i in cursor.execute(f'SELECT id, date, name FROM {table_name}'):
                list_records.insert(0, i)
                count_record += 1
            journal_label = Label(diary, text=f"Журнал записей (всего: {count_record})", bg='gray50',
                                  font=('Comic Sans MS', 11))
            journal_label.place(x=26, y=125)

        save_button = Button(diary, text='Сохранить', command=save, font=('Comic Sans MS', 11),
                             bg='green3', fg='white', overrelief=FLAT, cursor="hand2")
        save_button.place(x=780, y=508)

        def delete():
            nonlocal count_record
            date_rec = list_records.get(ANCHOR)
            result = messagebox.askyesno('My diary', f'Вы действительно хотите удалить запись "{date_rec[0]}"?')
            if result == True:
                try:
                    cursor.execute(f'DELETE FROM {table_name} WHERE id = {date_rec[0]}')
                    db.commit()
                    list_records.delete(ANCHOR)
                    count_record -= 1

                    journal_label = Label(diary, text=f"Журнал записей (всего: {count_record})", bg='gray50',
                                          font=('Comic Sans MS', 11))
                    journal_label.place(x=26, y=125)
                except Exception:
                    pass

        delete_button = Button(diary, text='Удалить', command=delete, font=('Comic Sans MS', 11),
                               bg='red', fg='white', overrelief=FLAT, cursor="hand2")
        delete_button.place(x=70, y=508)

        def open():
            date_rec = list_records.get(ANCHOR)
            for i in cursor.execute(f'SELECT name FROM {table_name} WHERE id = {date_rec[0]}'):
                name.delete(0, END)
                n = str(i)
                name.insert(0, n[2:-3])

            for i in cursor.execute(f'SELECT text FROM {table_name} WHERE id = {date_rec[0]}'):
                text.delete(1.0, END)
                string = str(i)
                num = string.count(r'\n') + 1
                text.insert(1.0, i)
                text.delete(1.0)
                text.delete(f'{num}.0')

        open_button = Button(diary, text='Открыть', command=open, font=('Comic Sans MS', 11),
                             bg='green3', fg='white', overrelief=FLAT, cursor="hand2")
        open_button.place(x=170, y=508)

        diary.mainloop()

    # function to registration in diary
    def entrance():
        user_login = login.get()
        user_password = password.get()
        if len(user_login) < 4 or len(user_password) < 4:
            messagebox.showinfo('Внимание', 'Длина логина или пароля меньше 4 символов!')
        else:
            cursor.execute(
                f"SELECT login, password FROM users WHERE login = '{user_login}' AND password = '{user_password}'")
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (user_login, user_password))
                db.commit()
            main_window()

    root = Tk()
    root.title('My diary')
    x = (root.winfo_screenwidth() - 920) / 2
    y = (root.winfo_screenheight() - 560) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    root.geometry('920x560')
    root.resizable(False, False)
    root['bg'] = 'gray50'

    with sqlite3.connect('db_diary.db') as db:
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL DEFAULT 1111,
            password TEXT NOT NULL DEFAULT 1111)"""
        cursor.execute(sql)
        db.commit()

    login_frame = LabelFrame(root, padx=10, pady=10, text='Вход', bg='gray50', font=('Comic Sans MS', 11))
    login_frame.pack(padx=0, pady=200)
    Label(login_frame, text="Логин", bg='gray50', font=('Comic Sans MS', 9)).grid(row=0)
    Label(login_frame, text="Пароль", bg='gray50', font=('Comic Sans MS', 9), pady=7).grid(row=1)
    login = Entry(login_frame, font=('Comic Sans MS', 11))
    login.grid(row=0, column=1, columnspan=2, sticky=W)
    password = Entry(login_frame, font=('Comic Sans MS', 11), show='*')
    password.grid(row=1, column=1, columnspan=2, sticky=W)
    Button(login_frame, text='Войти', command=entrance, font=('Comic Sans MS', 10),
           bg='green3', fg='white', width=6, overrelief=FLAT, cursor="hand2").grid(row=2, column=2, sticky=W)

    root.mainloop()


if __name__ == '__main__':
    main()

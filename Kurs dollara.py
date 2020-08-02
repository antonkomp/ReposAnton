import requests
from bs4 import BeautifulSoup
import warnings
from tkinter import *

warnings.filterwarnings('ignore')

clicks = 0


def click_button():
    global clicks
    clicks += 1
    buttonText.set("Просмотрено {} раз".format(clicks))
    

url = "https://finance.tut.by/kurs/"

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.findAll('table', class_='tbl-lite rates-table')
td = table[0].findAll('div', class_='b-course')
buy = 'Курс доллара в Минске (покупка): ' + td[0].text[2:8]
sale = 'Курс доллара в Минске (продажа): ' + td[1].text[2:8]

root = Tk()
root.title('Мой курс $ в Минске')
root.geometry('400x300+200+200')
buttonText = StringVar()
buttonText.set("Посмотреть курс $".format(clicks))
btn = Button(textvariable=buttonText,
             background='#777',
             foreground='#ccc',
             padx='25',
             pady='10',
             font='16',
             command=click_button)
btn.place(x=100, y=100)

label1 = Label(text=buy, justify=CENTER)
label1.pack()
label1 = Label(text=sale, justify=CENTER)
label1.pack()
root.mainloop()

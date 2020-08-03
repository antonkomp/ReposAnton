# Функция скачивания изображений

import datetime
import urllib.request
names = []

def download_img(url):
    name = datetime.datetime.today().strftime("%y-%m-%d--%H-%M-%S")
    name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, name)


download_img("https://pbs.twimg.com/media/EY-T8OBWkAkUuWK?format=jpg&name=900x900", )
download_img("https://pbs.twimg.com/media/EY-T4rGXgAEDO5I?format=jpg&name=900x900")


#https://drive.google.com/open?id=1Xxjj3gtFz9Z0-nlNJ7YMzNffJq25fujf
# 1 Проверка на неповторимость имен https://avatars.yandex.net/get-music-content/34131/d66519a2.a.950889-1/m1000x1000
# 2 При ошибке с адресом картинки брать новую или останавливать программу (try except)
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
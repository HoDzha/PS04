import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#assert "Википедия" in browser.title

paragraphs = browser.find_elements(By.TAG_NAME, "p")
#Для перебора пишем цикл
for paragraph in paragraphs:
    print(paragraph.text)
    input()

# hatnotes = []
# for element in browser.find_elements(By.TAG_NAME, "div"):
# #Чтобы искать атрибут класса
#     cl = element.get_attribute("class")
#     if cl == "hatnote navigation-not-searchable":
#         hatnotes.append(element)
#
# print(hatnotes)
# hatnote = random.choice(hatnotes)
#
# #Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
# link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
# browser.get(link)
# time.sleep(10)
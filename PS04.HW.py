# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# 3.1 листать параграфы текущей статьи;
# 3.2 перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#     3.2.1  - листать параграфы статьи;
#     3.2.2  - перейти на одну из внутренних статей.
# 3.3 выйти из программы.

import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
def print_paragraphs(page):
    # Листаем параграфы
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Для перебора пишем цикл
    # for paragraph in paragraphs:
    #     print(paragraph.text)
    for i, para in enumerate(paragraphs, 1):
        print(f"\nПараграф {i}:")
        print(para.text.strip())
        if i % 2 == 0:  # Показываем по 2 параграфа за раз
            choice = input("\nПродолжить чтение? (y/n): ")
            if choice.lower() != 'y':
                break
def show_links(page):
    # Показываем связанные страницы

def find_wiki(query):
    #функция для поиска в википедии
    result = browser.find_element(By.ID, query)

def main():
    #главная функция программы
    query = input("\nВведите запрос для поиска на Википедии: ")
    page = find_wiki(query)

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Для перебора пишем цикл
    # for paragraph in paragraphs:
    #     print(paragraph.text)
for i, para in enumerate(paragraphs, 1):
    print(f"\nПараграф {i}:")
    print(para.text.strip())
    if i % 2 == 0:  # Показываем по 2 параграфа за раз
        choice = input("\nПродолжить чтение? (y/n): ")
        if choice.lower() != 'y':
            break

browser.quit()

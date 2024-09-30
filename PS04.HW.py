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

def print_paragraphs(browser):
    # Листаем параграфы
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    #Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
    #for i, para in enumerate(paragraphs, 1):
    #     print(f"\nПараграф {i}:")
    #     print(para.text.strip())
    #     #if i % 2 == 0:  # Показываем по 2 параграфа за раз
    #     choice = input("\nПродолжить чтение? (y/n): ")
    #     if choice.lower() != 'y':
    #         break

def show_links(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    print(hatnotes)
    hatnote = random.choice(hatnotes)

    # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    # results = page.links.keys()
    # Показываем связанные страницы

def find_wiki(browser):
    #функция для поиска в википедии
    query = input("Введите запрос для поиска на Википедии: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)  # вводим запрос
    search_box.send_keys(Keys.ENTER)  # нажимаем Enter


def main():
    #главная функция программы
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    find_wiki(browser) #ищем в википедии
    #предлагаем варианты выбора дальнейших действий
    while True:
        print("\nВыберите действие:")
        print("1. Читать параграфы статьи")
        print("2. Перейти на связанные страницы")
        print("3. Выйти из программы")
        choice = input("Ваш выбор: ")
        if choice == "1":
            print_paragraphs(browser)
        elif choice == "2":
            show_links(browser)
            print("1. Читать параграфы статьи")
            print("2. Перейти на связанные страницы")
            choice = input("Ваш выбор: ")
            if choice == "1":
                print_paragraphs(browser)
            elif choice == "2":
                show_links(browser)
        elif choice == "3":
            return

if __name__ == "__main__":
    main()

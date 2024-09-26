import wikipediaapi

# Инициализация API с настройкой на русский язык
wiki = wikipediaapi.Wikipedia("MyWikiBot/1.0","ru")

def print_paragraphs(page):
    """
    Функция для вывода параграфов статьи.
    """
    paragraphs = page.text.split("\n\n")
    for i, para in enumerate(paragraphs, 1):
        print(f"\nПараграф {i}:")
        print(para.strip())
        if i % 2 == 0:  # Показываем по 2 параграфа за раз
            choice = input("\nПродолжить чтение? (y/n): ")
            if choice.lower() != 'y':
                break

def show_links(page):
    """
    Функция для показа связанных страниц (ссылок).
    """
    links = list(page.links.keys())
    if not links:
        print("Нет связанных страниц.")
        return None

    for i, link in enumerate(links[:10], 1):  # Показываем только первые 10 ссылок
        print(f"{i}. {link}")

    try:
        choice = int(input("\nВыберите номер статьи для перехода или 0 для возврата: "))
        if choice == 0:
            return None
        elif 1 <= choice <= len(links[:10]):
            selected_link = links[choice - 1]
            new_page = wiki.page(selected_link)
            return new_page
        else:
            print("Неверный выбор.")
            return None
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        return None

def main():
    while True:
        query = input("\nВведите запрос для поиска на Википедии: ")
        page = wiki.page(query)

        if not page.exists():
            print(f"Статья '{query}' не найдена. Попробуйте другой запрос.")
            continue

        print(f"\nСтатья: {page.title}")
        while True:
            print("\nВыберите действие:")
            print("1. Читать параграфы статьи")
            print("2. Перейти на связанную страницу")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ")

            if choice == '1':
                print_paragraphs(page)

            elif choice == '2':
                new_page = show_links(page)
                if new_page:
                    page = new_page
                    print(f"\nНовая статья: {page.title}")
                else:
                    print("Возврат к текущей статье.")

            elif choice == '3':
                print("Выход из программы.")
                return

            else:
                print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()

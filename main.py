def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = list(dict.fromkeys(words))
    return ' '.join(unique_words)

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

def main():
    while True:
        print("Меню:")
        print("1. Записать предложение в файл")
        print("2. Прочитать предложение из файла и удалить повторяющиеся слова")
        print("3. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            sentence = input("Введите предложение: ")
            filename = input("Введите имя файла для записи: ")
            write_to_file(filename, sentence)
            print("Предложение записано в файл.")

        elif choice == "2":
            filename = input("Введите имя файла для чтения: ")
            content = read_from_file(filename)
            new_content = remove_duplicate_words(content)
            print("Повторяющиеся слова удалены:")
            print(new_content)

        elif choice == "3":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

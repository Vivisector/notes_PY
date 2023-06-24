from notes_manager import NotesManager

def main():
    manager = NotesManager()

    while True:
        print("\nДоступные команды:")
        print("1. Создать новую заметку")
        print("2. Просмотреть все заметки")
        print("3. Изменить существующую заметку")
        print("4. Удалить заметку")
        print("5. Выход из программы")

        command_number = input('\nВведите номер команды: ')

        if command_number == '1':
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            manager.add(title, body)
            print('Заметка успешно добавлена')
        elif command_number == '2':
            manager.show()
        elif command_number == '3':
            id = int(input('Введите номер заметки: '))
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            manager.edit(id, title, body)
            print('Заметка успешно изменена')
        elif command_number == '4':
            id = int(input('Введите id заметки: '))
            manager.delete(id)
            print('Заметка успешно удалена')
        elif command_number == '5':
            break
        else:
            print('Неверный номер команды')

if __name__ == '__main__':
    main()
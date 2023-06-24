# import readline  # Добавляем модуль readline
# import pyinputplus as pyip
from notes_manager import NotesManager

def main_menu(manager):
    print("\nДоступные команды:")
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Изменить существующую заметку")
    print("4. Удалить заметку")
    print("5. Выход из программы")


def main():
    manager = NotesManager()

    while True:
        main_menu(manager)

        command_number = input('\nВведите номер команды: ')

        if command_number == '1':
            # title = pyip.inputStr(prompt='Введите заголовок заметки (по умолчанию "Новая заметка"): ',
            #                       default='Новая заметка')
            # # title = input('Введите заголовок заметки: ')
            print('Введите заголовок заметки (оставьте пустым для значения "Новая заметка"):')
            title = input()
            if title.strip() == '':
               title = 'Новая заметка'
            body = input('Введите текст заметки: ')
            manager.add(title, body)
            print('Заметка успешно добавлена')
        elif command_number == '2':
            # Проверяем наличие заметок
            if manager.count == 0:
                print("Заметок не найдено")
                continue
            manager.show()
        elif command_number == '3':
            # Проверяем наличие заметок
            if manager.count == 0:
                print("Заметок не найдено")
                continue
            elif manager.count > 0:
                print("\nИмеющиеся заметки:")
                manager.showshort()
            id = int(input('Введите номер редактируемой заметки: '))
            if manager.get_note_by_id(id) is None:
                print('Такой заметки нет')
            else:                
                title = input('Введите новый заголовок заметки: ')
                body = input('Введите новый текст заметки: ')
                manager.edit(id, title, body)
                # print('Заметка успешно изменена')
                print(f'Заметка {id} успешно изменена')
        elif command_number == '4':
            # Проверяем наличие заметок
            if manager.count == 0:
                print("Заметок не найдено")
                continue
            elif manager.count > 0:
                print("\nИмеющиеся заметки:")
                manager.showshort()
            id = int(input('Введите номер удаляемой заметки: '))
            if manager.get_note_by_id(id) is None:
                print('Такой заметки нет')
            else:
                manager.delete(id)
                # print('Заметка успешно удалена')
                print(f'Заметка {id} успешно удалена')
        elif command_number == '5':
            break
        else:
            print('Неверный номер команды')

if __name__ == '__main__':
    main()

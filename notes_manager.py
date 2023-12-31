import json
from note import Note
import datetime

class NotesManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []
        self.count = 0
        self.load()
    
    def load(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
                self.notes = [Note(**note) for note in data['notes']]
                self.count = len(data['notes']) # Сохраняем количество заметок
                for note in self.notes:
                    if isinstance(note.timestamp, str):
                        note.timestamp = datetime.datetime.fromisoformat(note.timestamp)
        except (json.JSONDecodeError, FileNotFoundError):
            self.notes = []

    def save(self):
        with open(self.filename, 'w') as f:
            data = {'notes': [note.to_dict() for note in self.notes]}
            json.dump(data, f)

    def add(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)
        self.save()
        print(f'Заметка {id} успешно добавлена')
    
    def show(self):
        if not self.notes:
            print('Заметок не найдено')
            # continue
        else:
            for note in self.notes:
                print(f'{note.id}. {note.title}\n{note.body}\n{note.timestamp}\n')

    def showshort(self):
        if not self.notes:
            print('Заметок не найдено')
        else:
            for note in self.notes:
                print(f'{note.id}. {note.title}')
            print("\nДействия:")
            print("1. Прочитать заметку")
            print("2. Вернуться в главное меню")
        
            action = input("Выберите действие: ")
            if action == '1':
                note_id = int(input("Введите номер заметки: "))
                note = self.get_note_by_id(note_id)
    
                if note:
                    print(f'\nЗаметка {note.id}')
                    print(f'Заголовок: {note.title}')
                    print(f'Текст: {note.body}')
                    # print(f'Время создания: {note.timestamp}\n')
                    print(f'Время создания: {note.timestamp.strftime("%Y-%m-%d %H:%M")}\n')
                else:
                    print("Заметка с таким номером не найдена")

    def showshort_noDialog(self):
        if not self.notes:
            print('Заметок не найдено')
        else:
            for note in self.notes:
                print(f'{note.id}. {note.title}')

    def edit(self, id, title, body):
        note = self.get_note_by_id(id)
        if not self.notes:
            print('Заметок не найдено')
        else:
            note.edit(title, body)
            self.save()

    def delete(self, id):
        note = self.get_note_by_id(id)
        if not note:
            print('Заметок не найдено')
            # continue
        self.notes.remove(note)
        self.renumber_notes()  # перенумерация заметок
        self.save()
    
    def renumber_notes(self):
        for i, note in enumerate(self.notes, start=1):
            note.id = i

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

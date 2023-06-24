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
    
    def show(self):
        if not self.notes:
            print('Заметок не найдено')
            # continue
        else:
            for note in self.notes:
                print(f'{note.id}. {note.title}\n{note.body}\n{note.timestamp}\n')

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
        self.save()

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

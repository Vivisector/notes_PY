import json
from note import Note
import datetime

class NotesManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []
        self.load()
    
    def load(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
                self.notes = [Note(**note) for note in data['notes']]
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
        for note in self.notes:
            print(f'{note.id}. {note.title}\n{note.body}\n{note.timestamp}\n')

    def edit(self, id, title, body):
        note = self.get_note_by_id(id)
        if note:
            note.edit(title, body)
            self.save()
        else:
            print('Заметка не найдена')

    def delete(self, id):
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)
            self.save()
        else:
            print('Заметка не найдена')

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

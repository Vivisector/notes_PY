import datetime

class Note:
    def __init__(self, id, title, body, timestamp=None):
        self.id = id
        self.title = title
        self.body = body
        # self.timestamp = datetime.datetime.now()
        self.timestamp = timestamp if timestamp is not None else datetime.datetime.now()

    def edit(self, title, body):
        self.title = title
        self.body = body
        self.timestamp = datetime.datetime.now()

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'body': self.body,
    #         'timestamp': self.timestamp.isoformat()
    #     }
    
    def to_dict(self):
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.datetime.fromisoformat(self.timestamp)
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp.isoformat()
        }
from mongoengine import *
from datetime import *

class Users(Document):
    name = StringField()
    phone_number = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    modified_at = DateTimeField(default=datetime.utcnow)
    @classmethod
    def from_dict(cls, d):
        allowed = ('name', 'phone_number', 'created_at', 'modified_at' )
        df = {k : v for k, v in d.items() if k in allowed}
        return cls(**df)

from collections import UserDict

from .save_load import SaverLoader
from .user_intaraction import NotebookTable


class NoteBook(UserDict, SaverLoader, NotebookTable):
    
    def add_note(self, note):
        self.data[note.title] = note

    def delete_note(self, title):
        try:
            self.data.pop(title)
        except KeyError:
            return 'You have no notes with this title'
        
        return f'Note with the title {title} has been deleted'


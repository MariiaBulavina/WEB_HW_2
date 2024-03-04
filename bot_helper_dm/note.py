class Note:

    def __init__(self, title: str, text: str) -> None:

        self.title = title
        self.text = text
        self.tags = []

    def add_text(self, text):
        self.text += ' ' + text

    def add_tags(self, tags):
        tags = tags.split(' ')
        for tag in tags:
            self.tags.append(tag)

    def change_note(self, text):
        self.text = text
                
    def remove_tag(self, tag):
        self.tags.remove(tag)

    def __str__(self) -> str:
        return f'{self.title}: {self.text} tags: {"; ".join([str(tag) for tag in self.tags])}'
    
    def __repr__(self) -> str:
        return f'{self.title}: {self.text} tags: {"; ".join([str(tag) for tag in self.tags])}'
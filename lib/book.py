class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    
    def __eq__(self, value):
        self.__dict__ == value.__dict__

    
    def __repr__(self):
        return f"{self.id} - {self.title}, {self.author_name}"
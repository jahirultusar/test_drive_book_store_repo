from lib.book_repository import BookRepository
from lib.book import Book

"""
test book repo contstructs with connection
"""
def test_repository_contructs(db_connection):
    repository = BookRepository(db_connection)
    assert repository._connection == db_connection

"""
Test all() method
"""
def test_returns_list_of_books(db_connection):
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
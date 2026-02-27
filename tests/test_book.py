from lib.book import Book
"""
contruct a book class 
"""
def test_construct_a_book_class():
    book = Book(1, "test_title", "test_author")
    assert book.id == 1
    assert book.title == "test_title"
    assert book.author_name ==  "test_author"


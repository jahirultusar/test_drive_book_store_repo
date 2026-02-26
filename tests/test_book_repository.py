from lib.book_repository import BookRepository

"""
test book repo contstructs with connection
"""
def test_repository_contructs(db_connection):
    repository = BookRepository(db_connection)
    assert repository._connection == db_connection
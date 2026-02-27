from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# List them out
# for artist in artists:
#     print(artist)

# Retrieve all books
book_repository = BookRepository(connection)
books = book_repository.all()

# Lis all the books
for book in books:
    print(book)
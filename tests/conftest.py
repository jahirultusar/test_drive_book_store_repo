import pytest
from lib.database_connection import DatabaseConnection

# This is a Pytest fixture.
# A fixture is a reusable function that provides setup 
# logic for tests, supplying data or state before a test 
# runs and cleaning up afterward.
#
# In our project, it creates an object that we can use in our tests.
# We will use it to create a database connection.

@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed('seeds/book_store.sql')
    return conn

# Now, when a test includes a parameter named `db_connection`, Pytest automatically
# calls this fixture before the test runs and passes in its return value instead 
# of the function itself.
# We don’t need to call `db_connection()` or `db_connection.connect()` manually.

# For example:

# def test_something(db_connection):
#     # db_connection's return value is now available to us in this test.

# More information on Pytest fixtures: https://www.tutorialspoint.com/pytest/pytest_fixtures.htm

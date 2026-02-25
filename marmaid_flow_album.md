sequenceDiagram
    participant t as Terminal
    participant app as Main program <br/> (in app.py)
    participant ar as AlbumRepository class <br /> (in lib/album_repository.py)
    participant db_conn as DatabaseConnection class <br/> (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: USER/Jay Runs `python app.py`
    app->>db_conn: Opens connection to database by <br/>calling connect() method
    db_conn->>db_conn: Opens database connection using <br/>psycopg and stores the connection
    
    app->>ar: Calls all() method on AlbumRepository
    ar->>db_conn: Sends SQL query by calling <br/>execute() method on DatabaseConnection
    
    db_conn->>db: Sends query to database via <br/>the open database connection
    db-->>db_conn: Returns a list of dictionaries, <br/>one for each row of the albums table

    db_conn-->>ar: Returns a list of dictionaries, <br/>one for each row of the albums table
    
    loop For each dictionary in the list
        ar->>ar: Loops through rows and creates <br/>an Album object for every row
    end
    
    ar-->>app: Returns list of Album objects
    app-->>t: Prints list of Album objects <br/>(formatted by __repr__)

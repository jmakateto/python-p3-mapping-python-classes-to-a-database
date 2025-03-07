

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
@classmethod
def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
        )
    """
    CURSOR.execute(sql)
def save(self):
    sql = """
        INSERT INTO songs (name, album)
        VALUES (?, ?)
    """
    CURSOR.execute(sql, (self.name, self.album))
    CONN.commit()
    self.id = CURSOR.lastrowid


from song import Song
from database import CURSOR, CONN

# Create the table
Song.create_table()

# Create song instances and save them
hello = Song("Hello", "25")
despacito = Song("Despacito", "Vida")

hello.save()
despacito.save()

# Verify the records
CURSOR.execute("SELECT * FROM songs")
rows = CURSOR.fetchall()

for row in rows:
    print(f"Song ID: {row[0]}, Name: {row[1]}, Album: {row[2]}")

# Close the database connection
CONN.close()

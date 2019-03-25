import sqlite3
import json

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

with open('cocktails.json') as f:
    cocktails = json.load(f)

for index, cocktails in enumerate(cocktails, 1):
    c.execute("insert into cocktails_cocktail values (?, ?, ?, ?)", 
              [index, cocktails['title'], cocktails['pic'], cocktails['link']])
    conn.commit()

conn.close()


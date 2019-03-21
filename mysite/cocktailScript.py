import sqlite3
import json

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

with open('cocktails.json') as f:
    cocktails = json.load(f)

for i in range(len(cocktails)):
    c.execute("insert into cocktails_cocktail values (?, ?, ?, ?)", [i + 1, cocktails[i]['title'], cocktails[i]['pic'], cocktails[i]['link']])
    conn.commit()

conn.close()
import sqlite3

conn = sqlite3.connect('db.sqlite3')

with open('esquema_workbench.sql', 'w', encoding='utf-8') as f:
    for row in conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND sql IS NOT NULL"):
        f.write(row[0] + ';\n\n')

print('Archivo esquema_workbench.sql generado correctamente')
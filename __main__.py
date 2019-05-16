import sqlite3

if __name__ == '__main__':
    from entitites import create_tables

    db = sqlite3.connect("./exceptd.db")
    create_tables(db)

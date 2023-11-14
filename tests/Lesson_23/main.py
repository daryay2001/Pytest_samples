from constants import ROOT_PATH
from utilities.sqlite_cm import Sqlite

if __name__ == '__main__':
    with Sqlite(f"{ROOT_PATH}/db/test.db") as c:
        query_create = '''
        CREATE TABLE PHONES
(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MODEL TEXT NOT NULL,
        BRAND TEXT NOT NULL,
        PROCESSOR TEXT,
        YEAR INT DEFAULT 2020,
        PRICE REAL NOT NULL
);
        '''

        c.execute(query_create)
        query_insert = '''
        INSERT INTO PHONES (MODEL, BRAND, PROCESSOR, YEAR, PRICE)
        VALUES ('Iphone 15 Pro', 'Apple', 'Apple A17 Pro', 2023, 800.00)
        '''

        c.execute(query_insert)
        res = c.execute("SELECT * FROM PHONES")
        print(res.fetchall())

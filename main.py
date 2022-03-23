import sqlite3
import os

from prettytable import from_db_cursor
from prettytable import PrettyTable 
from kaffedb import test

test()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

connection = sqlite3.connect("kaffe.db")
cursor = connection.cursor()

with open("kaffedb.sql", encoding="utf-8") as file:
    script = file.read()
    cursor.executescript(script)
    connection.commit()


def main():
    clearConsole()

    print("Hi and welcome to Kaffe db enjoy")
    print("")
    print("===================")
    print("Type 'quit' to exit")
    print("===================")

    user_history = input("Choose a user history (1 - 5): ")

    def new_result():
        clearConsole()
        print("Result for User Story " + user_history)

    while user_history != "quit":
        # Case 1:
        if user_history == "1":
            new_result()

            cursor.execute("SELECT * FROM bruker")
            close_query()

        elif user_history == "2":
            new_result()

            cursor.execute("""
            SELECT b.fornavn, b.etternavn, COUNT(DISTINCT k.navn) as unike_kaffer
            FROM bruker as b
            INNER JOIN kaffesmaking as s on b.bruker_id = s.bruker_id
            INNER JOIN ferdigbrent_kaffe as k on s.ferdigbrent_kaffe_id = k.ferdigbrent_kaffe_id
            WHERE s.smaksdato > 2022-01-01
            GROUP BY b.fornavn, b.etternavn
            ORDER BY unike_kaffer DESC;
            """)
            close_query()

        elif user_history == "3":
            new_result()

            cursor.execute("""         
            SELECT br.navn as kaffebrenneri, f.navn as kaffe, f.kilopris_nok as pris, ROUND(AVG(s.poeng), 2) as gjennomsnitsscore
            FROM kaffesmaking as s
            INNER JOIN ferdigbrent_kaffe as f ON s.ferdigbrent_kaffe_id = f.ferdigbrent_kaffe_id
            INNER JOIN kaffebrenneri as br ON f.kaffebrenneri_id = br.kaffebrenneri_id
            GROUP BY f.navn
            ORDER BY (CAST(AVG(s.poeng) as DECIMAL) / f.kilopris_nok)*1000 DESC; 
            """)
            close_query()

        elif user_history == "4":
            new_result()

            cursor.execute("""
            SELECT  f.navn, s.smaksnotater, f.beskrivelse
            FROM kaffesmaking as s
            LEFT JOIN ferdigbrent_kaffe as f USING(ferdigbrent_kaffe_id)
            WHERE s.smaksnotater LIKE "%floral%"
            UNION ALL

            SELECT br.navn, f.navn,  f.beskrivelse
            FROM ferdigbrent_kaffe as f
            LEFT JOIN kaffebrenneri as br USING(kaffebrenneri_id)
            WHERE f.beskrivelse LIKE "%floral%";
            """)
            close_query()

        elif user_history == "5":
            new_result()
            
            cursor.execute("SELECT * FROM bruker")
            close_query()
        
        else: 
            print("Not a valid input")

        user_history = input("Choose a user history (1 - 5): ")
        print("Type 'quit' to exit")

    connection.commit()
    connection.close()
    clearConsole()

def close_query():
    rows = cursor.fetchall()
    mytable = from_db_cursor(cursor)
        
    for row in rows:
        mytable.add_row(list(row))
    
    print(mytable)

main()
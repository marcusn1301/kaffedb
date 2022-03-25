from rich import print
from rich.table import Table
from rich.console import Console

def usecase1(cursor, clear):
    
    # Skriver ut listen til bruker  
    def show_table():
        rows = cursor.fetchall()
        row_list = list(rows)
        for row in row_list:
            print(row)
        print("")

    # Skriver ut formatert data (rich)
    def make_table():
        rows = cursor.fetchall()
        
        # Henter ut atributtene til tabellen
        field_names = [i[0] for i in cursor.description]
        # Lager tabellen, justerer fargen på atributtene, og setter en overskrift
        table = Table(show_header=True, header_style="bold magenta", title = "Table for usecase 1")

        # Legger til alle kolonnene i tabellen
        for field in field_names:
            table.add_column(field)
        
        # For hver rad gjøres hvert element om til strings og legges til i en ny liste
        # Deretter blir de omgjort til tupler som legges til i den formaterte tabellen
        for row in rows:
            eachrow = row
            liste = []
            for e in eachrow:
                liste.append(str(e))
            table.add_row(*liste)
        
        # Printer den formaterte tabellen
        print(table)
        
    clear()
    brennerinavn = input("Velg et kaffebrenneri: ")
    
    # Runs a query that shows kaffebrenneri and kaffenavn based on user input
    cursor.execute(f"""
        SELECT f.ferdigbrent_kaffe_id as kaffe_id, f.navn as kaffenavn, br.navn as brennerinavn 
        FROM ferdigbrent_kaffe as f
        INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
        WHERE br.navn like "%{brennerinavn}%";
        """)

    print("[bold magenta]Liste over Kaffebrennerier[/bold magenta]")
    clear()
    print("")

    make_table()

    kaffeid = input("Skriv inn tilhørende kaffe-id: ")
    clear()

    cursor.execute(f"""
        SELECT f.ferdigbrent_kaffe_id as kaffe_id, f.navn as kaffe, br.navn as brenneri
        FROM ferdigbrent_kaffe as f
        INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
        WHERE br.navn like "%{brennerinavn}%" AND kaffe_id = {kaffeid};
        """)
    
    make_table()
    
    print("[bold magenta]Påtide å rate kaffen[/bold magenta]")
    
    # If the user types an invalid input, you try again
    while True:
        poeng = input("Hvor mange poeng vil du gi kaffen (1-10)?: ")
        if (int(poeng) < 10 and int(poeng) > 0): break
       
        clear()
        print("Poeng må må være et tall mellom 1 og 10! Prøv igjen!")

    clear()
    smaksnotat = input("Gi kaffen et smaksnotat: ")
    clear()

    cursor.execute(f"INSERT INTO kaffesmaking VALUES(100, '{smaksnotat}', '{poeng}', '2022-03-24 10:00:00', 1, {kaffeid});")
    
    print("[bold magenta]Her er din kaffesmaking: [/bold magenta]")
    print("")
    
    cursor.execute("""
    SELECT br.navn as brenneri, k.navn as kaffe, s.smaksnotater as smaksnotat, s.poeng
    FROM kaffesmaking as s
    INNER JOIN bruker as b USING(bruker_id)
    INNER JOIN ferdigbrent_kaffe as k USING(ferdigbrent_kaffe_id)
    INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
    WHERE s.kaffesmaking_id = 100;
    """)

    make_table()
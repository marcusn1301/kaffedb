from rich import print
from rich.table import Table
from rich.console import Console

def usecase1(cursor, clear):
    
    def quit():
        print("Type 'quit' or 'q' to exit")
        print("")
    
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
        def color(e, i, liste):
            if i % 2 == 0:
                liste.append((str(f"[bold magenta]{e}[/bold magenta]")))
            else:
                liste.append((str(e)))
        i = 1
        for eachrow in rows:
            liste = []
            for e in eachrow:
                color(e, i, liste)
            i += 1 

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
        WHERE br.navn like "%{brennerinavn.lower()}%";
        """)

    print("[bold magenta]Liste over Kaffebrennerier[/bold magenta]")
    clear()

    make_table()

    kaffeid = input("Skriv inn tilhørende kaffe-id: ")
    clear()

    cursor.execute(f"""
        SELECT f.ferdigbrent_kaffe_id as kaffe_id, f.navn as kaffe, br.navn as brenneri
        FROM ferdigbrent_kaffe as f
        INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
        WHERE br.navn like "%{brennerinavn.lower()}%" AND kaffe_id = {kaffeid};
        """)
    
    make_table()
    print("")
    print("[bold magenta]Påtide å rate kaffen[/bold magenta]")
    
    # If the user types an invalid input, you try again
    while True:
        poeng = input("Hvor mange poeng vil du gi kaffen (1-10)?: ")
        if (poeng.isnumeric()) and (int(poeng) < 11 and int(poeng) > 0): break  
        
        clear()
        print("Poeng må må være et tall mellom 1 og 10! Prøv igjen!")

    clear()
    smaksnotat = input("Gi kaffen et smaksnotat: ")
    clear()

    cursor.execute(f"INSERT INTO kaffesmaking VALUES(100, '{smaksnotat.lower()}', '{poeng}', '2022-03-25 15:35:00', 1, {kaffeid});")    
    
    cursor.execute(f"""
    SELECT  f.navn, br.navn as brenneri, s.poeng, s.smaksnotater, f.beskrivelse, f.kilopris_nok, fm.navn as foredlingsmetode, f.brenningsgrad as brenningsgrad,
    kb.navn as bønne, kg.navn as kaffegård, r.moh, r.navn as region, l.navn as land
    FROM kaffesmaking as s
    INNER JOIN ferdigbrent_kaffe as f USING(ferdigbrent_kaffe_id)
    INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
    INNER JOIN kaffeparti as kp USING(parti_id)
    INNER JOIN foredlingsmetode as fm USING(foredlingsmetode_id)
    INNER JOIN består_av as ba USING(parti_id)
    INNER JOIN kaffebønner as kb USING(kaffebønne_id)
    INNER JOIN kaffegård as kg USING(kaffegård_id)
    INNER JOIN region as r USING(region_id)
    INNER JOIN land as l USING(land_id)
    WHERE s.kaffesmaking_id = 100
    """)

    print("[bold magenta]Her er din kaffesmaking: [/bold magenta]")
    print("")
    make_table()
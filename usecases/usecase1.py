from rich import print

def usecase1(cursor, clear):
    
    # Skriver ut listen til bruker  
    def show_table():
        rows = cursor.fetchall()
        row_list = list(rows)
        for row in row_list:
            print(row)
        print("")
        
    brennerinavn = input(print("[bold cyan]Velg et kaffebrenneri: [/bold cyan]"))
    clear()

    cursor.execute(f"""
        SELECT f.ferdigbrent_kaffe_id as kaffe_id, f.navn as kaffenavn, br.navn as brennerinavn 
        FROM ferdigbrent_kaffe as f
        INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
        WHERE br.navn like "%{brennerinavn}%";
        """)

    print("Liste over Kaffebrennerier")
    print("Velg en kaffe du ønsker å smake (velg en id fra listen): ")
    print("")

    show_table()

    kaffeid = input("Skriv inn tilhørende kaffe-id: ")
    clear()

    cursor.execute(f"""
        SELECT f.ferdigbrent_kaffe_id as kaffe_id, f.navn as kaffenavn, br.navn as brennerinavn 
        FROM ferdigbrent_kaffe as f
        INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
        WHERE br.navn like "%{brennerinavn}%" AND kaffe_id = {kaffeid};
        """)
    
    print("")
    print("Du valgte: ")
    show_table()
    
    print("Påtide å rate kaffen🤨😐😛🤤🤣")
    poeng = input("Hvor mange poeng vil du gi kaffen (1-10)?: ")
    smaksnotat = input("Gi kaffen et smaksnotat: ")

    cursor.execute(f"INSERT INTO kaffesmaking VALUES(100, '{smaksnotat}', {poeng}, 2022-03-24, 1, {kaffeid});")
    
    print("")
    print("Her er dine kaffesmakinger:")
    print("")
    
    cursor.execute("""
    SELECT * 
    FROM kaffesmaking as s
    INNER JOIN bruker as b USING(bruker_id)
    WHERE b.bruker_id = 1;
    """)

    show_table()

    # Sprørsmål:
    # Skal bruker smake på en eksisterende kaffe?
    # Fks. at vi lister opp alle alternativene til brukeren 

"""     cursor.execute("INSERT INTO bruker VALUES(100, 'bruker@gmail.com', 'brukerpassord' 'brukerfornavn', 'brukeretternavn');")
    cursor.execute(f"INSERT INTO kaffesmaking VALUES(100, '{smaksnotat}', {poeng}, 2022-03-24);")
    cursor.execute(f"INSERT INTO ferdigbrent_kaffe VALUES(100, '{kaffenavn}', '2022-01-20 10:00:00', 'middels brent', 'en velsmakende og kompleks kaffe for mørketiden');")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES(100, );")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();") """
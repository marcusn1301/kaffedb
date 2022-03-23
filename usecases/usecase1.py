def usecase1(cursor):
    kaffenavn = input("Hva er navnet på kaffen du har smakt? ")
    poeng = input("Hvor mange poeng vil du gi kaffen? ")
    smaksnotat = input("Gi kaffen et smaksnotat: ")
    brennerinavn = input("Velg et kaffebrenneri: ")

    cursor.execute("SELECT ferdigbrent_kaffe_id as kaffe_id, ferdigbrent_kaffe.navn as kaffenavn FROM ferdigbrent_kaffe")
    
    valgtBrenneri = input("Skriv inn tilhørende brenneri-id: ")
    
    # Sprørsmål:
    # Skal bruker smake på en eksisterende kaffe?
    # Fks. at vi lister opp alle alternativene til brukeren 

    """ cursor.execute("INSERT INTO bruker VALUES(100, 'bruker@gmail.com', 'brukerpassord' 'brukerfornavn', 'brukeretternavn');")
    cursor.execute(f"INSERT INTO kaffesmaking VALUES(100, '{smaksnotat}', {poeng}, 2022-03-24);")
    cursor.execute(f"INSERT INTO ferdigbrent_kaffe VALUES(100, '{kaffenavn}', '2022-01-20 10:00:00', 'middels brent', 'en velsmakende og kompleks kaffe for mørketiden');")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES(100, );")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();")
    cursor.execute("INSERT INTO ferdigbrent_kaffe VALUES();") """


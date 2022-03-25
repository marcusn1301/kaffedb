def usecase5(cursor, clear):
    land1 = input("Skriv inn et land du vil søke etter: ")
    land2 = input("Skriv inn et til land du vil søke etter: ")
    ikke_metode = input("Skriv inn en uønsket foredlingsmetode: ")
    clear()

    # Executes a query where the user is prompted to type two countries and an
    # unwanted processing method.
    cursor.execute(f"""
    SELECT br.navn as brennerinavn, k.navn as kaffenavn
    FROM ferdigbrent_kaffe as k

    INNER JOIN kaffebrenneri as br USING(kaffebrenneri_id)
    INNER JOIN kaffeparti as kp USING(parti_id)
    INNER JOIN foredlingsmetode as f USING(foredlingsmetode_id)
    INNER JOIN kaffegård as kg USING(kaffegård_id)
    INNER JOIN region as r USING(region_id)
    INNER JOIN land as l USING(land_id)
    WHERE f.foredlingsmetode_id NOT IN (SELECT foredlingsmetode_id 
    FROM foredlingsmetode WHERE foredlingsmetode.navn="{ikke_metode.lower()}") 
    AND (l.navn = "{land1.lower()}" OR l.navn = "{land2.lower()}"); 
    """)
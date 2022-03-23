def usecase4(cursor):
    x = input("Velg et ord du vil søke etter: ")

    cursor.execute(f"""
    SELECT  f.navn, s.smaksnotater, f.beskrivelse
    FROM kaffesmaking as s
    LEFT JOIN ferdigbrent_kaffe as f USING(ferdigbrent_kaffe_id)
    WHERE s.smaksnotater LIKE "%{x.lower()}%"
    UNION ALL

    SELECT br.navn, f.navn,  f.beskrivelse
    FROM ferdigbrent_kaffe as f
    LEFT JOIN kaffebrenneri as br USING(kaffebrenneri_id)
    WHERE f.beskrivelse LIKE "%{x.lower()}%";
    """)
def usecase4(cursor):
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
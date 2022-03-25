def usecase3(cursor, clear):
    cursor.execute("""         
    SELECT br.navn as kaffebrenneri, f.navn as kaffe, f.kilopris_nok as pris, ROUND(AVG(s.poeng), 2) as gjennomsnittsscore
    FROM kaffesmaking as s
    INNER JOIN ferdigbrent_kaffe as f ON s.ferdigbrent_kaffe_id = f.ferdigbrent_kaffe_id
    INNER JOIN kaffebrenneri as br ON f.kaffebrenneri_id = br.kaffebrenneri_id
    GROUP BY f.navn
    ORDER BY (CAST(AVG(s.poeng) as DECIMAL) / f.kilopris_nok) DESC; 
    """)
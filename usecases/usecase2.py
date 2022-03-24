def usecase2(cursor, clear):
    cursor.execute("""
    SELECT b.fornavn, b.etternavn, COUNT(DISTINCT k.navn) as unike_kaffer
    FROM bruker as b
    INNER JOIN kaffesmaking as s on b.bruker_id = s.bruker_id
    INNER JOIN ferdigbrent_kaffe as k on s.ferdigbrent_kaffe_id = k.ferdigbrent_kaffe_id
    WHERE s.smaksdato > 2022-01-01
    GROUP BY b.fornavn, b.etternavn
    ORDER BY unike_kaffer DESC;
    """)
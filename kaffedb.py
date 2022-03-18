import sqlite3
import os


path = os.getcwd()

con = sqlite3.connect(f'{path}/kaffe.db')
cur = con.cursor()

# Deletes tables which already exists in the database -
# when trying to create new ones

########**    重要的 -=====-Important message-====- 信息    **########
## The AUTOINCREMENT requires additional CPU, memory, disk space, ##
## and disk I/O overhead which is why we decided to remove it.    ##
########**                     =---*---=                  **########

cur.executescript('''DROP TABLE IF EXISTS bruker;
  DROP TABLE IF EXISTS ferdigbrent_kaffe;
  DROP TABLE IF EXISTS kaffesmaking;
  DROP TABLE IF EXISTS kaffebrenneri;
  DROP TABLE IF EXISTS foredlingsmetode;
  DROP TABLE IF EXISTS kaffeparti;
  DROP TABLE IF EXISTS består_av;
  DROP TABLE IF EXISTS kaffebønner;
  DROP TABLE IF EXISTS dyrket_av;
  DROP TABLE IF EXISTS kaffegård;
  DROP TABLE IF EXISTS region;
  DROP TABLE IF EXISTS land;'''
)

#-----------------------------------------------------
#              Table `KaffeDB`.`Bruker`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS bruker (
    bruker_id INT NOT NULL,
    epost varchar(50) NOT NULL,
    passord varchar(50) NOT NULL,
    fornavn varchar(30),
    etternavn varchar(30),
    CONSTRAINT bruker_pk PRIMARY KEY (bruker_id)
  );
''')
# Insert values
brukere = (
    (1, 'marius@gmail.com', "hemmeligpassord", "maius", "mariussen"),
    (2, 'hei@gmail.com', "secretpassord123", "fornavn", "norman"),
    (3, 'hu@stud.ntnu.no', "passord", ":D", "xD"),
    (4, 'test@gmail.com', "passord123", "Kim", "norman"),
    (5, 'bruker1@gmail.com', "secretkey123", "Apyr", "norman"),
    (6, 'annenbruker@hotmail.com', "bruker1sucks", "Ola", "norman"),
    (7, 'student@stud.ntnu.com', "12345678", "Ola2", "etternavn"),
)
# Insert into bruker
cur.executemany("INSERT INTO bruker VALUES(?, ?, ?, ?, ?)", brukere)


#-----------------------------------------------------
#        Table `KaffeDB`.`FerdigbrentKaffe`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS ferdigbrent_kaffe (
    ferdigbrent_kaffe_id INT NOT NULL,
    navn varchar(50) NOT NULL,
    dato DATE NOT NULL,
    brenningsgrad varchar(30),
    beskrivelse varchar(100),
    kilopris_nok float NOT NULL,
    parti_id int NOT NULL,
    kaffebrenneri_id int NOT NULL,
    CONSTRAINT ferdigbrent_kaffe_pk PRIMARY KEY (ferdigbrent_kaffe_id)
    CONSTRAINT ferdigbrent_kaffe_fk1 FOREIGN KEY (parti_id) REFERENCES kaffeparti(parti_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT ferdigbrentkaffe_fk2 FOREIGN KEY (kaffebrenneri_id) REFERENCES kaffebrenneri(kaffebrenneri_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')
# Insert values
ferdigbrent_kaffe = (
    (1, 'Vinterkaffe 2022', "20.01.2022", "lysbrent", "En velsmakende og kompleks kaffe for mørketiden", 600,00, 1, 1),
)
# Insert into into ferdigbrent_kaffe
cur.executemany("INSERT INTO ferdigbrent_kaffe VALUES(?, ?, ?, ?, ?, ?, ?, ?)", ferdigbrent_kaffe)

#-----------------------------------------------------
#           Table `KaffeDB`.`Kaffesmaking`
#-----------------------------------------------------

# UNSIGNED CONSTRAINT CHECK (poeng < 11) (var på poeng)

cur.execute('''
  CREATE TABLE IF NOT EXISTS kaffesmaking (
    kaffesmaking_id INT NOT NULL,
    smaksnotater VARCHAR(100),
    poeng INT NOT NULL,
    smaksdato DATE NOT NULL,
    bruker_id INT NOT NULL,
    ferdigbrent_kaffe_id INT NOT NULL,
    CONSTRAINT kaffesmaking_pk PRIMARY KEY (kaffesmaking_id),
    CONSTRAINT kaffesmaking_fk1 FOREIGN KEY (bruker_id) REFERENCES bruker(bruker_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT kaffesmaking_fk2 FOREIGN KEY (ferdigbrent_kaffe_id) REFERENCES ferdigbrent_kaffe(ferdigbrent_kaffe_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

#-----------------------------------------------------
#           Table `KaffeDB`.`Kaffebrenneri`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS kaffebrenneri (
    kaffebrenneri_id INT NOT NULL,
    navn VARCHAR(50) NOT NULL,
    CONSTRAINT kaffebrenneri_pk PRIMARY KEY (kaffebrenneri_id)
  );
''')

# Insert values
kaffebrenneri = (
    (1, 'Jacobsen & Svart'),
)
# Insert into kaffebrenneri
cur.executemany("INSERT INTO ferdigbrent_kaffe VALUES(?, ?)", kaffebrenneri)

#-----------------------------------------------------
#         Table `KaffeDB`.`Foredlingsmetode`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS foredlingsmetode (
    foredlingsmetode_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    beskrivelse VARCHAR(100),
    parti_id INT NOT NULL, 
    CONSTRAINT foredlingsmetode_pk PRIMARY KEY (foredlingsmetode_id),
    CONSTRAINT foredlingsmetode_fk FOREIGN KEY (parti_id) REFERENCES kaffeparti(parti_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

# Insert values
kaffebrenneri = (
    (1, 'Jacobsen & Svart'),
)
# Insert into kaffebrenneri
cur.executemany("INSERT INTO ferdigbrent_kaffe VALUES(?, ?)", kaffebrenneri)

#-----------------------------------------------------
#            Table `KaffeDB`.`Kaffeparti`
#-----------------------------------------------------
cur.execute('''
  CREATE TABLE IF NOT EXISTS kaffeparti (
    parti_id INT NOT NULL,
    innhøstingsår INT NOT NULL,
    kilopris_usd FLOAT NOT NULL,
    foredlingsmetode_id INT NOT NULL,
    kaffegård_id INT NOT NULL,
    CONSTRAINT kaffeparti_pk PRIMARY KEY (parti_id),
    CONSTRAINT kaffeparti_fk1 FOREIGN KEY (foredlingsmetode_id) REFERENCES foredlingsmetode(foredlingsmetode_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT kaffeparti_fk2 FOREIGN KEY (kaffegård_id) REFERENCES kaffegård(kaffegård_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`BestårAv`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS består_av (
    parti_id INT NOT NULL,
    kaffebønne_id INT NOT NULL,
    CONSTRAINT består_av_fk1 FOREIGN KEY (parti_id) REFERENCES kaffeparti(parti_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT består_av_fk2 FOREIGN KEY (kaffebønne_id) REFERENCES kaffebønner(kaffebønne_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`Kaffebønner`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS kaffebønner (
    kaffebønne_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    art VARCHAR(30) NOT NULL,
    CONSTRAINT kaffebønner_pk PRIMARY KEY (kaffebønne_id)
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`DyrketAv`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS dyrket_av (
    kaffebønne_id INT NOT NULL,
    kaffegård_id INT NOT NULL,
    CONSTRAINT dyrket_av_fk1 FOREIGN KEY (kaffebønne_id) REFERENCES kaffebønner(kaffebønne_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT dyrket_av_fk2 FOREIGN KEY (kaffegård_id) REFERENCES kaffegård(kaffegård_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`Kaffegård`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS kaffegård (
    kaffegård_id INT NOT NULL,
    navn VARCHAR(50) NOT NULL,
    region_id INT NOT NULL,  
    CONSTRAINT kaffegård_pk PRIMARY KEY (kaffegård_id),
    CONSTRAINT kaffegård_fk FOREIGN KEY (region_id) REFERENCES region(region_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE 
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`Region`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS region (
    region_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    moh FLOAT NOT NULL,
    land_id INT NOT NULL,
    CONSTRAINT region_pk PRIMARY KEY (region_id),
    CONSTRAINT region_fk FOREIGN KEY (land_id) REFERENCES land(land_id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
  );
''')

#-----------------------------------------------------
#         Table `KaffeDB`.`Land`
#-----------------------------------------------------

cur.execute('''
  CREATE TABLE IF NOT EXISTS land (
    land_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    CONSTRAINT land_pk PRIMARY KEY (land_id)
  );
''')



cur.execute("SELECT * FROM bruker")
cur.execute("SELECT * FROM ferdigbrent_kaffe")

#cur.execute("SELECT * FROM bruker WHERE fornavn = Petter", (fornavn))



rows = cur.fetchall()
print(rows)



# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

#cur = con.cursor()
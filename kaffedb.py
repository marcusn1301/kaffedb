import sqlite3
import os


def test():
  print("DEEZ")

path = os.getcwd()

con = sqlite3.connect(f'{path}/kaffe.db')
cur = con.cursor()

# Deletes tables which already exists in the database -
# when trying to create new ones

########**     重要的 -=====-Important message-====- 信息      **########
##                                                                    ##
##    The AUTOINCREMENT requires additional CPU, memory, disk space,  ##
##    and disk I/O overhead which is why we decided to remove it.     ## 
##                                                                    ##
########**                       =---*---=                    **########

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
    (1, 'marius@gmail.com', "hemmeligpassord", "Marius", "Mariussen"),
    (2, 'hei@gmail.com', "secretpassord123", "Ola", "Nordmann"),
    (3, 'hu@stud.ntnu.no', "passord", "Petter", "Pettersen"),
    (4, 'test@gmail.com', "passord123", "Tobias", "Gunnes"),
    (5, 'bruker1@gmail.com', "secretkey123", "Rick", "Astley"),
    (6, 'annenbruker@hotmail.com', "bruker1sucks", "Petter", "Stordalen"),
    (7, 'student@stud.ntnu.com', "12345678", "Peter", "Pan"),
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
    (1, 'Vinterkaffe 2022', "2022-01-20 10:00:00", "lysbrent", "En velsmakende og kompleks kaffe for mørketiden", 600.00, 5, 1),
    (2, 'Rusten kaffe', "2021-03-04 10:00:00", "middels brent", "En skikkelig god kaffe med smak av gammel spiker", 399.00, 4, 2),
    (3, 'Esporesso', "2021-02-09 10:00:00", "lysbrent", "Espresse, men med O", 499.00, 5, 1),
    (4, 'Caffè Americano', "2020-09-26 10:00:00", "mørkbrent", "En amerikansk kaffe, ekstra stor og billig", 200.00, 3, 4),
    (5, 'Sommerkaffe 2021', "2020-11-01 10:00:00", "mørkbrent", "It's koffe, but only drink floral during summer", 299.00, 4, 5),
    (6, 'Gangsterkaffe 420', "2022-05-21 10:00:00", "lysbrent", "Eyo ", 459.00, 6, 2),
    (7, 'Høstkaffe 2021', "2019-09-25 10:00:00", "middels brent", "Only drink høst", 420, 2, 2),
    (8, 'Vårkaffe 2023', "2022-03-09 10:00:00", "lysbrent", "Smaker godt på våren :)", 299.00, 5, 3),
    (9, 'Starbuck', "2015-02-16 10:00:00", "lysbrent", "Starbuck 200kr for en kaffe hva i søren", 321.00, 8, 4),
    (10, 'Mocha kaffe', "2020-07-12 10:00:00", "middels brent", "Grønn kaffe som er floral", 421.00, 4, 1),
    (11, 'Iskaffe', "2021-06-05 10:00:00", "lysbrent", "Yo, that's icecold, I even got the chills hypothermia😥💀", 68.00, 5, 5),
    (12, 'Halloween kaffe', "2022-04-09 10:00:00", "middles brent", "Spooky delicious!", 41.00, 5, 3),
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

# Insert values
kaffesmaking = (
    (1, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '2020-01-20 10:00:00', 1, 1),
    (2, 'Veldig dårlig smak', 1, "2020-12-30 10:00:00", 2, 1),
    (3, 'floral', 7, "2019-03-03 10:00:00", 3, 1),
    (4, 'Helt Ok', 1, "2022-08-13 10:00:00", 4, 1),
    (5, 'Decent, mamma lager bedre tbh (L + ratio) BOZO', 3, "2022-02-12 10:00:00", 1, 1),
    (6, 'Smaker sopp mmmh kantarell', 4, "2022-02-17 10:00:00", 1, 1),
    (7, 'Ikke god, ikke dårlig', 4, "2022-02-27 10:00:00", 2, 2),
    (8, 'Mening1', 4, "2022-03-02 10:00:00", 3, 3),
    (9, 'Mening2', 9, "2022-02-18 10:00:00", 4, 7),
    (10, 'Jeg har ikke noe mening (NPC)🥴😵🤖', 4, "2022-02-21 10:00:00", 5, 8),
    (11, 'Gi meg pengene tilbake vær så snill', 4, "2022-02-22 10:00:00", 5, 10),
    (12, 'Iphon 11', 4, "2022-02-08 10:00:00", 3, 6),
    (13, 'asdasdasd', 8, "2022-02-02 10:00:00", 3, 3),
    (14, 'meget floral', 4, "2022-02-01 10:00:00", 6, 7),
    (15, 'Scrumptious', 10, "2022-02-11 10:00:00", 7, 8),
    (16, 'Breedable and submissive', 3, "2022-02-28 10:00:00", 1, 9),
    (17, 'Emil (8) liker den fordi den er floral', 5, "2021-02-13 10:00:00", 1, 2),
    (18, 'Jeg liker denne kaffen den er god', 2, "2021-02-14 10:00:00", 3, 2),

    
)
# Insert into kaffesmaking
cur.executemany("INSERT INTO kaffesmaking VALUES(?, ?, ?, ?, ?, ?)", kaffesmaking)

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
    (2, "Best brenneri EUW"),
    (3, "Best brenneri NA"),
    (4, "Brenneri Antonsen"), 
    (5, "La Brenneria de Casa"), 
)
# Insert into kaffebrenneri
cur.executemany("INSERT INTO kaffebrenneri VALUES(?, ?)", kaffebrenneri)

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
foredlingsmetode = (
    (1, 'Bærtørket', 'Tørker bærene lol', 1),
)
# Insert into foredlingsmetode
cur.executemany("INSERT INTO foredlingsmetode VALUES(?, ?, ?, ?)", foredlingsmetode)

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

# Insert values
kaffeparti = (
    (1, '2017', 1.5, 1, 2),
    (2, '2018', 69.0, 1, 3),
    (3, '2019', 42.0, 1, 4),
    (4, '2020', 21.0, 1, 4),
    (5, '2021', 8.0, 1, 1),
    (6, '2022', 66.6, 1, 5),
    (7, '2016', 66.6, 1, 2),
    (8, '2015', 66.6, 1, 1),
    (9, '2014', 66.6, 1, 3),
)
# Insert into kaffeparti
cur.executemany("INSERT INTO kaffeparti VALUES(?, ?, ?, ?, ?)", kaffeparti)

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

# Insert values
består_av = (
    (5,1),
    (2,1),
    (3,2),
    (4,3),
    (1,2),
)
# Insert into består_av
cur.executemany("INSERT INTO består_av VALUES(?, ?)", består_av)

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

# Insert values
kaffebønner = (
    (1, 'c. Bourbon', 'c. arabica'),
    (2, 'Tanzania Peaberry Coffee', 'Den beste arten'),
    (3, 'Nicaraguan Coffee', 'jeg elsker kaffe'),
    (4, 'Ethiopian Harrar Coffee', 'c++'),
    (5, 'Mocha Java Coffee', 'Java'),
)
# Insert into kaffebønner
cur.executemany("INSERT INTO kaffebønner VALUES(?, ?, ?)", kaffebønner)

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

# Insert values
dyrket_av = (
    (1, 1),
    (1, 2),
)
# Insert into DyrketAv
cur.executemany("INSERT INTO dyrket_av VALUES(?, ?)", dyrket_av)

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

# Insert values
kaffegård = (
    (1, 'Nombre de Dios', 1),
    (2, 'Kaffegård finland perkele', 2),
    (3, 'Unklabrundur gård', 3),
    (4, 'Kaffegård', 4),
    (5, 'Kaffegård2', 5),
)
# Insert into kaffegård
cur.executemany("INSERT INTO kaffegård VALUES(?, ?, ?)", kaffegård)

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

# Insert values
region = (
    (1, "Santa Ana", 1500, 1),
    (2, "vest-Finland", 123, 2),
    (3, 'Øst-Vest', 99999, 3),
    (4, 'På andre siden', -1, 4),
    (5, 'Java', 69, 5),
)
# Insert into region
cur.executemany("INSERT INTO region VALUES(?, ?, ?, ?)", region)

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

# Insert values
land = (
    (1, "El Salvador"),
    (2, "Finland"),
    (3, 'Norge'),
    (4, 'Frankrike'),
    (5, 'Chinatown'),
)
# Insert into land
cur.executemany("INSERT INTO land VALUES(?, ?)", land)

# Spørring brukerhistorie 1:
""" cur.execute("SELECT * FROM bruker")
cur.execute("SELECT * FROM ferdigbrent_kaffe") """


# Spørring brukerhistorie 2
# Spørring brukerhistorie 3
# Spørring brukerhistorie 4
# Spørring brukerhistorie 5



rows = cur.fetchall()
print(rows)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
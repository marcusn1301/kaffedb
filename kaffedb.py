import sqlite3

con = sqlite3.connect("kaffedb.db")


cur = con.cursor()

# Bruker table
cur.execute('''
  CREATE TABLE bruker (
  brukerid INT NOT NULL,
  epost varchar NOT NULL,
  passord varchar NOT NULL,
  fornavn varchar,
  etternavn varchar,
  CONSTRAINT bruker_pk PRIMARY KEY (brukerid)
  );

  CREATE TABLE ferdigbrentkaffe (
  ferdigbrentkaffeid INT NOT NULL,
  navn text NOT NULL,
  dato text NOT NULL,
  brenningsgrad text,
  beskrivelse text,
  kiloprisnok text,
  partiid text,
  kaffebrenneriid text,
  CONSTRAINT ferdigbrentkaffe_pk PRIMARY KEY (ferdigbrentkaffeid)
  );

  CREATE TABLE kaffesmaking (

KaffesmakingID INT NOT NULL,
  Smaksnotater VARCHAR(100),
  Poeng INT UNSIGNED CONSTRAINT CHECK (Poeng < 11) NOT NULL,
  Smaksdato DATE NOT NULL,
  BrukerID INT NOT NULL,
  FerdigbrentKaffeID INT NOT NULL,
  CONSTRAINT Kaffesmaking_PK PRIMARY KEY (KaffesmakingID),
  CONSTRAINT Kaffesmaking_FK FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT Kaffesmaking_FK FOREIGN KEY (FerdigbrentKaffeID) REFERENCES FerdigbrentKaffe(FerdigbrentKaffeID)
    ON UPDATE CASCADE
    ON DELETE CASCADE

  );


  ''')

  # Insert a row of datasdfds
cur.execute("INSERT INTO Bruker VALUES ('test@email.no','passord123','Ola','Nordmann')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

cur = con.cursor()

# FerdigbrentKaffe
cur.execute('''CREATE TABLE ferdigbrentkaffe (
  ferdigbrentkaffeid INT NOT NULL,
  navn text NOT NULL,
  dato text NOT NULL,
  brenningsgrad text,
  beskrivelse text,
  kiloprisnok text,
  partiid text,
  kaffebrenneriid text,
  CONSTRAINT ferdigbrentkaffe_pk PRIMARY KEY ()''')

# Hello sindrou


                            
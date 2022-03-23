DROP TABLE IF EXISTS bruker;
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
DROP TABLE IF EXISTS land;

CREATE TABLE IF NOT EXISTS bruker (
    bruker_id INT NOT NULL,
    epost varchar(50) NOT NULL,
    passord varchar(50) NOT NULL,
    fornavn varchar(30),
    etternavn varchar(30),
    CONSTRAINT bruker_pk PRIMARY KEY (bruker_id)
);

INSERT INTO bruker VALUES(1, 'marius@gmail.com', "hemmeligpassord", "Marius", "Mariussen");
INSERT INTO bruker VALUES(2, 'hei@gmail.com', "secretpassord123", "Ola", "Nordmann");
INSERT INTO bruker VALUES(3, 'hu@stud.ntnu.no', "passord", "Petter", "Pettersen");
INSERT INTO bruker VALUES(4, 'test@gmail.com', "passord123", "Tobias", "Gunnes");
INSERT INTO bruker VALUES(5, 'bruker1@gmail.com', "secretkey123", "Rick", "Astley");
INSERT INTO bruker VALUES(6, 'annenbruker@hotmail.com', "bruker1sucks", "Petter", "Stordalen");
INSERT INTO bruker VALUES(7, 'student@stud.ntnu.com', "12345678", "Peter", "Pan");

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


INSERT INTO ferdigbrent_kaffe VALUES(1, 'Vinterkaffe 2022', "2022-01-20 10:00:00", "lysbrent", "En velsmakende og kompleks kaffe for mørketiden", 600.00, 5, 1);
INSERT INTO ferdigbrent_kaffe VALUES(2, 'Rusten kaffe', "2021-03-04 10:00:00", "middels brent", "En skikkelig god kaffe med smak av gammel spiker", 399.00, 4, 2);
INSERT INTO ferdigbrent_kaffe VALUES(3, 'Esporesso', "2021-02-09 10:00:00", "lysbrent", "Espresse, men med O", 499.00, 5, 1);
INSERT INTO ferdigbrent_kaffe VALUES(4, 'Caffè Americano', "2020-09-26 10:00:00", "mørkbrent", "En amerikansk kaffe, ekstra stor og billig", 200.00, 3, 4);
INSERT INTO ferdigbrent_kaffe VALUES(5, 'Sommerkaffe 2021', "2020-11-01 10:00:00", "mørkbrent", "It's koffe, but only drink floral during summer", 299.00, 4, 5);
INSERT INTO ferdigbrent_kaffe VALUES(6, 'Gangsterkaffe 420', "2022-05-21 10:00:00", "lysbrent", "Eyo ", 459.00, 6, 2);
INSERT INTO ferdigbrent_kaffe VALUES(7, 'Høstkaffe 2021', "2019-09-25 10:00:00", "middels brent", "Only drink høst", 420, 2, 2);
INSERT INTO ferdigbrent_kaffe VALUES(8, 'Vårkaffe 2023', "2022-03-09 10:00:00", "lysbrent", "Smaker godt på våren :)", 299.00, 5, 3);
INSERT INTO ferdigbrent_kaffe VALUES(9, 'Starbuck', "2015-02-16 10:00:00", "lysbrent", "Starbuck 200kr for en kaffe hva i søren", 321.00, 8, 4);
INSERT INTO ferdigbrent_kaffe VALUES(10, 'Mocha kaffe', "2020-07-12 10:00:00", "middels brent", "Grønn kaffe som er floral", 421.00, 4, 1);
INSERT INTO ferdigbrent_kaffe VALUES(11, 'Iskaffe', "2021-06-05 10:00:00", "lysbrent", "Yo, that's icecold, I even got the chills hypothermia😥💀", 68.00, 5, 5);
INSERT INTO ferdigbrent_kaffe VALUES(12, 'Halloween kaffe', "2022-04-09 10:00:00", "middles brent", "Spooky delicious!", 41.00, 5, 3);

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

INSERT INTO kaffesmaking VALUES(1, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '2020-01-20 10:00:00', 1, 1);
INSERT INTO kaffesmaking VALUES(2, 'Veldig dårlig smak', 1, "2020-12-30 10:00:00", 2, 1);
INSERT INTO kaffesmaking VALUES(3, 'floral', 7, "2019-03-03 10:00:00", 3, 1);
INSERT INTO kaffesmaking VALUES(4, 'Helt Ok', 1, "2022-08-13 10:00:00", 4, 1);
INSERT INTO kaffesmaking VALUES(5, 'Decent, mamma lager bedre tbh (L + ratio) BOZO', 3, "2022-02-12 10:00:00", 1, 1);
INSERT INTO kaffesmaking VALUES(6, 'Smaker sopp mmmh kantarell', 4, "2022-02-17 10:00:00", 1, 1);
INSERT INTO kaffesmaking VALUES(7, 'Ikke god, ikke dårlig', 4, "2022-02-27 10:00:00", 2, 2);
INSERT INTO kaffesmaking VALUES(8, 'Mening1', 4, "2022-03-02 10:00:00", 3, 3);
INSERT INTO kaffesmaking VALUES(9, 'Mening2', 9, "2022-02-18 10:00:00", 4, 7);
INSERT INTO kaffesmaking VALUES(10, 'Jeg har ikke en mening (NPC)🥴😵🤖', 4, "2022-02-21 10:00:00", 5, 8);
INSERT INTO kaffesmaking VALUES(11, 'Gi meg pengene tilbake vær så snill', 4, "2022-02-22 10:00:00", 5, 10);
INSERT INTO kaffesmaking VALUES(12, 'Iphon 11', 4, "2022-02-08 10:00:00", 3, 6);
INSERT INTO kaffesmaking VALUES(13, 'asdasdasd', 8, "2022-02-02 10:00:00", 3, 3);
INSERT INTO kaffesmaking VALUES(14, 'meget floral', 4, "2022-02-01 10:00:00", 6, 7);
INSERT INTO kaffesmaking VALUES(15, 'Scrumptious', 10, "2022-02-11 10:00:00", 7, 8);
INSERT INTO kaffesmaking VALUES(16, 'Breedable and submissive', 3, "2022-02-28 10:00:00", 1, 9);
INSERT INTO kaffesmaking VALUES(17, 'Emil (8) liker den fordi den er floral', 5, "2021-02-13 10:00:00", 1, 2);
INSERT INTO kaffesmaking VALUES(18, 'Jeg liker denne kaffen den er god', 2, "2021-02-14 10:00:00", 3, 2);

CREATE TABLE IF NOT EXISTS kaffebrenneri (
    kaffebrenneri_id INT NOT NULL,
    navn VARCHAR(50) NOT NULL,
    CONSTRAINT kaffebrenneri_pk PRIMARY KEY (kaffebrenneri_id)
);

INSERT INTO kaffebrenneri VALUES(1, 'Jacobsen & Svart');
INSERT INTO kaffebrenneri VALUES(2, "Best brenneri EUW");
INSERT INTO kaffebrenneri VALUES(3, "Best brenneri NA");
INSERT INTO kaffebrenneri VALUES(4, "Brenneri Antonsen"); 
INSERT INTO kaffebrenneri VALUES(5, "La Brenneria de Casa"); 

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

INSERT INTO foredlingsmetode VALUES(1, 'Bærtørket', 'Tørker bærene lol😁😁😁😁🍒🍓', 1);
INSERT INTO foredlingsmetode VALUES(2, 'Vaskebjørn', 'Washy washy🦝🦝', 1);

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


INSERT INTO kaffeparti VALUES(1, '2017', 1.5, 1, 2);
INSERT INTO kaffeparti VALUES(2, '2018', 69.0, 1, 3);
INSERT INTO kaffeparti VALUES(3, '2019', 42.0, 1, 4);
INSERT INTO kaffeparti VALUES(4, '2020', 21.0, 1, 4);
INSERT INTO kaffeparti VALUES(5, '2021', 8.0, 1, 1);
INSERT INTO kaffeparti VALUES(6, '2022', 66.6, 1, 5);
INSERT INTO kaffeparti VALUES(7, '2016', 66.6, 1, 2);
INSERT INTO kaffeparti VALUES(8, '2015', 66.6, 1, 1);
INSERT INTO kaffeparti VALUES(9, '2014', 66.6, 1, 3);



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

INSERT INTO består_av VALUES(5,1);
INSERT INTO består_av VALUES(2,1);
INSERT INTO består_av VALUES(3,2);
INSERT INTO består_av VALUES(4,3);
INSERT INTO består_av VALUES(1,2);


CREATE TABLE IF NOT EXISTS kaffebønner (
    kaffebønne_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    art VARCHAR(30) NOT NULL,
    CONSTRAINT kaffebønner_pk PRIMARY KEY (kaffebønne_id)
);


INSERT INTO kaffebønner VALUES(1, 'c. Bourbon', 'c. arabica');
INSERT INTO kaffebønner VALUES(2, 'Tanzania Peaberry Coffee', 'Den beste arten');
INSERT INTO kaffebønner VALUES(3, 'Nicaraguan Coffee', 'jeg elsker kaffe');
INSERT INTO kaffebønner VALUES(4, 'Ethiopian Harrar Coffee', 'c++');
INSERT INTO kaffebønner VALUES(5, 'Mocha Java Coffee', 'Java');


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

INSERT INTO dyrket_av VALUES(1, 1);
INSERT INTO dyrket_av VALUES(1, 2);

CREATE TABLE IF NOT EXISTS kaffegård (
    kaffegård_id INT NOT NULL,
    navn VARCHAR(50) NOT NULL,
    region_id INT NOT NULL,  
    CONSTRAINT kaffegård_pk PRIMARY KEY (kaffegård_id),
    CONSTRAINT kaffegård_fk FOREIGN KEY (region_id) REFERENCES region(region_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE 
);

INSERT INTO kaffegård VALUES(1, 'Nombre de Dios', 1);
INSERT INTO kaffegård VALUES(2, 'Kaffegård finland perkele', 2);
INSERT INTO kaffegård VALUES(3, 'Unklabrundur gård', 3);
INSERT INTO kaffegård VALUES(4, 'Kaffegård', 4);
INSERT INTO kaffegård VALUES(5, 'Kaffegård2', 5);


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

INSERT INTO region VALUES(1, "Santa Ana", 1500, 1);
INSERT INTO region VALUES(2, "vest-Finland", 123, 2);
INSERT INTO region VALUES(3, 'Øst-Vest', 99999, 3);
INSERT INTO region VALUES(4, 'På andre siden', -1, 4);
INSERT INTO region VALUES(5, 'Java', 69, 5);


CREATE TABLE IF NOT EXISTS land (
    land_id INT NOT NULL,
    navn VARCHAR(30) NOT NULL,
    CONSTRAINT land_pk PRIMARY KEY (land_id)
);


INSERT INTO land VALUES(1, "El Salvador");
INSERT INTO land VALUES(2, "Finland");
INSERT INTO land VALUES(3, 'Norge');
INSERT INTO land VALUES(4, 'Frankrike');
INSERT INTO land VALUES(5, 'Chinatown');
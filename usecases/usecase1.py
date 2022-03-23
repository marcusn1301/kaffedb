def usecase1(cursor):
    print("Usecase 1")
    """ sql = "INSERT INTO bruker VALUES (?, ?, ?, ?, ?)"
    
    val = [
        (1, 'marius@gmail.com', "hemmeligpassord", "Marius", "Mariussen"),
        (2, 'hei@gmail.com', "secretpassord123", "Ola", "Nordmann"),
        (3, 'hu@stud.ntnu.no', "passord", "Petter", "Pettersen"),
        (4, 'test@gmail.com', "passord123", "Tobias", "Gunnes"),
        (5, 'bruker1@gmail.com', "secretkey123", "Rick", "Astley"),
        (6, 'annenbruker@hotmail.com', "bruker1sucks", "Petter", "Stordalen"),
        (7, 'student@stud.ntnu.com', "12345678", "Peter", "Pan"),
    ]

    cursor.executemany(sql, val)
    cursor.execute("SELECT * FROM bruker") """


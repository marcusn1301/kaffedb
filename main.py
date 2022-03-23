import sqlite3
import os

from prettytable import from_db_cursor
from prettytable import PrettyTable 

from usecases.usecase1 import usecase1
from usecases.usecase2 import usecase2
from usecases.usecase3 import usecase3
from usecases.usecase4 import usecase4
from usecases.usecase5 import usecase5

# Clears the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

# Creates a connection to the kaffe.db database
# If the file does not exists, it creates a new one
connection = sqlite3.connect("database/kaffe.db")
cursor = connection.cursor()

# Opens the kaffe.db database and executes the sql script
with open("database/kaffedb.sql", encoding="utf-8") as file:
    script = file.read()
    cursor.executescript(script)
    connection.commit()

def main():
    # Greets the user with an introduction
    clearConsole()

    print("Hi and welcome to KaffeDB! Enjoy!")
    print("")
    print("===================")
    print("Type 'quit' to exit")
    print("===================")

    user_history = input("Choose a user history (1 - 5): ")

    # Clears the console and displays the current usecase
    def new_result():
        clearConsole()
        print("Result for User Story " + user_history)

    # Keeps asking the user to input a usecase
    # If the input is not quit, it keeps asking
    while user_history != "quit":

        # Checks each case from the user input
        if user_history == "1":   run_usecase(usecase1, cursor, new_result)
        elif user_history == "2": run_usecase(usecase2, cursor, new_result)
        elif user_history == "3": run_usecase(usecase3, cursor, new_result)
        elif user_history == "4": run_usecase(usecase4, cursor, new_result)
        elif user_history == "5": run_usecase(usecase5, cursor, new_result)
        
        # If the input is not a valid input
        else: 
            print("Not a valid input")

        user_history = input("Choose a user history (1 - 5): ")
        print("Type 'quit' to exit")

    # Commits the result and closes the prompt
    connection.commit()
    connection.close()
    clearConsole()

# Runs a usecase
# Takes in the casenumber, cursor and the new_result function
def run_usecase(case, cursor, newresult):
    newresult()  
    case(cursor)
    rows = cursor.fetchall()

    # Creates columns from the sqlite3 query
    mytable = from_db_cursor(cursor)
        
    # For each row in the query result:
    # adds a row to the formatted table
    for row in rows:
        mytable.add_row(list(row))
    
    print(mytable)

main()
import sqlite3
import os

from rich import print
from rich.table import Table
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

    print("Hi and welcome to [bold magenta]KaffeDB[/bold magenta]! Enjoy!")
    print("")
    print("[bold green]==============================[/bold green]")
    print(" Type 'quit' or 'q' to exit ")
    print("[bold green]==============================[/bold green]")

    user_history = input("Choose a user history (1 - 5): ")
    clearConsole()

    # Clears the console and displays the current usecase
    def new_result():
        clearConsole()
        print("Result for User Story " + user_history)

    # Keeps asking the user to input a usecase
    # If the input is not quit, it keeps asking
    while True:
        # If user input is "quit" or "q" the loop stops
        if (user_history == "quit" or user_history == "q"): return

        # Checks each case from the user input
        if user_history == "1": usecase1(cursor, clearConsole)
        elif user_history == "2": run_usecase(usecase2, cursor, new_result)
        elif user_history == "3": run_usecase(usecase3, cursor, new_result)
        elif user_history == "4": run_usecase(usecase4, cursor, new_result)
        elif user_history == "5": run_usecase(usecase5, cursor, new_result)
        
        # If the input is not a valid input
        else: 
            print("Not a valid input")

        user_history = input("Choose a user history (1 - 5): ")
        print("Type 'quit' or 'q' to exit")

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
    
    field_names = [i[0] for i in cursor.description]
    print(field_names)
    table = Table(show_header=True, header_style="bold magenta")

    for field in field_names:
        table.add_column(field)

    print("ROWS=================")
    
    instances = []
 
    
    for row in rows:
        eachrow = row
        liste = []
        for e in eachrow:
            liste.append(str(e))
        #print(tuple(liste))
        table.add_row(*liste)

        #allRows = ','.join(list([str(i) for i in row]))
        #print(allRows)
       # print(mystr)
        #mystr = ""
       # instance = (([str(i) for i in row]))
        #instance_removed = (str(instance).replace("[", "").replace("]", ""))
       # instances.append(instance_removed).
    #print(instances)
        
        #print(str(instance)[1:-1])
        #print("")
        #table.add_row(*(str(instance)[1:-1]))
        #"""  print(instances)
        #for instance in instances:
        #table.add_row(*(instance)) """
        
        
        
        
    """ for i in range(len(instances)):
            table.add_row(instances[i].join) """
            #table.add_row(instances[_])
        #table.add_row(*(mystr))
        #mystr = ""
        #print(",".join(instances))
        
        
        
    
    """ mytable = from_db_cursor(cursor)

    for row in rows:
        mytable.add_row(list(row)) """

    print(table)

    
    # For each row in the query result:
    # adds a row to the formatted table
    

main()
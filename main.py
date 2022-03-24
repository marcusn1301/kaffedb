import sqlite3
import os

from rich import print
from rich.table import Table
from rich.console import Console

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
    print("[cyan]Use a large console for best experience[/cyan]")
    print("")
    print("[bold green]==============================[/bold green]")
    print(" Type 'quit' or 'q' to exit ")
    print("[bold green]==============================[/bold green]")

    user_history = input("Choose a user history (1 - 5): ")
    clearConsole()

    # Clears the console and displays the current usecase
    def new_result():
        clearConsole()
        print("Type 'quit' or 'q' to exit")
        print("")

    # Keeps asking the user to input a usecase
    # If the input is not quit, it keeps asking
    while True:
        # If user input is "quit" or "q" the loop stops
        if (user_history == "quit" or user_history == "q"): return

        # Checks each case from the user input
        if user_history == "1": usecase1(cursor, clearConsole)
        elif user_history == "2": run_usecase(usecase2, cursor, new_result, "usecase 2", clearConsole)
        elif user_history == "3": run_usecase(usecase3, cursor, new_result, "usecase 3", clearConsole)
        elif user_history == "4": run_usecase(usecase4, cursor, new_result, "usecase 4", clearConsole)
        elif user_history == "5": run_usecase(usecase5, cursor, new_result, "usecase 5", clearConsole)
        
        # If the input is not a valid input
        else: 
            print("Not a valid input")

        user_history = input("Choose a user history (1 - 5): ")
        

# Runs a usecase
# Takes in the casenumber, cursor and the new_result function
def run_usecase(case, cursor, newresult, table_name, clear):
    newresult()  
    case(cursor, clear)
    rows = cursor.fetchall()
    
    field_names = [i[0] for i in cursor.description]
    table = Table(show_header=True, header_style="bold magenta", title=f"Table for {table_name}")

    for field in field_names:
        table.add_column(field)
        
    for eachrow in rows:
        liste = []
        for e in eachrow:
            liste.append(str(e))
        table.add_row(*liste)
    
    console = Console()
    console.print(table)

main()
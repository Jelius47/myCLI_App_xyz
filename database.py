import sqlite3
import datetime

from typing import List
from model import Todo

conn  =  sqlite3.connect("todos.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos (
              task text,
              cartegory text,
              date_added text,
              date_completed text,
              status text,
              position interger   )""")
    
create_table()

def insert_todo(todo : Todo):
    c.execute('select count(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0

    with conn:
        c.execute("INSERT INTO todos VALUES(:task, :cartegory,:date_added,:date_completed,:status,:position)",
                  {"task":todo.task,"cartegory":todo.cartegory,"date_added":todo.date_added,"date_completed":todo.date_completed,
                   "status":todo.status,"position":todo.position}) # The method is called parameter substitution to prevent SQL injection


def get_all_todos()->List[Todo]:
    c.execute("SELECT * FROM todos")
    results = c.fetchall()

    todos = []
    for result in results:
        todos.append(Todo(*result))

    return todos

def delete_todos(position):
    c.execute("SELECT COUNT(*) FROM todos")
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE FROM todos WHERE position = :position",{"position":position})
        for pos in range(position+1,count):
            change_position(pos,pos-1,False)


def change_position(old_position:int,new_position:int,commit=True):
    c.execute("UPDATE todos SET position = :position_new WHERE position = :position_old",
              {"position_new":new_position,"position_old":old_position})
    if commit:
        conn.commit()


def update_todo(position: int,task: str, cartegory:str):
    with conn:
        if task is not None and cartegory is not None:
            c.execute("UPDATE todos SET task = :task ,cartegory =:cartegory WHERE position =:position",
                      {"position":position,"task":task,"cartegory":cartegory})
            
        elif task is not None:
            c.execute("UPDATE todos SET task = :task WHERE position = :position",
                      {'position':position,'task':task})
        
        elif cartegory is not None:
            c.execute("UPDATE todos SET cartegory =:cartegory WHERE position =:position",
                      {"position":position,"cartegory":cartegory})


def complete_todo(position: int):
    with conn:
        c.execute(
            "UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position",
            {"date_completed": datetime.datetime.now().isoformat(), "position": str(position)},
        )
        conn.commit()  # Explicitly commit the changes

import typer
from rich.console import Console # rich is for the styling of our CLI
from rich.table import Table
from model import Todo
from database import *

console = Console()
app = typer.Typer()

@app.command(short_help='adds an item')
def add(task :str,cartegory:str):
    typer.echo(f"Adding {task},{cartegory}")

    todo = Todo(task=task,cartegory=cartegory)
    insert_todo(todo=todo)
    show()

@app.command()
def delete(position:int):
    typer.echo(f"Deleting {position}")
    # Indices in UI begins with 1 but in database with 0
    delete_todos(position=position-1)
    show()
    


@app.command()
def update(position:int,task:str = None,cartegory:str=None):
    typer.echo(f"Updating{position}")
    update_todo(position=position-1,task=task,cartegory=cartegory)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"Marking todo {position} as completed")
    if position > 0:
        complete_todo(position=position - 1)  # Adjust if off-by-one
    else:
        typer.echo("Invalid position. Please provide a valid position.")
    show()
# @app.command()
# def complete(position:int):
#     typer.echo(f"Completed {position}")
#     complete_todo(position=position-1)
#     show()

@app.command()
def show():
    # tasks = [("Todo1","Study"),("Todo2","sports")] this was hard coded
    tasks = get_all_todos()
    console.print("[bold magenta]Jelius DAilY Todos[/bold magenta]!","📓")

    table  = Table(show_header=True,header_style="bold blue")
    table.add_column("#",style="dim",width=6)
    table.add_column("Todo",min_width=20)
    table.add_column("Cartegory",min_width=20,justify="right")
    table.add_column("Done",min_width=20,justify="right")
    
    def get_cartegory_color(cartegory):
        COLORS = {"Teach":"cyan","Youtube":"red","Guitar":"cyan","Sports":"yellow","Study":"green"}
        if cartegory in COLORS:
            return COLORS[cartegory]
        return "white"



    for idx,task in enumerate(tasks,start=1):
        c = get_cartegory_color(task.cartegory)
        is_done_str = "🔵✔️" if task.status==2 else "❌"
        table.add_row(str(idx), task.task,f"[{c}]{task.cartegory}[/{c}]",is_done_str)
    console.print(table)


if __name__ ==  "__main__":
    app()


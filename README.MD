# TodoCLI Application 📓

A command-line interface (CLI) application to manage your daily tasks. This project is built using Python and leverages the `Typer` library for creating user-friendly CLI commands, along with `Rich` for styled terminal outputs. It helps you organize tasks into categories, mark them as completed, and visualize your to-do list in an aesthetically pleasing way.

## Features ✨
- Add new tasks with categories.
- Display all tasks in a formatted table.
- Mark tasks as completed.
- Delete tasks by position.
- Keep track of task status and completion date.

## Prerequisites 📋
- **Python**: Version 3.8 or higher is required.
- **SQLite3**: For database management.

## Installation ⚙️

### Step 1: Clone the Repository
```bash
git clone https://github.com/Jelius47/myCLI_App_xyz.git
cd todocli-app
```
### Step 2: Set Up a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run the Application
```bash
python todocli.py --help
```
## Usage 🚀
-- Here are some examples of how to use the TodoCLI application:

#### Adding a Task
```bash
python todocli.py add "Task Name"  "CategoryName"
```
#### Viewing All Tasks
```bash
python todocli.py show
```
#### Marking a Task as Completed
```bash
python todocli.py complete <task_position>
```
#### Deleting a Task
```bash
python todocli.py delete <task_position>
```

### Project Structure 🗂️
```bash
.
├── todocli.py            # Entry point for the CLI application
├── database.py        # Contains database interaction logic
├── models.py          # Defines the Todo class and its properties
├── README.md          # Documentation for the project
└── requirements.txt   # List of Python dependencies
```
#### Example Output 📋
---When you display your tasks, you’ll see something like this:

```bash
Jelius DAILY Todos! 📓

┏━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ # ┃ Todo         ┃ Category   ┃ Done     ┃
┡━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 1 │ Study Python │ Study      │ ❌       │
└───┴─────────────┴────────────┴──────────┘
```
### Acknowledgements 🙏
This project is inspired by the YouTube tutorial by [Patrick Loeber](https://youtu.be/ynd67UwG_cI). A big thanks for the insightful walkthrough of building a CLI application with Typer and Rich!

### Contributing 🤝
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions for new features or improvements.
 You may also add a star fork or whatever :)

Happy coding! 🎉
Jelius H. 
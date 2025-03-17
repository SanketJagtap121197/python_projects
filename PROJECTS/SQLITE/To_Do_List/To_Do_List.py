
#                                              SQLite Python Connectivity

import sqlite3

connection = sqlite3.connect("to_do_list.db")

cursor = connection.cursor()

#                                                  SQLite querries

cursor.execute('''
 CREATE TABLE IF NOT EXISTS tasks
 (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   task TEXT NOT NULL,
   status TEXT NOT NULL CHECK(status IN ('pending', 'completed'))
 )''')
connection.commit()

#                                                 SQLite functions

def task_add(task) :
    """ insert a new task in database """
    cursor.execute("INSERT INTO tasks (task, status) VALUES (?, 'pending')", (task,))
    connection.commit()
    print("Task added successfully!")

def task_view() :
    """ Retrieves and displays all tasks from the database """
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if tasks :
        print("\n To do lists : ")
        for task in tasks :
            print(f' {task[0]} - {task[1]} - {task[2]} ')
    else :
        print("\n no tasks available")


def task_complete (task_id) :
    """
    mark a specified task as completed
    parameters
    task_id (int) : the id of the task to be marked as completed
    """
    cursor.execute("UPDATE tasks SET status ='completed' WHERE id = ?", (task_id,))
    connection.commit()
    print("task marked as completed")

def task_delete (task_id) :
    """
    delete a specified task from database
    parameters
    task_id (int) : the id of the task to be marked as deleted
    """
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    print("task deleted sucessfully")


#                                              Python functions

# menu driven interface
while True :
    print("\nto do list")
    print("1. add task")
    print("2. view task")
    print("3. mark task as completed")
    print("4. delete task")
    print("5. exit")

    choice = input("enter your choice : ")

    if choice == '1':
        task = input("Enter task: ").upper()
        if task:
            task_add(task)
        else:
            print("task cannot be empty")


    elif choice == '2':
        task_view()

    elif choice == '3' :
        task_id = input("enter task id to mark as completed : ")
        if task_id.isdigit():
            task_complete(int(task_id))
        else:
            print("invalid task, enter a number")

    elif choice == '4':
        
        task_id = input("Enter task ID to delete: ")
        if task_id.isdigit():
            task_delete(int(task_id))
        else:
            print("invalid task, enter a number")

    elif choice == '5' :
        print("exiting application")

        break
    else :
        print("invalid choice")


connection.close()


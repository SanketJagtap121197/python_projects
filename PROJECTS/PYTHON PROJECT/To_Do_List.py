
tasks = []  # List to store tasks

while True:
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")  # user choices

    if choice == "1":
        task = input("Enter a task you want to do: ")
        tasks.append(task)  # Add task to the list
        print(f"Task '{task}' added!")

    elif choice == "2":
        if not tasks:  # Check if list is empty
            print("\nYour task list is empty!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")  # Display tasks # here . is given for readibility like 1. eat 2. run

    elif choice == "3":
        if not tasks:
            print("\nNo tasks to remove!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                remove_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= remove_index < len(tasks):  # Ensures the number is not negative and also ensures the number is within the task list range
                    removed_task = tasks.pop(remove_index)  # Remove task
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number! Please enter a valid number.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    elif choice == "4":
        print("Bye")
        break  # Exit the loop

    else:
        print("Invalid choice, please enter a number between 1-4.")

todos = []

def display_todos():
    print("\nYOUR TO-DO LIST:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}: {todo}")

def add_todo():
    input_str = input("Enter tasks to add in To-Do List (space-separated): ")
    input_list = input_str.split()
    for todo in input_list:
        if todo != "":
            todos.append(todo)
            added = True
    if added:
        print(f"Tasks added successfully.")
    else:
        print("No valid tasks provided. To-Do List remains unchanged.")

def delete_todo():
    display_todos()
    if not todos: #if todo list is empty
        print("No tasks to delete.")
        return

    index = int(input("Enter the task number to delete: "))
    
    if 1 <= index <= len(todos):
        deleted_todo = todos.pop(index - 1)
        print(f"Task '{deleted_todo}' deleted successfully.")
    else:
        print("Invalid task number.")

def mark_completed():
    display_todos()
    index = int(input("Enter the task number to mark as completed: "))
    
    if 1 <= index <= len(todos):
        todos[index - 1] = todos[index - 1] + " (completed)"
        print(f"Task '{todos[index - 1]}' marked as completed.")
    else:
        print("Invalid task number.")

# Load previously saved todos in the file.
try:
    with open("todos.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            todos.append(line.strip())
except FileNotFoundError:
    print("No existing to-do list found.\nStarting with an empty list.")


while True:
    print("\nTO-DO LIST MENU:")
    print("1. Display Todos")
    print("2. Add Todo")
    print("3. Delete Todo")
    print("4. Mark Todo as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_todos()
    elif choice == '2':
        add_todo()
    elif choice == '3':
        delete_todo()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Exited")
        with open("todos.txt", "a") as file:
            for todo in todos:
                file.write(todo + "\n")
        print("Your recent todos sucessfully saved.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

def display_menu():
    print("\nTo-Do List Menu")
    print("1. add a task")
    print("2. View all the tasks")
    print("3. remove completed or not interested task")
    print("4. Exit")

def add_task(todo_list):
    task = input("enter your demanded task: ")
    if task:
        todo_list.append(task)
        print("✔️")
    else:
        print("Task cannot be empty.")

def view_tasks(todo_list):
    if todo_list:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("❌ nothing left to do.")


def remove_task(todo_list):
    view_tasks(todo_list)
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()

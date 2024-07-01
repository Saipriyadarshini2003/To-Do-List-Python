# Define a class to represent a to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index. Please try again.")

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your to-do list is empty.")

# Function to display menu options
def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

# Main function to run the program
def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_index = int(input("Enter task index to remove: ")) - 1
                todo_list.remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

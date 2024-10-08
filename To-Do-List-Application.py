class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        except ValueError:
            print(f"Task '{task}' not found in the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task to add: ")
                self.add_task(task)
            elif choice == '2':
                task = input("Enter the task to remove: ")
                self.remove_task(task)
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()

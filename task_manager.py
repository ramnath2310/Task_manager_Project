import os
import json

# Dummy credentials for login
Dummy_Email= "test@mnk.com"
Dummy_Password = "password123"


# Login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == Dummy_Email and password == Dummy_Password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return login()

#Define task Structure
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "Task is completed" if self.completed else "Task is Not completed"
        return f"[{self.id}] {self.title} - {status}"

# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    # adding task
    def add_task(self, title):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")

    # view tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    # delete task with task_id
    def delete_task(self, task_id):
        task_to_delete = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"Task {task_id} deleted.")
        else:
            print(f"No task found with ID {task_id}.")

    # make task as completed to tasks performed by user
    def mark_task_as_complete(self, task_id):
        task_to_complete = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_complete:
            task_to_complete.completed = True
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"No task found with ID {task_id}.")
#File Handling
    # used to save task to tasks.json file
    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)
        print("Tasks saved to tasks.json.")

    # loads tasks from tasks.json file when the application starts
    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(task_id=task['id'], title=task['title'], completed=task['completed']) for task in tasks_data]
            print("Tasks loaded from tasks.json.")


# Main function for CLI
def main():
    if not login():
        return

    manager = TaskManager()

    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice to perform a task: ")

        if choice == '1':
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_task_as_complete(task_id)
        elif choice == '5':
            manager.save_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


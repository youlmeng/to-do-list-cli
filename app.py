import os

# 任务类
class Todo:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{self.task} [{status}]"

# ToDoList类
class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        new_todo = Todo(task)
        self.todos.append(new_todo)
        print(f"Added: {task}")

    def remove_task(self, task_id):
        try:
            task = self.todos.pop(task_id)
            print(f"Removed: {task.task}")
        except IndexError:
            print("Invalid task ID.")

    def list_tasks(self):
        if not self.todos:
            print("No tasks to show.")
            return
        for idx, todo in enumerate(self.todos):
            print(f"{idx}. {todo}")

    def mark_completed(self, task_id):
        try:
            self.todos[task_id].mark_as_completed()
            print(f"Task {task_id} marked as completed.")
        except IndexError:
            print("Invalid task ID.")

# 打印菜单
def print_menu():
    print("\nTodo List Menu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Exit")

# 主程序
def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            todo_list.list_tasks()
            try:
                task_id = int(input("Enter the task ID to remove: "))
                todo_list.remove_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.list_tasks()
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                todo_list.mark_completed(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

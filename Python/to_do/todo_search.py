def show_menu():
    """Prints the interaction menu options to the console."""
    print("\n---📝 My To Do List ---")
    print("1️⃣. Create 🦄")
    print("2️⃣. Delete 🗑️")
    print("3️⃣. Mark task DONE ✅")
    print("4️⃣. Mark task BLOCKED 💀")
    print("5️⃣. Increase priority ⬆️")
    print("6️⃣. Decrease priority ⬇️")
    print("7️⃣. Show my tasks 📋")
    print("8️⃣. Find task by ID 🔍")
    print("9️⃣. Exit 👋")

def generate_new_id_task(list_tasks: list) -> int:
    """Returns the maximum ID + 1. If list is empty, returns 0."""
    if not list_tasks:
        return 0
    return max(t['id'] for t in list_tasks) + 1

def find_task_by_id(task_list: list, task_id: int):
    """
    Searches for a task with id=task_id and returns all its data.
    
    Args:
        task_list (list): A list of dictionaries representing tasks.
        task_id (int): The unique identifier to search for.
    Returns:
        dict: If the task exists.
        None: If the task does NOT exist.
    """
    for t in task_list:
        if t.get("id") == task_id:
            return t
    return None

def modify_task_status(task_list: list, target_id: int, new_status: str) -> bool:
    """Updates the status field of a specific task."""
    task = find_task_by_id(task_list, target_id)
    if task:
        task['status'] = new_status
        return True
    return False

def modify_task_priority(task_list: list, target_id: int, new_priority: str) -> bool:
    """Updates the priority field of a specific task."""
    task = find_task_by_id(task_list, target_id)
    if task:
        task['priority'] = new_priority
        return True
    return False

def print_tasks(task_list: list):
    """Displays the task list formatted as a table."""
    if not task_list:
        print("\nYour list is empty. 🤷")
        return
    print(f"\n{'ID':<3} | {'Description':<40} | {'Priority':<8} | {'Status':<12} | {'Tag'}")
    print("-" * 75)
    for t in task_list:
        print(f"{t['id']:<3} | {t['description']:<40} | {t['priority']:<8} | {t['status']:<12} | {t['tag']}")

def run_todo_list():
    """Main flow control for the application."""
    tasks = []
    # Priority order: low -> medium -> high
    priorities = ["low", "medium", "high"]
    
    while True:
        show_menu()
        choice = input("\nChoose what do you want to do 🤔: ")

        if choice == "9": # Exit
            print("Good job today! Goodbye, see you soon! 💃🕺👋") 
            break

        elif choice == "1": # Create Task
            desc = input("Description: ")
            if not desc: 
                print("Error: Description cannot be empty. 🤷")
                continue
            prio = input("Priority (low/medium/high): ").lower()
            tag = input("Tag: ")
            new_id = generate_new_id_task(tasks)
            tasks.append({
                "id": new_id, 
                "description": desc, 
                "priority": prio if prio in priorities else "low", 
                "status": "pending 🚧", # Default status
                "tag": tag
            })
            print(f"✨Task {new_id} created.✨")

        elif choice == "2": # Delete Task
            try:
                target_id = int(input("Enter ID to delete: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    tasks.remove(task)
                    print("Task deleted successfully. 🗑️")
                else:
                    print("Task not found.🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "3": # Mark DONE
            try:
                target_id = int(input("Enter ID to mark DONE: "))
                if modify_task_status(tasks, target_id, "Done✅"):
                    print(f"Task {target_id} is now DONE ✅.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "4": # Mark BLOCKED
            try:
                target_id = int(input("Enter ID to mark BLOCKED: "))
                if modify_task_status(tasks, target_id, "Blocked💀"):
                    print(f"Task {target_id} is now BLOCKED 💀.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "5": # Increase priority
            try:
                target_id = int(input("Enter Task ID: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx < 2:
                        modify_task_priority(tasks, target_id, priorities[idx + 1])
                        print(f"Priority increased to {priorities[idx + 1]} ⬆️.")
                    else:
                        print("Priority is already at the maximum.🤯")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "6": # Decrease priority
            try:
                target_id = int(input("Enter Task ID: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx > 0:
                        modify_task_priority(tasks, target_id, priorities[idx - 1])
                        print(f"Priority decreased to {priorities[idx - 1]} ⬇️.")
                    else:
                        print("Priority is already at the minimum.🏖️🏝️")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "7": # Show all tasks
            print_tasks(tasks)

        elif choice == "8": # Find by ID
            try:
                target_id = int(input("Enter ID to find 🕵️: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    print("\n🔎 Task Found:")
                    print(f"Description: {task['description']}")
                    print(f"Priority:    {task['priority']}")
                    print(f"Status:      {task['status']}")
                    print(f"Tag:         {task['tag']}")
                else:
                    print("❌ Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        else:
            print("Oops! Wrong number. Choose from 1-9. 🤷")

if __name__ == "__main__":
    run_todo_list()
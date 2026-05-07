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
    print("8️⃣. Exit 👋")

def generate_new_id_task(list_tasks: list) -> int:
    """Returns the maximum ID + 1. If list is empty, returns 0."""
    if not list_tasks:
        return 0
    return max(t['id'] for t in list_tasks) + 1

def search_task_by_id(list_tasks: list, id_searched: int):
    """Returns the task dictionary or None if not found."""
    for task in list_tasks:
        if task['id'] == id_searched:
            return task
    return None

def modify_task_status(list_tasks: list, id_target: int, new_status: str) -> bool:
    """Updates the status field of a task."""
    task = search_task_by_id(list_tasks, id_target)
    if task:
        task['status'] = new_status
        return True
    return False

def modify_task_priority(list_tasks: list, id_target: int, new_priority: str) -> bool:
    """Updates the priority field of a task[cite: 1]."""
    task = search_task_by_id(list_tasks, id_target)
    if task:
        task['priority'] = new_priority
        return True
    return False

def print_tasks(list_tasks: list):
    """Displays tasks in a formatted table[cite: 1]."""
    if not list_tasks:
        print("\nYour list is empty. 🤷")
        return
    print(f"\n{'ID':<3} | {'Description':<50} | {'Priority':<8} | {'Status':<10} | {'Tag'}")
    print("-" * 85)
    for t in list_tasks:
        print(f"{t['id']:<3} | {t['description']:<50} | {t['priority']:<8} | {t['status']:<10} | {t['tag']}")

def run_todo_list():
    """Main flow control for the application[cite: 1]."""
    tasks = []
    priorities = ["low", "medium", "high"]
    
    while True:
        show_menu()
        choice = input("\nChoose what do you want to do 🤔: ")

        if choice == "8":
            print("Good job today! Goodbye, see you soon! 💃🕺👋") 
            break

        elif choice == "1": # Create
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
                "status": "🚧", 
                "tag": tag
            })
            print(f"Task {new_id} created.")

        elif choice == "2": # Delete
            try:
                target_id = int(input("Enter ID to delete: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    tasks.remove(task)
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "3": # Mark DONE (Using modify_task_status)[cite: 1]
            try:
                target_id = int(input("Enter ID to mark DONE: "))
                if modify_task_status(tasks, target_id, "✅"):
                    print(f"Task {target_id} is now DONE.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4": # Mark BLOCKED (Using modify_task_status)[cite: 1]
            try:
                target_id = int(input("Enter ID to mark BLOCKED: "))
                if modify_task_status(tasks, target_id, "💀"):
                    print(f"Task {target_id} is now BLOCKED.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5": # Increase Priority (Using modify_task_priority)[cite: 1]
            try:
                target_id = int(input("Enter ID: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx < 2:
                        modify_task_priority(tasks, target_id, priorities[idx + 1])
                        print(f"Priority increased to {priorities[idx + 1]}.")
                    else:
                        print("Already at maximum priority.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6": # Decrease Priority (Using modify_task_priority)[cite: 1]
            try:
                target_id = int(input("Enter ID: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx > 0:
                        modify_task_priority(tasks, target_id, priorities[idx - 1])
                        print(f"Priority decreased to {priorities[idx - 1]}.")
                    else:
                        print("Already at minimum priority.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "7": # Show tasks
            print_tasks(tasks)

        else:
            print("Oops! Wrong number. Choose from 1-8. 🤷")

if __name__ == "__main__":
    run_todo_list()
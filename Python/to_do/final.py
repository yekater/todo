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

# --------------------------------

def modify_task_status(list_tasks: list, id_target: int, new_status: str) -> bool:
    """Updates the status field of a specific task."""
    task = search_task_by_id(list_tasks, id_target)
    if task:
        task['status'] = new_status
        return True
    return False

def modify_task_priority(list_tasks: list, id_target: int, new_priority: str) -> bool:
    """Updates the priority field of a specific task[cite: 1]."""
    task = search_task_by_id(list_tasks, id_target)
    if task:
        task['priority'] = new_priority
        return True
    return False

# --------------------------------

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

        elif choice == "1": # Create Task
            desc = input("Description: ")
            if not desc: 
                print("Error: Description c1annot be empty. 🤷")
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

        elif choice == "2": # Delete Task
            try:
                target_id = int(input("Enter ID to delete: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    tasks.remove(task)
                    print("Task deleted. 🗑️")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice in ["3", "4"]: # Mark DONE or BLOCKED
            try:
                target_id = int(input("Enter Task ID: "))
                status_map = {"3": "✅", "4": "💀"}
                if modify_task_status(tasks, target_id, status_map[choice]):
                    print(f"Task {target_id} updated successfully. 🔄")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice in ["5", "6"]: # Increase or Decrease Priority
            try:
                target_id = int(input("Enter Task ID: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    current_idx = priorities.index(task['priority'])
                    new_idx = current_idx + 1 if choice == "5" else current_idx - 1
                    
                    if 0 <= new_idx < len(priorities):
                        modify_task_priority(tasks, target_id, priorities[new_idx])
                        print(f"Priority changed to {priorities[new_idx]}. 🔄")
                    else:
                        print("Priority is already at its limit.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice == "7": # Show tasks
            print_tasks(tasks)

        else:
            print("Oops! Wrong number. Choose from 1-8. 🤷")

if __name__ == "__main__":
    run_todo_list()
def show_menu():
    """Prints the interaction menu options to the console[cite: 1]."""
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
    """Returns the maximum ID + 1. If list is empty, returns 0[cite: 1]."""
    if not list_tasks:
        return 0
    return max(t['id'] for t in list_tasks) + 1

def search_task_by_id(list_tasks: list, id_searched: int):
    """Returns the task dictionary or None if not found[cite: 1]."""
    for task in list_tasks:
        if task['id'] == id_searched:
            return task
    return None

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
    # INITIALIZATION: Start with an empty list[cite: 1]
    tasks = []
    
    priorities = ["low", "medium", "high"]
    
    while True:
        show_menu()
        choice = input("\nChoose what do you want to do 🤔: ")

        if choice == "8":
            print("Good job today! Goodbye, see you soon! 💃🕺👋") 
            break

        elif choice == "1": # Create Task[cite: 1]
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

        elif choice == "2": # Delete Task[cite: 1]
            try:
                target_id = int(input("Enter ID to delete: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    tasks.remove(task)
                    print("Task deleted.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "3": # Mark DONE[cite: 1]
            try:
                target_id = int(input("Enter ID to mark DONE: "))
                task = search_task_by_id(tasks, target_id)
                if task: 
                    task['status'] = "✅"
                    print(f"Task {target_id} marked as done.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice == "4": # Mark BLOCKED[cite: 1]
            try:
                target_id = int(input("Enter ID to mark BLOCKED: "))
                task = search_task_by_id(tasks, target_id)
                if task: 
                    task['status'] = "💀"
                    print(f"Task {target_id} marked as blocked.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice == "5": # Increase Priority[cite: 1]
            try:
                target_id = int(input("Enter ID to increase priority: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx < 2: 
                        task['priority'] = priorities[idx + 1]
                        print(f"Priority increased to {task['priority']}.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice == "6": # Decrease Priority[cite: 1]
            try:
                target_id = int(input("Enter ID to decrease priority: "))
                task = search_task_by_id(tasks, target_id)
                if task:
                    idx = priorities.index(task['priority'])
                    if idx > 0: 
                        task['priority'] = priorities[idx - 1]
                        print(f"Priority decreased to {task['priority']}.")
            except ValueError:
                print("Invalid input. 🤷")

        elif choice == "7": # Show tasks[cite: 1]
            print_tasks(tasks)

        else:
            print("Oops! Wrong number. Choose from 1-8. 🤷")

if __name__ == "__main__":
    run_todo_list()
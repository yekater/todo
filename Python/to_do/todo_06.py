def show_menu():
    """Prints the interaction menu options to the console."""
    print("\n" + "="*30)
    print("      📝 MY TO-DO LIST")
    print("="*30)
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
    """Returns the maximum ID + 1. If list is empty, returns 1."""
    if not list_tasks:
        return 1
    return max(t['id'] for t in list_tasks) + 1

def find_task_by_id(task_list: list, task_id: int):
    for t in task_list:
        if t.get("id") == task_id:
            return t
    return None

def modify_task_status(task_list: list, target_id: int, new_status: str) -> bool:
    task = find_task_by_id(task_list, target_id)
    if task:
        task['status'] = new_status
        return True
    return False

def modify_task_priority(task_list: list, target_id: int, new_priority: str) -> bool:
    task = find_task_by_id(task_list, target_id)
    if task:
        task['priority'] = new_priority
        return True
    return False

def print_tasks(task_list: list):
    """Displays the task list formatted as a table."""
    if not task_list:
        print("\n--- Your list is empty. 🤷 ---")
        return
    
    print(f"\n{'ID':<3} | {'Description':<30} | {'Priority':<10} | {'Status':<13} | {'Tag'}")
    print("-" * 75)
    for t in task_list:
        print(f"{t['id']:<3} | {t['description']:<30} | {t['priority']:<10} | {t['status']:<13} | {t['tag']}")

def run_todo_list():
    """Main flow control for the application."""
    tasks = []
    priorities = ["low", "medium", "high"]
    
    while True:
        show_menu()
        choice = input("\nChoose what do you want to do 🤔: ").strip()

        if choice == "9":
            print("Good job today! Goodbye, see you soon! 💃🕺👋") 
            break

        elif choice == "1":
            desc = input("Description: ").strip()
            if not desc: 
                print("Error: Description cannot be empty. 🤷")
                continue
            
            prio = input("Priority (low/medium/high): ").lower().strip()
            # if a user enters something other than low/medium/high, we will set it to low by default
            final_prio = prio if prio in priorities else "low"
            
            tag = input("Tag: ").strip()
            new_id = generate_new_id_task(tasks)
            
            tasks.append({
                "id": new_id, 
                "description": desc, 
                "priority": final_prio, 
                "status": "pending 🚧",
                "tag": tag
            })
            print(f"✨ Task {new_id} created. ✨")

        elif choice == "2":
            try:
                target_id = int(input("Enter ID to delete: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    tasks.remove(task)
                    print(f"Task {target_id} deleted successfully. 🗑️")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "3":
            try:
                target_id = int(input("Enter ID to mark DONE: "))
                if modify_task_status(tasks, target_id, "Done ✅"):
                    print(f"Task {target_id} is now DONE ✅.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "4":
            try:
                target_id = int(input("Enter ID to mark BLOCKED: "))
                if modify_task_status(tasks, target_id, "Blocked 💀"):
                    print(f"Task {target_id} is now BLOCKED 💀.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "5":
            try:
                target_id = int(input("Enter Task ID: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    current_prio = task['priority']
                    if current_prio in priorities:
                        idx = priorities.index(current_prio)
                        if idx < 2:
                            new_prio = priorities[idx + 1]
                            modify_task_priority(tasks, target_id, new_prio)
                            print(f"Priority increased to {new_prio} ⬆️.")
                        else:
                            print("Priority is already at the maximum (high). 🤯")
                    else:
                        # if a user enters something other than low/medium/high, we will set it to low by default
                        task['priority'] = "low"
                        print("Resetting invalid priority to 'low'.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "6":
            try:
                target_id = int(input("Enter Task ID: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    current_prio = task['priority']
                    if current_prio in priorities:
                        idx = priorities.index(current_prio)
                        if idx > 0:
                            new_prio = priorities[idx - 1]
                            modify_task_priority(tasks, target_id, new_prio)
                            print(f"Priority decreased to {new_prio} ⬇️.")
                        else:
                            print("Priority is already at the minimum (low). 🏖️")
                    else:
                        task['priority'] = "low"
                        print("Resetting invalid priority to 'low'.")
                else:
                    print("Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        elif choice == "7":
            print_tasks(tasks)

        elif choice == "8":
            try:
                target_id = int(input("Enter ID to find 🕵️: "))
                task = find_task_by_id(tasks, target_id)
                if task:
                    print("\n🔎 Task Found:")
                    print(f"ID:          {task['id']}")
                    print(f"Description: {task['description']}")
                    print(f"Priority:    {task['priority']}")
                    print(f"Status:      {task['status']}")
                    print(f"Tag:         {task['tag']}")
                else:
                    print("❌ Task not found. 🤷")
            except ValueError:
                print("Invalid input. Please enter a number. 🤷")

        else:
            print("Oops! Wrong choice. Please enter a number from 1 to 9. 🤷")

if __name__ == "__main__":
    run_todo_list()
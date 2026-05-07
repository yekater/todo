import json
import os
import random

# --- JSON Persistence Functions ---

def filter_tasks(task_list: list) -> list:
    """Returns a new list excluding tasks tagged as 'TEST'[cite: 1]."""
    return [t for t in task_list if t.get("tag") != "TEST"]

def load_tasks(file_name="tasks.json"):
    """Loads tasks from a JSON file. Returns an empty list if file doesn't exist[cite: 1]."""
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(task_list, file_name="tasks.json"):
    """Filters out test tasks and then saves the list to a JSON file[cite: 1]."""
    # We filter the tasks so test data stays only in memory, not in the file[cite: 1]
    tasks_to_save = filter_tasks(task_list)
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(tasks_to_save, f, indent=4, ensure_ascii=False)
        print(f"💾 Tasks successfully saved to '{file_name}' (Test tasks excluded).")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# --- Core Functions ---

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
    print("🇨. Load tasks (JSON) 📂")
    print("🇬. Save tasks (JSON) 💾")
    print("🇹. TEST-create test task 🧪")
    print("🇷. RESET-Clear task list 🧨")
    print("9️⃣. Exit 👋")

def generate_new_id_task(list_tasks: list) -> int:
    """Returns the maximum ID + 1. If list is empty, returns 1[cite: 1]."""
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
    """Displays the task list formatted as a table[cite: 1]."""
    if not task_list:
        print("\n--- Your list is empty. 🤷 ---")
        return
    
    print(f"\n{'ID':<3} | {'Description':<30} | {'Priority':<10} | {'Status':<13} | {'Tag'}")
    print("-" * 75)
    for t in task_list:
        print(f"{t['id']:<3} | {t['description']:<30} | {t['priority']:<10} | {t['status']:<13} | {t['tag']}")

def run_todo_list():
    """Main flow control for the application."""
    tasks = load_tasks() 
    priorities = ["low", "medium", "high"]
    
    while True:
        show_menu()
        choice = input("\nChoose what do you want to do 🤔: ").strip().upper()

        if choice == "9":
            save_tasks(tasks) 
            print("Good job today! Goodbye, see you soon! 💃🕺👋") 
            break

        elif choice == "1":
            desc = input("Description: ").strip()
            if not desc: 
                print("Error: Description cannot be empty. 🤷")
                continue
            
            prio = input("Priority (low/medium/high): ").lower().strip()
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

        elif choice == "C":
            tasks = load_tasks()
            print("📂 Tasks loaded from storage.")

        elif choice == "G":
            save_tasks(tasks)

        elif choice == "T":
            random_desc = "TEST TASK " + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
            random_prio = random.choice(priorities)
            new_id = generate_new_id_task(tasks)
            tasks.append({
                "id": new_id,
                "description": random_desc,
                "priority": random_prio,
                "status": "pending 🚧",
                "tag": "TEST" # This tag ensures it gets filtered during save[cite: 1]
            })
            print(f"🧪 Random task {new_id} created successfully!")

        elif choice == "R":
            confirm = input("⚠️ Are you sure you want to DELETE ALL tasks? (Y/N): ").strip().upper()
            if confirm == "Y":
                tasks.clear()
                print("🧨 All tasks have been deleted.")

        else:
            print("Oops! Wrong choice. Please enter a number or letter from the menu. 🤷")

if __name__ == "__main__":
    run_todo_list()
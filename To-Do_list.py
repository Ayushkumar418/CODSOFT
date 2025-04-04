import json
import os
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

TODO_FILE = 'todo_list.json'

def print_border(width=80):
    print(Fore.CYAN + "=" * width)

def print_header(text):
    print_border()
    print(Fore.BLUE + text.center(80))
    print_border()

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = json.load(file)
            # Convert old format (strings) to new format (dictionaries)
            return [task if isinstance(task, dict) else {
                'title': task,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'status': 'PENDING'
            } for task in tasks]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "\nNo tasks in the list.")
    else:
        print(Fore.CYAN + "\nYour Tasks:")
        print_border()
        for i, task in enumerate(tasks, start=1):
            if isinstance(task, dict):
                status = task.get('status', 'PENDING')
                created_at = task.get('created_at', 'Unknown')
                status_color = Fore.GREEN if status == 'COMPLETED' else Fore.YELLOW
                print(f"{Fore.WHITE}{i}. {task['title']}")
                print(f"   {Fore.BLUE}Created: {created_at}")
                print(f"   Status: {status_color}{status}{Style.RESET_ALL}")
            else:
                # Handle old format (strings)
                print(f"{Fore.WHITE}{i}. {task}")
        print_border()

def add_task(tasks):
    print_header("Add New Tasks")
    try:
        num_tasks = int(input(Fore.YELLOW + "Number of tasks: "))
        for i in range(num_tasks):
            task = {
                'title': input(Fore.YELLOW + f"Enter the {i+1} task: "),
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'status': 'PENDING'
            }
            tasks.append(task)
        save_tasks(tasks)
        print(Fore.GREEN + "\n✓ Task added successfully!")
    except ValueError:
        print(Fore.RED + "\n✗ Please enter a valid number!")
    except Exception as e:
        print(Fore.RED + f"\n✗ Error adding task: {str(e)}")

def update_task(tasks):
    print_header("Update Task")
    try:
        if not tasks:
            print(Fore.YELLOW + "\nNo tasks to update!")
            return
        
        display_tasks(tasks)
        task_index = int(input(Fore.YELLOW + "\nEnter task number to update: ")) - 1
        
        if 0 <= task_index < len(tasks):
            # Convert old format to new format if needed
            if not isinstance(tasks[task_index], dict):
                tasks[task_index] = {
                    'title': tasks[task_index],
                    'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'status': 'PENDING'
                }
            
            print(Fore.CYAN + "\n1. Update task title")
            print("2. Mark as completed")
            print("3. Mark as pending")
            
            choice = input(Fore.YELLOW + "\nEnter your choice (1-3): ")
            
            if choice == '1':
                tasks[task_index]['title'] = input(Fore.YELLOW + "Enter new task title: ")
            elif choice == '2':
                tasks[task_index]['status'] = 'COMPLETED'
            elif choice == '3':
                tasks[task_index]['status'] = 'PENDING'
            else:
                print(Fore.RED + "\n✗ Invalid choice!")
                return
                
            save_tasks(tasks)
            print(Fore.GREEN + "\n✓ Task updated successfully!")
        else:
            print(Fore.RED + "\n✗ Invalid task number!")
    except ValueError:
        print(Fore.RED + "\n✗ Please enter a valid number!")

def remove_task(tasks):
    print_header("Remove Task")
    try:
        if not tasks:
            print(Fore.YELLOW + "\nNo tasks to remove!")
            return
            
        display_tasks(tasks)
        task_index = int(input(Fore.YELLOW + "\nEnter task number to remove: ")) - 1
        
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(Fore.GREEN + f"\n✓ Task '{removed_task['title']}' removed successfully!")
        else:
            print(Fore.RED + "\n✗ Invalid task number!")
    except ValueError:
        print(Fore.RED + "\n✗ Please enter a valid number!")

def main():
    tasks = load_tasks()
    
    while True:
        print_header("TO-DO LIST MANAGER")
        print(Fore.CYAN + """
        1. 📝 Add Task
        2. 📋 View Tasks
        3. ✏️  Update Task
        4. ❌ Remove Task
        5. 🚪 Exit
        """)
        
        try:
            choice = input(Fore.YELLOW + "Choose an option (1-5): ")
            
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                display_tasks(tasks)
            elif choice == '3':
                update_task(tasks)
            elif choice == '4':
                remove_task(tasks)
            elif choice == '5':
                print_header("Thank you for using To-Do List Manager!")
                break
            else:
                print(Fore.RED + "\n✗ Invalid option. Please try again.")
        except Exception as e:
            print(Fore.RED + f"\n✗ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

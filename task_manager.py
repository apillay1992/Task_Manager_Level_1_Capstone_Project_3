from datetime import date, datetime
import csv

print("*******************Task Manager******************\n")

# Request user input for username and password.
user_name = input("Enter username: ")
pass_word = input("Enter password: ")

def open_user_txt():
    """
    Reads the contents of 'user.txt' and returns a list of lines without newline characters.

    Returns:
        list: A list of user credentials (username, password) from 'user.txt'.
    """
    mylines = []
    with open('user.txt', 'r+') as user:
        for line in user:
            mylines.append(line.rstrip("\n"))
    return mylines

def cridentials():
    """
    Validates the user's credentials. If incorrect, prompts the user to re-enter until valid credentials are provided.
    On successful login, the user is welcomed.
    """
    global user_name
    global pass_word
    access = f"{user_name}, {pass_word}"
    access.split(", ")

    while access not in open_user_txt():
        print("Incorrect username or password!\n")
        user_name = input("Enter username: ")
        pass_word = input("Enter password: ")
        access = f"{user_name}, {pass_word}"
        access.split(", ")

    print(f"\nLogin successful!\nWelcome! ... {user_name}\n")

def reg_user():
    """
    Registers a new user if the current user is 'adm1n'. Prevents duplication of usernames.
    New credentials are appended to 'user.txt'.
    """
    with open('user.txt', 'a+') as user:
        password = input("Enter password to validate user: ")
        if password == 'adm1n':
            print("Access granted!\n")
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            access = f'{new_username}, {new_password}'
            access.split(", ")

            while access in open_user_txt():
                print("Username and password already exist, try again.")
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")
                access = f'{new_username}, {new_password}'
                access.split(", ")

            confirm_password = input("Confirm password: ")
            if confirm_password == new_password:
                print("User added successfully!")
                user.write(f"\n{new_username}, {new_password}")
            else:
                print("Passwords do not match!")
        else:
            print("Access Denied!")

def add_task():
    """
    Adds a new task to 'tasks.txt' with the user's input for task details.
    The task status is set to 'No' by default.
    """
    current_username = input("Please enter your username:\n")
    task_title = input("Please enter your task title:\n")
    task_description = input("Please enter the description of the task:\n")
    today = date.today()
    d1 = today.strftime("%d %b %Y")
    due_date = input("Please enter the due date of the task. e.g. 01 Dec 2020:\n")
    task_complete = 'No'
    print("Task status set to: No")
    main_menu = input("Please enter -1 to return to the main menu: ")

    with open('tasks.txt', 'a+') as tasks:
        tasks.write(f"{current_username}, {task_title}, {task_description}, {d1}, {due_date}, {task_complete}\n")

def admin_menu():
    """
    Displays the admin menu options.
    """
    print("\nPlease select one of the following options:\n"
          "r  - register new user\n"
          "a  - add task\n"
          "va - view all tasks\n"
          "vm - view my tasks\n"
          "gr - generate reports\n"
          "ds - display statistics\n"
          "e  - exit\n")

def user_menu():
    """
    Displays the user menu options.
    """
    print("\nPlease select one of the following options:\n"
          "r  - register new user\n"
          "a  - add task\n"
          "va - view all tasks\n"
          "vm - view my tasks\n"
          "e  - exit\n")

def admin_statistics():
    """
    Displays the statistics of all users and tasks.
    Reads data from 'task_overview.txt' and 'user_overview.txt'.
    """
    print("Your statistics below:\n")
    print("*Note: If there are no statistics displayed below, please use the 'gr' function to generate the tasks and users overview.\n")
    
    # Count and display total number of registered users
    count = 0 
    with open('user.txt', 'r') as f: 
        for line in f:
            count += 1 
    print("Total number of users registered:", count) 
    
    # Count and display total number of tasks
    count = 0 
    with open('tasks.txt', 'r') as f: 
        for line in f: 
            count += 1 
    print("Total number of tasks:", count)
    
    # Display task overview
    with open('task_overview.txt', 'r') as file:
        print('\n****Tasks Overview****\n')
        for line in file:
            print(line.strip())
    
    # Display user overview
    with open('user_overview.txt', 'r') as file:
        print('\n****User Overview****\n')
        for line in file:
            print(line.strip())
            
    main_menu = input("Please enter -1 to return to the main menu: ")

def task_dict():
    """
    Reads 'tasks.txt' and returns a dictionary representation of the tasks.

    Returns:
        dict: A dictionary where each key is a task number, and the value is another dictionary with task details.
    """
    with open('tasks.txt', 'r') as file:
        task_dictionary = {}
        for i, line in enumerate(file):
            val = line.strip().split(', ')
            task_dictionary[i + 1] = {
                "username": val[0],
                "task": val[1],
                "task_discrip": val[2],
                "date_loaded": val[3],
                "due_date": val[4],
                "task_status": val[5]
            }
    return task_dictionary

def user_dict():
    """
    Reads 'user.txt' and returns a dictionary representation of the users.

    Returns:
        dict: A dictionary where each key is a user number, and the value is another dictionary with user details.
    """
    with open('user.txt', 'r') as file:
        user_dictionary = {}
        for i, line in enumerate(file):
            val = line.strip().split(', ')
            user_dictionary[i + 1] = {
                "user_name": val[0],
                "password": val[1]
            }
    return user_dictionary 

def view_all():
    """
    Displays all tasks in a user-friendly manner.
    """
    task_dictionary = task_dict()
    for i in task_dictionary:
        task = task_dictionary[i]
        print(f"\n{i}. Task: \t\t{task['task']}")
        print(f"   Assigned to: \t{task['username']}")
        print(f"   Task description: \t{task['task_discrip']}")
        print(f"   Date assigned: \t{task['date_loaded']}")
        print(f"   Due date: \t\t{task['due_date']}")
        print(f"   Task Complete?: \t{task['task_status']}\n")

    main_menu = input("Please enter -1 to return to the main menu: ")
    
def view_mine():
    """
    Displays the tasks assigned to the logged-in user and allows the user to edit or mark tasks as complete.
    """
    task_dictionary = task_dict()
    user_tasks = []

    for i in task_dictionary:
        task = task_dictionary[i]
        if user_name == task['username']:
            print(f"\n{i}. Task: \t\t{task['task']}")
            print(f"   Assigned to: \t{task['username']}")
            print(f"   Task description: \t{task['task_discrip']}")
            print(f"   Date assigned: \t{task['date_loaded']}")
            print(f"   Due date: \t\t{task['due_date']}")
            print(f"   Task Complete?: \t{task['task_status']}\n")
            user_tasks.append(i)         

    line_num = int(input("Select a number to edit task or type -1 to return to the menu: "))

    if line_num != -1 and line_num in user_tasks:
        edit_task(line_num, task_dictionary)
        
def edit_task(task, dictionary):
    """
    Edits or marks the selected task as complete based on the user's choice.

    Args:
        task (int): The task number to be edited or marked as complete.
        dictionary (dict): The dictionary containing task details.
    """
    line_num = input(f"Edit task ({task}) or mark task ({task}) as complete: Enter 'mark' or 'edit': ")
    print('')
    
    if line_num == 'mark':
        if dictionary[task]["task_status"] == 'Yes':
            print("Task completed, unable to mark again!\n")
            main_menu = input("Please enter -1 to return to the main menu: ")
        else:
            dictionary[task]["task_status"] = 'Yes'
            print(f"Task '{dictionary[task]['task']}' marked as complete.\n")
            main_menu = input("Please enter -1 to return to the main menu: ")

    elif line_num == 'edit':
        if dictionary[task]["task_status"] == 'Yes':
            print("Task already completed, unable to edit!\n")
            main_menu = input("Please enter -1 to return to the main menu: ")
        else:
            edit_option = input("Enter 'edit' to change username or 'date' to change the due date: ")
            if edit_option == 'edit':
                dictionary[task]["username"] = input("Enter the new username: ")
            elif edit_option == 'date':
                dictionary[task]["due_date"] = input("Enter the new due date: ")

    # Rewrite the 'tasks.txt' file with updated task information.
    with open('tasks.txt', 'w') as file:
        for i in dictionary:
            file.write(f"{dictionary[i]['username']}, {dictionary[i]['task']}, {dictionary[i]['task_discrip']}, "
                       f"{dictionary[i]['date_loaded']}, {dictionary[i]['due_date']}, {dictionary[i]['task_status']}\n")

    print("Task updated successfully!\n")
    main_menu = input("Please enter -1 to return to the main menu: ")

def generate_reports():
    """
    Generates reports for tasks and users, storing them in 'task_overview.txt' and 'user_overview.txt'.
    """
    task_dictionary = task_dict()
    user_dictionary = user_dict()

    # Task Overview
    with open('task_overview.txt', 'w') as file:
        file.write("************TASK OVERVIEW************\n\n")
        file.write(f"Total number of tasks: {len(task_dictionary)}\n")
        
        completed_tasks = sum(1 for task in task_dictionary.values() if task['task_status'] == 'Yes')
        file.write(f"Total number of completed tasks: {completed_tasks}\n")
        
        uncompleted_tasks = sum(1 for task in task_dictionary.values() if task['task_status'] == 'No')
        file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        
        overdue_tasks = sum(1 for task in task_dictionary.values() 
                            if datetime.strptime(task['due_date'], "%d %b %Y") < datetime.today() and task['task_status'] == 'No')
        file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
        
        incomplete_percentage = (uncompleted_tasks / len(task_dictionary)) * 100
        file.write(f"Percentage of incomplete tasks: {incomplete_percentage:.2f}%\n")
        
        overdue_percentage = (overdue_tasks / len(task_dictionary)) * 100
        file.write(f"Percentage of overdue tasks: {overdue_percentage:.2f}%\n")
    
    # User Overview
    with open('user_overview.txt', 'w') as file:
        file.write("************USER OVERVIEW************\n\n")
        file.write(f"Total number of users registered: {len(user_dictionary)}\n")
        
        for user in user_dictionary.values():
            tasks_assigned = [task for task in task_dictionary.values() if task['username'] == user['user_name']]
            file.write(f"\n{user['user_name']}:\n")
            file.write(f"Total number of tasks assigned: {len(tasks_assigned)}\n")
            
            completed_tasks = sum(1 for task in tasks_assigned if task['task_status'] == 'Yes')
            file.write(f"Total number of completed tasks: {completed_tasks}\n")
            
            uncompleted_tasks = sum(1 for task in tasks_assigned if task['task_status'] == 'No')
            file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
            
            overdue_tasks = sum(1 for task in tasks_assigned 
                                if datetime.strptime(task['due_date'], "%d %b %Y") < datetime.today() and task['task_status'] == 'No')
            file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
            
            if tasks_assigned:
                percentage_tasks = (len(tasks_assigned) / len(task_dictionary)) * 100
                file.write(f"Percentage of total tasks assigned to user: {percentage_tasks:.2f}%\n")
                
                if len(tasks_assigned) > 0:
                    completed_percentage = (completed_tasks / len(tasks_assigned)) * 100
                    file.write(f"Percentage of completed tasks: {completed_percentage:.2f}%\n")
                    
                    overdue_percentage = (overdue_tasks / len(tasks_assigned)) * 100
                    file.write(f"Percentage of overdue tasks: {overdue_percentage:.2f}%\n")

    print("Reports generated successfully!\n")
    main_menu = input("Please enter -1 to return to the main menu: ")

# Main program logic
def main():
    cridentials()

    while True:
        if user_name == 'adm1n':
            admin_menu()
            menu_option = input("Enter your selection here: ").strip().lower()
            if menu_option == 'r':
                reg_user()
            elif menu_option == 'a':
                add_task()
            elif menu_option == 'va':
                view_all()
            elif menu_option == 'vm':
                view_mine()
            elif menu_option == 'gr':
                generate_reports()
            elif menu_option == 'ds':
                admin_statistics()
            elif menu_option == 'e':
                print("Goodbye!")
                break
            else:
                print("Invalid selection, please try again.")
        else:
            user_menu()
            menu_option = input("Enter your selection here: ").strip().lower()
            if menu_option == 'r':
                reg_user()
            elif menu_option == 'a':
                add_task()
            elif menu_option == 'va':
                view_all()
            elif menu_option == 'vm':
                view_mine()
            elif menu_option == 'e':
                print("Goodbye!")
                break
            else:
                print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()

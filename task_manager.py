# imported date and time modules.
# imported csv comma seperated values.
from datetime import date
import datetime
import csv

print("""*******************Task Manager******************""")
print('')

# requested users input for username and password.
user_name = input("Enter username: ")
pass_word = input("Enter password: ")


# defined a function called open_user_txt().
# opened user.txt for reading and writing.
# used a for loop to iterate through lines and appended to list mylines[], used the rstrip method to remove new lines "\n".
def open_user_txt():
    mylines = [] 
    with open('user.txt', 'r+') as user:
        for line in user:
            mylines.append(line.rstrip("\n"))
            

    return mylines


# defined a function called cridentials().
# used global variable user_name and pass_word for use later in program.
# created a variable called access stored user_name and pass_word after using split method into a list.
# called the open_user_txt().
# used a while loop to check if variable access is in list mylines[].
# if access in mylines[] access granted otherwise incorrect cridentials.
def cridentials():
    
    global user_name
    global pass_word
    access = (f"{user_name}, {pass_word}")
    access.split(",")
    open_user_txt()

    while access not in open_user_txt():
        
        print("Incorrect username or password!")
        print()
        user_name = input("Enter username: ")
        pass_word = input("Enter password: ")
        access = (f"{user_name}, {pass_word}")
        access.split(",")
        open_user_txt()

    if access in open_user_txt():
        print('')
        print(f"login successuful!")
        print('')
        print(f"Welcome! ... {user_name}")


# defined a function called reg_user().
# opened user.txt for appending.
# requested user input for password, if password equal to 'adm1n' access is granted.
# created a variable called access which stores the username and password in a list.
# if access in function open_user_txt() means password already created, access denied, user would not be able to duplicate username and password.
# if access not in function open_user_txt() user confirms password added to user.txt.
def reg_user():
    
    with open('user.txt', 'a+') as user:
        
        password = input("Enter password to validate user: ")
        if password == 'adm1n':
            print("Access granted!")
            print('')
            new_username = input("Enter new username: ") 
            new_password = input("Enter new password: ")
            access = (f'{new_username}, {new_password}')
            access.split(", ")

            while access in open_user_txt():
                print("Username and password already exits, try again?")
                
                new_username = input("Enter new username: ") 
                new_password = input("Enter new password: ")
                access = (f'{new_username}, {new_password}')
                access.split(", ")
            if access not in open_user_txt():
            
                confirm_password = input("Confirm password: ")
            
            if confirm_password == new_password:
                print("User added successfully!") 
                user.write(f"\n{new_username}, {new_password}") 
            else:
                print("Your passwords do not match!") 
        else:
            print("Access Denied!") 


# define the funstion called add_task().
# requested users input, for task information.
# open task.txt for appending and wrote task information to file.
def add_task():

    
    current_username = input("Please enter your username:\n") 
    task_title = input("Please enter your task title:\n") 
    task_description = input("Please enter the description of the task:\n") 
    today = date.today() 
    d1 = today.strftime("%d %b %Y") 
    due_date = input("Please enter the due date of the task. e.g. 01 Dec 2020:\n") 
    task_complete = 'No'
    print(f"Task status set to: No")
    main_menu = input("Please enter -1 to return to the main menu: ")

    with open('tasks.txt', 'a+') as tasks:
        tasks.write(f"{current_username}, {task_title}, {task_description}, {d1}, {due_date}, {task_complete}\n") 
    
# defined function called admin_menu().
# displayed appropriate menu for admin user.
def admin_menu():
    
    print('')
    print("""Please select one of the following options:
    r - register new user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit\n""")


# defined a function called user_menu().
# displayed appropriate menu for user.
def user_menu():
    
    print('')
    print("""Please select one of the following options:
    r - register new user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit\n""")
    
# defined a function called admin_ statistics() to display all tasks and users info.
def admin_statistics():
    
    print("Your statistics below:")
    print('')
    print("*Note if there are are no statistics displayed below, please use the 'gr' function to generate the tasks and users overview.")
    print('')
    count = 0 
    with open('user.txt', 'r') as f: 
          for line in f:
                count += 1 
    print("Total number of users registed:", count) 
    
    count = 0 
    with open('tasks.txt', 'r') as f: 
        for line in f: 
            count += 1 
    print("Total number of tasks:", count)
    
    # opened task_overview.txt in read mode to perform the display
    with open('task_overview.txt', 'r') as file:
        print('\n****Tasks Overview****\n')
        for line in file:
            print(line.strip())
    # opened user_over.txt in read mode to perfom the display
    with open('user_overview.txt', 'r') as file:
        
        print('\n****user Overview****\n')
        for line in file:
            print(line.strip())
            
    main_menu = input("Please enter -1 to return to the main menu: ")

# defined a function called task_dict().
# created a dictionary with tasks.txt.
def task_dict():
    with open('tasks.txt', 'r') as file:
            task_dictionary = {}
            
            for i,line in enumerate(file):
                val = line.strip().split(', ')
                task_dictionary[i + 1] = {"username" : val[0],"task" : val[1],"task_discrip" : val[2],"date_loaded": val[3],"due_date" : val[4],"task_status" : val[5]}
  
    return task_dictionary


# defined a function called user_dict().
# created a dictionary with user.txt.
def user_dict():
    with open('user.txt', 'r') as file:
                user_dictionary = {}
                
                for i,line in enumerate(file):
                    val = line.strip().split(', ')
                    user_dictionary[i + 1] = {"user_name" : val[0],"password" : val[1]}

    
    return user_dictionary 



# defined a function called view_all().
# created a variable called task_dictionary which stores function task_dict().
# printed out tasks in a user friendly manner.
def view_all():
    task_dictionary = task_dict()
        
    for i in task_dictionary:
        task = task_dictionary[i]

        print(f"\n{i}. Task: \t\t{task['task']}")
        print(f"   Assigned to: \t{task['username']}")
        print(f"   Task description: \t{task['task_discrip']}")
        print(f"   Date assigned: \t{task['date_loaded']}")
        print(f"   Due date: \t\t{task['due_date']}")
        print(f"   Task Complete?: \t{task['task_status']}")
        print('')

    main_menu = input("Please enter -1 to return to the main menu: ")
    
    if main_menu == -1:
        
        return

# defined a function called view_mine().
# created a variable called task_dictionary which stores function task_dict().
# created a list called user_task, used a counter appended each task to user_task.
# if username equal to task key, print all usernames tasks.
def view_mine():
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
            print(f"   Task Complete?: \t{task['task_status']}")
            print('')
            user_tasks.append(i)         

    line_num = int(input("Select a number to edit task or type -1 to return to the menu: "))

    # requested users input, if line_num not in user_tasks call function edit_task with parameters line_num and task_dictionary.    
    if line_num != -1 and line_num in user_tasks:
        edit_task(line_num,task_dictionary)
        
    elif line_num == -1:
        return

            
# define a function called edit_task() with parameters task and dictionary.
# Requested users input to choose 'mark' or 'edit'.
def edit_task(task, dictionary):

    line_num = input(f"Edit task ({task}) or mark task ({task}) as complete: Enter '(mark)' or '(edit)': ")
    print('')
    # if input equals 'mark'
    # if dictionary [task_status] equals to "Yes"
    # print "Task already completed"
    # -1 to return to main menu.
    if line_num == 'mark':
        if dictionary[task]["task_status"] == 'Yes':
            print("Task completed, unable to mark again!")
            print('')
            main_menu = input("Please enter -1 to return to the main menu: ")
        # dictionary [task_status] now is changed to "Yes"
        # -1 to return to main menu
        else:
            dictionary[task]["task_status"] = 'Yes'
            print(f"Task '{dictionary[task]['task']}' marked as complete.")
            print('')
            main_menu = input("Please enter -1 to return to the main menu: ")
    # otherwise if input equals to 'edit'
    # if dictionary [task_status] equals to 'Yes'
    # print task already complete.
    elif line_num == 'edit':
        if dictionary[task]['task_status'] == 'Yes':
            print("Task already complete!")
        # Requested users input.
        user_input1 = input(f"Change user or change date, please choose (user) or (date): ")
        # if user input equals to 'user'.
        # requested user to input new username.
        # dictionary [username] is changed to new username
        if user_input1 == 'user':
            new_user_input1 = input("Please enter the new user: ")
            dictionary[task]['username'] = new_user_input1
            main_menu = input("Please enter -1 to return to the main menu: ")
        # if user_name_1 == 'date'
        # requested user to input new due date
        # dicitonary [due_date] value is changed to new due date
        elif user_input1 == 'date':
            date_input = input("Please enter the new due date: ")
            dictionary[task]['due_date'] = date_input
            main_menu = input("Please enter -1 to return to the main menu: ")
    # opened tasks.txt for writing.
    # wrote new changes to from dictionary to tasks.txt.
    with open('tasks.txt', 'w') as file:
        for i in dictionary:
            file.write(f"{dictionary[i]['username']}, {dictionary[i]['task']}, {dictionary[i]['task_discrip']}, {dictionary[i]['date_loaded']}, {dictionary[i]['due_date']}, {dictionary[i]['task_status']}\n")


# Defined a function called task_overview().
# task_dictionary is equal to task_dic().
# created counter for comp_tasks, to count all "yes" values in task_dictionary.
# created counter for incomp_tasks, to count all "No" values in task_dictionary.
# created counter for overdue_tasks, to count all tasks past current date.
def task_overview():
    task_dictionary = task_dict()
    comp_tasks = 0
    incomp_tasks = 0
    overdue_tasks = 0
    
    # created textflie called task_overview for writing.
    with open('task_overview.txt', 'w',) as file:
        for i in task_dictionary:

            
            task = task_dictionary[i]

            # if value dictionary [task_status] equals to 'Yes'
            if 'Yes' == task['task_status']:
                comp_tasks += 1 # comp_tasks incremented by 1
            # if value dictionary [task_status equals to 'No'
            elif 'No' == task['task_status']:
                incomp_tasks += 1 # comp_tasks incremented by 1
                
            # declared a variable called d1 and changed the format of dictionary [due_date] to compare with current date. 
            d1 = datetime.datetime.strptime(task['due_date'], '%d %b %Y')
            # if d1 less than current date and dictionary value [task_status is equal to 'No' 
            if d1 < datetime.datetime.today() and 'No' == task['task_status']:
                overdue_tasks += 1 # overdue is incremented by 1.
                
        # Declared a variable called percent_incomp1 to calculate the percentage of incompleted tasks.    
        percent_incomp1 = (incomp_tasks * 100) / (len(task_dictionary))
        percent_incomp = round(percent_incomp1,2) # rounded to 2 decimal place

        # Declared a variable called percent_overdue1 to calculate the percentage of overdue tasks.
        percent_overdue1 = (overdue_tasks * 100) / (len(task_dictionary))
        percent_overdue = round(percent_overdue1,2)

        
        # Wrote all info the text file.      
        file.write(f"There are {len(task_dictionary)} number of tasks tracked and generated.\n")
        file.write(f"There are {comp_tasks} completed tasks in task manager.\n")
        file.write(f"There are {incomp_tasks} incompleted tasks in task manager.\n")
        file.write(f"There are {overdue_tasks} incomplete tasks that are overdue tasks.\n")
        file.write(f"There are {percent_incomp}% incompleted tasks.\n")
        file.write(f"There are {percent_overdue}% overdue tasks.\n")
        print("Tasks overview written to file")
    
        
# Defined a function called user_overview()    
def user_overview():
    
    user_dictionary = user_dict()
    task_dictionary = task_dict()
    # Created text file called user_over.txt for writing,
    with open('user_overview.txt', 'w') as file:
        # wrote the number of registed users by using the len() function to count items in user_dictionary.
        file.write(f"There are {len(user_dictionary)} number of users registered with task manager\n")
        # wrote the number of tasks by using the len() funciton to count the items in task_dictionary.
        file.write(f"There are {len(task_dictionary)} number of tasks generated using task manager")
        for i in user_dictionary:
            # declared a new variable called new_user.
            new_user = user_dictionary[i]['user_name']
            # set counter for the variables belowl.
            count_tasks = 0
            user_comp_tasks = 0
            user_incomp_tasks = 0
            overdue_tasks = 0
            
            # defined a variable called x, used a for loop to iterate through task dictionary.
            for x in task_dictionary:
                task = task_dictionary[x]
                # if new_user found in task_dictionary [username] 
                if new_user in task_dictionary[x]['username']:
                    count_tasks +=1 # count_tasks in incremented by 1 
                    # if task[task_status] in task dictionary equal to 'Yes'
                    if task['task_status'] == 'Yes':
                        user_comp_tasks += 1 # user_comp_tasks incremented by 1
                    # otherwise if task[task_status] equal to 'No'
                    elif task['task_status'] == 'No':
                        user_incomp_tasks += 1 # user_incomp_tasks incremented by 1
                    # declared a variable called d1 to change task [due_date] to format '%d %b %Y'
                    d1 = datetime.datetime.strptime(task['due_date'], '%d %b %Y')
                    # if d1 less than todays date and task [task_status] equals to 'No'
                    if d1 < datetime.datetime.today() and 'No' == task['task_status']:
                         overdue_tasks += 1 # overdue_tasks in incremented by 1 
            # calculated percentage of completed tasks in tasks.txt
            # rounded of to 2 decimal place
            if user_comp_tasks > 0:
                percent_tasks_comp1 = (user_comp_tasks * 100 )/ count_tasks
                percent_tasks_comp = round(percent_tasks_comp1,2)
            # if user_comp_task equal to zero
            # completed tasks are zero
            elif user_comp_tasks == 0:
                percent_tasks_comp = 0
            # Calculate the percentage of incomplete tasks in tasks.txt.
            # Rounded of to 2 decimal places.
            if user_incomp_tasks > 0:
                percent_tasks_incomp1 = (user_incomp_tasks * 100) / count_tasks
                percent_tasks_incomp = round(percent_tasks_incomp1,2)
            # if user_incomp_tasks equals to zero
            # incompleted tasks are zero
            elif user_incomp_tasks == 0:
                percent_tasks_incomp = 0
            # Calculated the percentage of overdue tasks
            # rounded off to 2 decimal places
            if overdue_tasks > 0:
                percentage_overdue1 = (overdue_tasks * 100) / (user_incomp_tasks)
                percentage_overdue = round(percentage_overdue1,2)
            # if overdue_tasks equals to zero
            # overdue tasks are zero 
            elif overdue_tasks == 0:
                percentage_overdue = 0

            # Wrote all totals and percentages to users.txt.
            file.write("\n")
            file.write(f"\nThe total tasks assigned to user {new_user} is {count_tasks}\n")
            file.write(f"There are {(float(count_tasks) * 100) / float(len(task_dictionary))}% of tasks assigned to user {new_user}\n")
            file.write(f"There are {percent_tasks_comp}% of tasks assigned to user {new_user}\n")
            file.write(f"There are {percent_tasks_incomp}% of tasks assigned to user {new_user} which are not completed \n")
            file.write(f"There are {percentage_overdue}% of tasks assigned to user {new_user} which are not completed and are overdue.")
            
        print("users overview written to file")
        main_menu = input("Please enter -1 to return to the main menu: ")

# defined a program called exit_program()
# used the exit function which terminates the program
def exit_program(): 
    print("Good Bye!")
    return exit()

# defined a function called generate_reports() which calls on function task_overview() and user_overiew()
def generate_reports():
    task_overview()
    user_overview()

# defined a function called final program() which calls on each function when needed.
# Used a infinite while loop to keep the program running all the time.
# Used conditional statements to call each function as per the users input.
def final_program():
    
    cridentials()
    
    # user admin functions
    while user_name == 'admin':
        admin_menu()
        menu = input()
        if menu == 'ds':
            admin_statistics()
        elif menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr':
            generate_reports()
        elif menu == 'e':
            exit_program()
        
    # standard user functions
    while user_name != 'admin':
        user_menu()
        menu = input()
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'e':
            exit_program()
        

final_program()





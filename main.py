tasks = []

while True:
    print("--- TASK MANAGER---- \n 1. Add Task \n 2. View Tasks \n 3. Delete task \n 4.Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        new_task = input("Please enter the task: ") 
        tasks.append(new_task)
        print("Task Added")
    elif user_choice == "2":
        if not tasks:
            print("No tasks found")
        else:
            for number,task in enumerate(tasks,start = 1):
                print(f"{number}.{task}")
    elif user_choice == "3":
        if not tasks:
            print("No previous tasks")
        else:
            for number,task in enumerate(tasks, start = 1):
                print(f"{number}:{task}")
            delete_number = int(input("Please enter the task you want to be deleted: "))
            delete_index = delete_number - 1
            removed_task = tasks.pop(delete_index)
            print(f"Deleted task : {removed_task}")
    elif user_choice == "4":
        print("Good Bye..!! Have a Nice Day.. :)")
        break
    else:
        print("Invalid input. Please give a value from 1 to 3")

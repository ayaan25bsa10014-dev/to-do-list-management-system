import os
filename="task.txt"
tasks=[]
if os.path.exists(filename):
    with open(filename, "r") as file:
        tasks=[line.strip() for line in file.readlines()]
while True:
    print("--TO_DO_LIST--")
    print("1. add task")
    print("2. view task")
    print("3. delete task")
    print("4. exit")
    c=input("enter your choice: ")
    if c =="1":
        t=input("enter task:")
        tasks.append(t)
        print("task added sucessfully.")
        with open(filename,"a") as file:
            file.write(t+ "/n")
    elif c =="2":
        if len(tasks)==0:
            print("no task has been added")
        else:
            print("your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif c== "3":
        if len(tasks)==0:
            print("there is nothing to delete.")
        else:
            print("select the number of task which you want to delete")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            n=int(input("task number is:  "))
            if 1 <= n <= len(tasks):
                r=(f"delete: {r}")
                with open(filename, "w") as file:
                    for i in tasks:
                        file.write(t + "/n")
            else:
                print("invalid number, please write another number.")
    elif c == "4":
        print("exited program, thanks for visiting our code")
        break
    else:
        print("invalid choice. please try again")
    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("Exiting program.")
        break
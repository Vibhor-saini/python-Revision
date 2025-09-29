# 4️⃣ Exercises for You

1# Create a list of 5 movies, print them, add 2 more, and remove 1.

# movies = ["hero","tiger","dhadak","sukoon","raid"]
# movies.append("raid2")
# movies.append("raid3")
# movies.remove("hero")


2# Slice the list to get the middle 3 movies.

# mid = len(movies) // 2
# print(mid)
# print("Middle 3 movies:", movies[mid-1:mid+2])


3# Create a tuple of 4 cities and try adding a city (see the error).

# cities = ("dehradun","mohali","chilkana","chandigarh")
# cities.append("punjab")
# print(cities)


4# Create a set of 5 numbers, add 2 new numbers (including a duplicate), and print it.

# numbers = {1,2,3,4,5}
# numbers.add(6)
# numbers.add(6)
# print(numbers)

5# Loop through a list, tuple, and set, printing all elements.

# list_num = [1,2,3,4,5]
# tuple_num = (1,2,3,4,5)
# set_num = {1,2,3,4,5}


# for num in list_num:
#     print(num)
# print("------------------------")

# for numm in tuple_num:
#     print(numm)

# print("------------------------")
 
# for nummm in set_num:
#     print(nummm)

# Bonus===========
# movies = ["hero", "tiger", "dhadak", "sukoon", "raid"]

# size = len(movies)
# print("Initial size:", size)

# count = 1
# while size < 10:   # until list has 10 items
#     movies.append(f"raid{count}")  # f-string for "raid1", "raid2", ...
#     count += 1
#     size = len(movies)  # update size

# for movie in movies:
#     print(movie)

# 5️⃣ Mini Project – To-Do List CLI

# You’ll build a simple text-based app:
# Menu: Add task, View tasks, Delete task, Exit
# Use a list to store tasks
# Use loops + if/else for menu options


# 1. Add Task
# 2. View Tasks
# 3. Delete Task
# 4. Exit
# Enter choice: 1
# Enter task: Learn Python
# Task added!

menu = ["1. Add Task", "2. View Tasks", "3. Delete Task", "4. Exit"]
list_of_task = []

ask_user = 0   # start with dummy value

while ask_user != 4:
    for i in menu:
        print(i)
    
    ask_user = int(input("Enter choice: "))

    if ask_user == 1:
        user_task = input("Enter task: ")
        list_of_task.append(user_task)
        print("Task added!")

    elif ask_user == 2:
        if not list_of_task:
            print("No tasks yet.")
        else:
            for task in list_of_task:
                print(task)

    elif ask_user == 3:
        if not list_of_task:
            print("No tasks to delete.")
        else:
            print("Tasks:")
            for i, task in enumerate(list_of_task, start=1):
                print(i, task)
            delete_index = int(input("Enter task number to delete: "))
            if 1 <= delete_index <= len(list_of_task):
                list_of_task.pop(delete_index - 1)
                print("Task deleted!")
            else:
                print("Invalid choice!")

    elif ask_user == 4:
        print("Exiting... Goodbye!")



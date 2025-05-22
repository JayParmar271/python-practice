def todoList():
    tasks_list = []
    end_text=input("end text\n")
    while True:        
        tasks=input("enter your tasks\n")
        if tasks == end_text:
            break
        tasks_list.append(tasks)
    print(f"your todo list is {end_text}")
todoList()

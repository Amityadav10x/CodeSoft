
tasks = []


def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added to the to-do list.')


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed from the to-do list.')
    else:
        print(f'Task "{task}" not found in the to-do list.')


def view_tasks():
    if tasks:
        print('To-Do List:')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')
    else:
        print('To-Do List is empty.')


while True:
    print('\nOptions:')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Tasks')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        task = input('Enter the task: ')
        add_task(task)
    elif choice == '2':
        task = input('Enter the task to remove: ')
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')

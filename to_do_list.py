class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found in the list.')

    def show_tasks(self):
        if not self.tasks:
            print('The task list is empty.')
        else:
            print('Task list:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')


def main():
    todo_list = ToDoList()

    while True:
        print('\nMenu:')
        print('1. Add a task')
        print('2. Remove a task')
        print('3. Show tasks')
        print('4. Exit')

        choice = input('Choose an action (1-4): ')

        if choice == '1':
            task = input('Enter a task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter a task to remove: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()

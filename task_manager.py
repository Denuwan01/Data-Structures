class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        if not self.head or self.head.priority > priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def complete_task(self):
        if not self.head:
            print("No tasks to complete.")
            return
        completed_task = self.head
        self.head = self.head.next
        print(f"Completed task: {completed_task.description}")

    def view_tasks(self):
        if not self.head:
            print("No tasks available.")
            return
        current = self.head
        while current:
            print(f"Task: {current.description}, Priority: {current.priority}")
            current = current.next

# Example Usage
if __name__ == "__main__":
    task_manager = TaskManager()

    # Adding tasks
    task_manager.add_task("Complete project report", 2)
    task_manager.add_task("Send email to client", 1)
    task_manager.add_task("Prepare for meeting", 3)

    # Viewing tasks
    print("Tasks in the manager:")
    task_manager.view_tasks()

    # Completing tasks
    task_manager.complete_task()
    print("\nTasks after completing one task:")
    task_manager.view_tasks()

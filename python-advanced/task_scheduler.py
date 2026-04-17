
import heapq

class TaskScheduler:
    def __init__(self):
        # Priority queue (min-heap) to store tasks based on their priority
        self.task_queue = []
    
    def add_task(self, task, priority):
        '''
        Add a task to the scheduler with a given priority.
        Lower priority values indicate higher priority.
        '''
        heapq.heappush(self.task_queue, (priority, task))
        print(f"Task '{task}' added with priority {priority}.")
    
    def execute_task(self):
        '''
        Execute the highest priority task (the one with the lowest priority value).
        '''
        if not self.task_queue:
            print("No tasks to execute.")
            return
        
        priority, task = heapq.heappop(self.task_queue)
        print(f"Executing task '{task}' with priority {priority}.")
    
    def peek_next_task(self):
        '''
        Peek at the next task to be executed without removing it from the queue.
        '''
        if not self.task_queue:
            print("No tasks in the queue.")
            return
        
        priority, task = self.task_queue[0]
        print(f"Next task to execute: '{task}' with priority {priority}.")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1", priority=3)
scheduler.add_task("Task 2", priority=1)
scheduler.add_task("Task 3", priority=2)    

scheduler.peek_next_task()  # Should show Task 2 as it has the highest priority
scheduler.execute_task()    # Should execute Task 2
scheduler.execute_task()    # Should execute Task 3
scheduler.execute_task()    # Should execute Task 1
scheduler.execute_task()    # No tasks to execute


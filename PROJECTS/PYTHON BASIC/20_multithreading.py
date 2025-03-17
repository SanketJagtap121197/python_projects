import threading  # The threading module allows us to run multiple tasks concurrently (at the same time) using threads

# Defining a function for the thread
'''
This function prints numbers from 0 to 4.
It will be executed in a separate thread instead of the main program thread.
'''

def print_numbers():
    for i in range(5):
        print(i)

# Creating a thread
thread = threading.Thread(target=print_numbers) 
'''
This creates a new thread that will execute print_numbers().
target=print_numbers means the function print_numbers will run in this thread
'''

thread.start()
'''
This starts the thread and makes it run the print_numbers() function.
The main program does not wait for the thread to finish and may continue running other tasks
'''

thread.join()  # Waits for the thread to finish
'''
.join() makes the main program wait until the thread completes execution.
Without .join(), the main program could exit before the thread finishes.
'''

# a simple example using threads to show that order of execution is not guaranteed

import threading
import time

count = 0

def print_counter(thread_name, increment):
    global count
    i = 0
    while i < 10:
        i += 1
        count += increment
        print("%s: %s" % (thread_name, count))

# print_counter("Thread-1", 0.1)
# print_counter("Thread-2", 0.1)

# create two threads as follows
try:
    threading.Thread(target=print_counter, args=("Thread-1", 1)).start()
    threading.Thread(target=print_counter, args=("Thread-2", -1)).start()
except:
    print("Error: unable to start thread")

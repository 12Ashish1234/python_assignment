import threading
import time

# creating an event object
e = threading.Event()

# value of e.is_set() will be 'False' by default


# here after 3 seconds, the e.set() is called which sets the value of is_set() to 'True'.
def task():
    print("Game started")
    time.sleep(3)

    e.set()


# once e.set() is set to true, this method will be called by the another thread
def end():
    e.wait()

    if e.is_set():
        print("Game Over...")


t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()

import threading
import time

# creating an event object
e = threading.Event()


def light_switch():
    while True:
        print("Light is green")
        e.set()
        time.sleep(5)
        print("Light is red")
        e.clear()
        time.sleep(5)
        # e.set()


def traffic_message():
    e.wait()
    while e.is_set():
        print("You can go")
        time.sleep(1)
        e.wait()


t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()

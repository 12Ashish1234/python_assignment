from time import sleep
import threading
from queue import Queue


def producer(my_que):
    print("producer: running")
    # print("current thread:", threading.current_thread())
    n = int(input("Enter number of students: "))
    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    my_que.put(None)

    print("producer: end")


def consumer(my_que):
    print("consumer: running")
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f"Got {item}")
        # sleep(3)

    print("consumer: end")


my_que = Queue()
t1 = threading.Thread(target=producer, args=(my_que,))
# print(t1.daemon)
t2 = threading.Thread(target=consumer, args=(my_que,))

t1.start()
t2.start()

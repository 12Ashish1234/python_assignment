import threading

lock = threading.Lock()

geek = 0


def sumOne():
    global geek

    # lock.acquire()
    for _ in range(10000000):
        geek = geek + 1

    # lock.release()


def sumTwo():
    global geek

    # lock.acquire()
    for _ in range(10000000):
        geek = geek + 1

    # lock.release()


t1 = threading.Thread(target=sumOne)
t2 = threading.Thread(target=sumTwo)

t1.start()
t2.start()


print(geek)
print(geek)

t1.join()
t2.join()

print(geek)
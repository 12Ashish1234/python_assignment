from threading import Thread, current_thread, main_thread


def display():
    print("current thread: ", current_thread().ident)
    print("main thread: ", main_thread().ident)
    for i in range(6):
        print(i)


t1 = Thread(target=display)
print(f"Is alive: {t1.is_alive()}")

t1.start()
print(f"Is alive: {t1.is_alive()}")

t1.join()
print(f"Is alive: {t1.is_alive()}")

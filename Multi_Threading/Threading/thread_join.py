from threading import Thread
from time import sleep


def upload():
    print("Uploading starts...")
    sleep(3)
    print("Video uploaded.")


def notification():
    print("Sending notif to subscribers")


t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()

# main thread
for i in range(5):
    print("Hello!")

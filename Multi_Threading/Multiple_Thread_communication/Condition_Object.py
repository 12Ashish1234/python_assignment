import threading
import time

# in this code, after entering the data only the other threads gets triggered.

def write_data():
    con.acquire()
    with open("report.txt", "w") as file1:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        for day in days:
            temp = input(f"Enter the temperature for {day} in Celsius: ")
            file1.write(temp + "\n")
            time.sleep(1.5)
    con.notify_all()
    con.release()


def max_temp():
    con.acquire()
    # reading the report.txt file
    with open("report.txt", "r") as file1:
        # reading each line from the file and saving it as a list
        data = file1.readlines()
        # extracting the first element of the list, converting it to float from string
        max = float(data[0].strip("\n"))
        # looping from 2nd element to the last
        for temp in data[1:]:
            # finding max value
            temp = float(temp.strip("\n"))
            if temp > max:
                max = temp
        print(f"max temperature: {max}")
        con.release()


def avg_temp():
    con.acquire()
    with open("report.txt", "r") as file1:
        data = file1.readlines()
        sum = 0
        for temp in data:
            temp = float(temp.strip("\n"))
            sum += temp
        avg = sum / len(data)
        print(f"average temperature: {avg}")
        con.release()


# Condition object for thread communication
con = threading.Condition()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()

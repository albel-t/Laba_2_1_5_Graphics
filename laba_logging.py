import os
import time

LOG_FILE = 'loggs.txt' 

def InitLogFile():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        # fcntl.flock(f, fcntl.LOCK_EX)  # Блокировка файла
        f.write("=== Start logging ===\n")
    InitFile(__file__)
        # fcntl.flock(f, fcntl.LOCK_UN)  # Разблокировка


def InitFile(filename):
    with open(LOG_FILE, "a+", encoding="utf-8") as f:
        print("add - "+filename)
        f.write("-init|" + str(filename) + "\n") 
        time.sleep(0.1)
                
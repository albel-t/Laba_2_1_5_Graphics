import os

LOG_FILE = 'loggs.txt' 

def InitLogFile():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("=== Start logging ===\n\n")
        InitFile(__file__)

def InitFile(filename):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"-init {filename}") 
                
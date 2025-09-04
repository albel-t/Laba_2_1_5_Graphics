
from laba_logging import *

InitLogFile()
InitFile(__file__)
import task1.main
import task2.main

print("Введите номер задания:")
a = input()
if a == '1':
    task1.main.main()
if a == '2':
    task2.main.main()
else:
    print("ненадо это ломать")


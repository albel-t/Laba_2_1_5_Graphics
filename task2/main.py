import sys
import os
import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitLogFile()
InitFile(__file__)


import tkinter as tk
from graphic import MultiPlotApp

months = {"Янв": 31, 
    "Фев": 28 , 
    "Мар": 31 ,
    "Апр": 30 ,
    "Май": 31 ,
    "Июн": 30 ,
    "Июл": 31 ,
    "Авг": 31 ,
    "Сен": 30 ,
    "Окт": 31 ,
    "Ноя": 30 ,
    "Дек": 31 }

months_num = {"Янв": 1, 
    "Фев": 2 , 
    "Мар": 3 ,
    "Апр": 4 ,
    "Май": 5 ,
    "Июн": 6 ,
    "Июл": 7 ,
    "Авг": 8 ,
    "Сен": 9 ,
    "Окт": 10 ,
    "Ноя": 11 ,
    "Дек": 12 }



def main():
    root = tk.Tk()
    app = MultiPlotApp(root, "window", "D:\\projects\\VisualStudioCode\\Laba_2_1_5_Graphics\\task2\\task2_data.txt")
    app.categories_name = "дни"
    app.values_name = "коммиты"
    days_name = app.categories_list
    days_data = app.values_list

    app.categories_list_without_null =  copy.deepcopy(app.categories_list)
    app.values_list_without_null =  copy.deepcopy(app.values_list)

    for year in range(0, 3):
        for month in months:
            for day in range(1, months[month]+1):
                # print(f"year {year}, month {month}, day {day}")
                title = f'{month} {year+2020}'
                num_cell = months_num[month] + year*12
                if title not in days_name[num_cell][0]:
                    days_name.insert(num_cell, [])
                    days_data.insert(num_cell, [])

                if f'{day} {title}' not in days_name:
                    days_name[num_cell].insert(day, f'{day} {title}')
                    days_data[num_cell].insert(day, 0)


    # days_name = list(map(lambda x: list(x), app.categories_list))
    app.categories_list = days_name
    app.values_list = days_data
    root.mainloop()

if __name__ == "__main__":
    main()
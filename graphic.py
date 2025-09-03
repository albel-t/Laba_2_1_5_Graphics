
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitFile(__file__)

class MultiPlotApp:
    def __init__(self, root, name:str, data):
        self.root = root
        self.root.title(name)
        self.root.geometry("1200x800")
        
        self.categories_name = 'категории'
        self.values_name = 'значения'
        # Пример данных
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = [23, 45, 56, 78, 33]
        # self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A826', '#6C5CE7']
        
        self.create_widgets()
        self.create_plots()
        self.current_index = 1
        self.categories_list = [['q', 'w', 'e', 'e'], ['r', 't', 'y', 'u'], ['i', 'o', 'p', '[]'], ['a', 's', 'd', 'f'], ['g', 'h', 'j', 'k']]
        self.values_list = [[12, 32, 64, 15], [48, 63, 15, 36], [48, 95, 62, 51], [42, 51, 54, 36], [75, 35, 42, 63]]
        self.switch_data()


        #data изъятие
        with open(data, "r", encoding="utf-8") as f:
            read_data = f.read().split('-')
            print(read_data)
            self.categories_list.clear()
            self.values_list.clear()
            for i in range(1, len(read_data), 2):
                part_data_categories = []
                part_data_values = []
                print(read_data[i] + "   - " + read_data[i+1])

                for items in (read_data[i+1].split('\n')):
                    item = items.split(' ')
                    if(items == ''):
                        continue

                    print(item)
                    print(f'|{item[0]}|{item[1]}|')

                    part_data_categories.append(item[0] + " " + read_data[i])
                    part_data_values.append(int(item[1]))
                self.categories_list.append(part_data_categories)
                self.values_list.append(part_data_values)
                print("all ------------")
                print(part_data_categories)
                print(part_data_values)
        

    def set_categories(self, data):
        self.categories = data

    def set_values(self, data):
        self.values = data

    def create_widgets(self):
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=0, column=0, sticky="ew")
        
        plot_frame = ttk.Frame(self.root, padding="10")
        plot_frame.grid(row=1, column=0, sticky="nsew")
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        ttk.Label(control_frame, text="Тип графика:").grid(row=0, column=0, padx=5)
        
        self.plot_type = tk.StringVar(value="linear")
        plot_types = [
            ("Линейный график", "linear"),
            ("Точечный график", "scatter"),
            ("Столбчатая диаграмма", "bar"),
            ("Горизонтальная диаграмма", "barh"),
            ("Круговая диаграмма", "pie"),
            ("Гистограмма", "hist")
        ]
        
        for i, (text, value) in enumerate(plot_types):
            ttk.Radiobutton(control_frame, text=text, variable=self.plot_type, 
                           value=value, command=self.update_plot).grid(row=0, column=i+1, padx=5)
            
        # Кнопка обновления
        ttk.Button(control_frame, text="<-", command=self.switch_data_l).grid(row=0, column=len(plot_types)+1, padx=5)        
        # Кнопка обновления
        ttk.Button(control_frame, text="->", command=self.switch_data_r).grid(row=0, column=len(plot_types)+2, padx=5)

        self.figure = plt.Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def create_plots(self):
        self.update_plot()
    
    def switch_data_l(self):
        self.current_index = max(self.current_index - 1, 1)
        self.switch_data()

    def switch_data_r(self):
        self.current_index = min(self.current_index + 1, len(self.categories_list)-2)
        self.switch_data()

    def switch_data(self):
        self.set_categories(self.categories_list[self.current_index-1]+self.categories_list[self.current_index]+self.categories_list[self.current_index+1])
        self.set_values(self.values_list[self.current_index-1]+self.values_list[self.current_index]+self.values_list[self.current_index+1])
        self.update_plot()

    def update_plot(self):


        plot_type = self.plot_type.get()
        self.figure.clear()
        
        ax = self.figure.add_subplot(111)
        
        if plot_type == "linear":
            self.create_linear_plot(ax)
        elif plot_type == "scatter":
            self.create_scatter_plot(ax)
        elif plot_type == "bar":
            self.create_bar_plot(ax)
        elif plot_type == "barh":
            self.create_barh_plot(ax)
        elif plot_type == "pie":
            self.create_pie_plot(ax)
        elif plot_type == "hist":
            self.create_hist_plot(ax)
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def create_linear_plot(self, ax):
        x = np.arange(len(self.values))
        ax.plot(x, self.values, marker='o', linestyle='-', linewidth=2, markersize=8, color='blue')
        ax.set_title('Линейный график', fontsize=16, fontweight='bold')
        ax.set_xlabel(self.categories_name, fontsize=12)
        ax.set_ylabel(self.values_name, fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories)
    
    def create_scatter_plot(self, ax):
        x = np.arange(len(self.values))
        scatter = ax.scatter(x, self.values, s=100, c=self.values, cmap='viridis', alpha=0.7, edgecolors='black')
        ax.set_title('Точечный график', fontsize=16, fontweight='bold')
        ax.set_xlabel(self.categories_name, fontsize=12)
        ax.set_ylabel(self.values_name, fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories)
        
        plt.colorbar(scatter, ax=ax, label=self.values_name)
    
    def create_bar_plot(self, ax):
        bars = ax.bar(self.categories, self.values, alpha=0.7, edgecolor='black')
        ax.set_title('Столбчатая диаграмма', fontsize=16, fontweight='bold')
        ax.set_xlabel(self.categories_name, fontsize=12)
        ax.set_ylabel(self.values_name, fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')
        
        for bar, value in zip(bars, self.values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{value}', ha='center', va='bottom', fontweight='bold')
    
    def create_barh_plot(self, ax):
        bars = ax.barh(self.categories, self.values, alpha=0.7, edgecolor='black')
        ax.set_title('Горизонтальная диаграмма', fontsize=16, fontweight='bold')
        ax.set_xlabel(self.values_name, fontsize=12)
        ax.set_ylabel(self.categories_name, fontsize=12)
        ax.grid(True, alpha=0.3, axis='x')
        
        for bar, value in zip(bars, self.values):
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2.,
                   f'{value}', ha='left', va='center', fontweight='bold')
    
    def create_pie_plot(self, ax):
        wedges, texts, autotexts = ax.pie(
            self.values, 
            labels=self.categories, 
            autopct='%1.1f%%',
            startangle=90,
            shadow=True,
            explode=[0.05] * len(self.values)
        )
        
        ax.set_title('Круговая диаграмма', fontsize=16, fontweight='bold')
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
    
    def create_hist_plot(self, ax):
        ax.hist(self.values, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
        ax.set_title('Гистограмма распределения значений', fontsize=16, fontweight='bold')
        ax.set_xlabel(self.values_name, fontsize=12)
        ax.set_ylabel("количество", fontsize=12)
        ax.grid(True, alpha=0.3)

def main():
    root = tk.Tk()
    app = MultiPlotApp(root, "window", "D:\\projects\\VisualStudioCode\\Laba_2_1_5_Graphics\\task1\\task1_data.txt")
    root.mainloop()

if __name__ == "__main__":
    main()
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from laba_logging import *
InitLogFile()
InitFile(__file__)


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class MultiPlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мультиграфик - Все типы графиков")
        self.root.geometry("1200x800")
        
        # Пример данных
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = [23, 45, 56, 78, 33]
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9A826', '#6C5CE7']
        
        self.create_widgets()
        self.create_plots()
    
    def create_widgets(self):
        # Создаем фреймы
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=0, column=0, sticky="ew")
        
        plot_frame = ttk.Frame(self.root, padding="10")
        plot_frame.grid(row=1, column=0, sticky="nsew")
        
        # Настройка весов для растягивания
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Элементы управления
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
                
        # Фрейм для графика
        self.figure = plt.Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def create_plots(self):
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
        """Линейный график"""
        x = np.arange(len(self.values))
        ax.plot(x, self.values, marker='o', linestyle='-', linewidth=2, markersize=8, color='blue')
        ax.set_title('Линейный график', fontsize=16, fontweight='bold')
        ax.set_xlabel('Индекс', fontsize=12)
        ax.set_ylabel('Значение', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories)
    
    def create_scatter_plot(self, ax):
        """Точечный график"""
        x = np.arange(len(self.values))
        scatter = ax.scatter(x, self.values, s=100, c=self.values, cmap='viridis', alpha=0.7, edgecolors='black')
        ax.set_title('Точечный график', fontsize=16, fontweight='bold')
        ax.set_xlabel('Индекс', fontsize=12)
        ax.set_ylabel('Значение', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(x)
        ax.set_xticklabels(self.categories)
        
        # Добавляем цветовую шкалу
        plt.colorbar(scatter, ax=ax, label='Значение')
    
    def create_bar_plot(self, ax):
        """Вертикальная столбчатая диаграмма"""
        bars = ax.bar(self.categories, self.values, color=self.colors, alpha=0.7, edgecolor='black')
        ax.set_title('Столбчатая диаграмма', fontsize=16, fontweight='bold')
        ax.set_xlabel('Категории', fontsize=12)
        ax.set_ylabel('Значения', fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Добавляем значения на столбцы
        for bar, value in zip(bars, self.values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{value}', ha='center', va='bottom', fontweight='bold')
    
    def create_barh_plot(self, ax):
        """Горизонтальная столбчатая диаграмма"""
        bars = ax.barh(self.categories, self.values, color=self.colors, alpha=0.7, edgecolor='black')
        ax.set_title('Горизонтальная диаграмма', fontsize=16, fontweight='bold')
        ax.set_xlabel('Значения', fontsize=12)
        ax.set_ylabel('Категории', fontsize=12)
        ax.grid(True, alpha=0.3, axis='x')
        
        # Добавляем значения на столбцы
        for bar, value in zip(bars, self.values):
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2.,
                   f'{value}', ha='left', va='center', fontweight='bold')
    
    def create_pie_plot(self, ax):
        """Круговая диаграмма"""
        wedges, texts, autotexts = ax.pie(
            self.values, 
            labels=self.categories, 
            colors=self.colors,
            autopct='%1.1f%%',
            startangle=90,
            shadow=True,
            explode=[0.05] * len(self.values)  # Немного отделяем секторы
        )
        
        ax.set_title('Круговая диаграмма', fontsize=16, fontweight='bold')
        
        # Делаем проценты жирными
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
    
    def create_hist_plot(self, ax):
        """Гистограмма"""
        # Для гистограммы используем значения как данные
        ax.hist(self.values, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
        ax.set_title('Гистограмма распределения значений', fontsize=16, fontweight='bold')
        ax.set_xlabel('Значения', fontsize=12)
        ax.set_ylabel('Частота', fontsize=12)
        ax.grid(True, alpha=0.3)

def main():
    root = tk.Tk()
    app = MultiPlotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
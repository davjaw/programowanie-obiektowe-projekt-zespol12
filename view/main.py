import tkinter
from customtkinter import *

root = CTk()

root.title("Python project")
root.geometry("1000x1000")
root.configure(fg_color="#1b243a")
root.resizable(width=False, height=False)

pie1 = CTkCheckBox(root, text="% Ocen w przedziale gatunków")
pie2 = CTkCheckBox(root, text="% Ocen w przedziale lat")
pie3 = CTkCheckBox(root, text="% Gatunków w przedziale lat")
bar1 = CTkCheckBox(root, text="Średnia ocen na każdy gatunek")
bar2 = CTkCheckBox(root, text="Srednia ocen na każdy rok")
point1= CTkCheckBox(root, text="Ilość wszystkich opinii na kazdy rok")
point2 = CTkCheckBox(root, text="Rozkład procentowy gatunków na kazdy rok")

def piecharts():
    pie1.grid(row=2, column=0,padx=(120, 0), columnspan=2, sticky="w")
    pie2.grid(row=2, column=2,padx=(40, 0), columnspan=2, sticky="w")
    pie3.grid(row=2, column=4, columnspan=2, sticky="w")
    bar1.grid_remove()
    bar2.grid_remove()
    point1.grid_remove()
    point2.grid_remove()
def barcharts():
    bar1.grid(row=2, column=0, padx=(120, 0), columnspan=3,sticky="w")
    bar2.grid(row=2, column=3, padx=(100, 0), columnspan=3, sticky="w")
    pie1.grid_remove()
    pie2.grid_remove()
    pie3.grid_remove()
    point1.grid_remove()
    point2.grid_remove()

def pointcharts():
    point1.grid(row=2, column=0, padx=(120, 0), columnspan=3, sticky="w")
    point2.grid(row=2, column=3, padx=(100, 0),columnspan=3, sticky="w")
    pie1.grid_remove()
    pie2.grid_remove()
    pie3.grid_remove()
    bar1.grid_remove()
    bar2.grid_remove()

CTkLabel(root, text="imGraphs", text_color="#C0256F", font=("Kaushan Script", 64)).grid(row=0, column=2, columnspan=2, pady=(0, 50))
CTkButton(root, text="Kołowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=piecharts).grid(row=1, column=0,columnspan=2, padx=(225, 0), pady=(0,50))
CTkButton(root, text="Słupkowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=barcharts).grid(row=1, column=2,columnspan=2, pady=(0,50))
CTkButton(root, text="Punktowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=pointcharts).grid(row=1, column=4,columnspan=2, padx=(0, 225), pady=(0,50))
root.mainloop()
#! Multiple arguments
# def add(*args):
#     sum = 0
#     for number in args:
#         sum += number
#     return sum


# print(add(1, 2, 3, 4, 5))


#! Keyword argument
# def my_function(**kwargs):
#     # for key, value in kwargs.items():
#     #     print(f"{key}={value}")
#     print(kwargs.get("color", "Sorry, not defined"))


# my_function(name="Alice", age=25, city="New York")
# my_function(make="Nissan", model="GT-R", color="Blue", wheels=4, spoiler="Attached")

from tkinter import *

screen = Tk()
screen.minsize(width=400, height=300)
screen.config(padx=50, pady=50)

miles = 0


def calculateKM():
    miles = float(input.get())
    output = round(miles * 1.609)
    output_label["text"] = output


FONT = ("Calibri", 24, "normal")

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=1)
equal_to_label = Label(text="=", font=FONT)
equal_to_label.grid(row=0, column=2)
output_label = Label(text="0", font=FONT)
output_label.grid(row=0, column=3)
km_label = Label(text="Km", font=FONT)
km_label.grid(row=0, column=4)

input = Entry(width=5, font=FONT)
input.grid(row=0, column=0)


button = Button(text="Calculate", font=("Calibri", 18, "normal"), command=calculateKM)
button.grid(row=1, column=0)

screen.mainloop()

from tkinter import *

FONT = ("Calibri", 24, "normal")

window = Tk()

window.title("Password manager")
window.config(padx=50, pady=50)
logo_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0)
website_label.config(pady=30)
website_input = Entry(width=35, font=FONT)
website_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username", font=FONT)
username_label.grid(row=2, column=0)
username_label.config(pady=30)
username_input = Entry(width=35, font=FONT)
username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0)
password_label.config(pady=30)
password_input = Entry(width=25, font=FONT)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate", font=FONT)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, font=FONT)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

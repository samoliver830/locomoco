import test

food = input("What are you looking forward to eating?: ")
test.forecast(food)

# import tkinter as tk
# from tkinter import scrolledtext
# import sys
#
#
# def send_message():
#     user_input = input_entry.get()
#     test.forecast(user_input)
#     input_entry.delete(0, tk.END)
#
#
# root = tk.Tk()
# root.title("LocoMoco (please be patient... very slow)")
#
# comicsans = ("Comic Sans MS", 16)
#
# textbox = scrolledtext.ScrolledText(root, width=80, height=20, font=comicsans)
# textbox.pack()
#
# forward_text = tk.Label(text="What are you looking forward to eating?", font=comicsans)
# forward_text.pack()
#
# input_entry = tk.Entry(root, width=30, font=comicsans)
# input_entry.pack()
#
# send_button = tk.Button(root, text="Send", command=send_message, font=comicsans)
# send_button.pack()
#
#
# def print_to_textbox(text):
#     textbox.insert(tk.END, text)
#
#
# sys.stdout.write = print_to_textbox
#
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Welcome")
page = tk.Frame(root)
page.pack()

user_email = tk.StringVar()
user_password = tk.StringVar()
quit_game = tk.StringVar()

tk.Label(page).grid(row=0, column=0)

tk.Label(page, text="Email").grid(row=1, column=1, sticky=tk.W, pady=10)
tk.Entry(page, textvariable=user_email).grid(row=1, column=2)

tk.Label(page, text="Password").grid(row=2, column=1, sticky=tk.W, pady=20)
tk.Entry(page, textvariable=user_password).grid(row=2, column=2)


def login():
    email = user_email.get()
    pwd = user_password.get()

    print(email, pwd)


def register():
    email = user_email.get()
    pwd = user_password.get()

    print(email, pwd)


button_frame = tk.Frame(page)
button_frame.grid(row=3, column=1, columnspan=2)

register_btn = tk.Button(button_frame, text="Register", command=register)
register_btn.pack(side=tk.LEFT, padx=5)

login_btn = tk.Button(button_frame, text="Login", command=login)
login_btn.pack(side=tk.LEFT, padx=5)

quit_btn = tk.Button(button_frame, text="Quit", command=page.quit)
quit_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()

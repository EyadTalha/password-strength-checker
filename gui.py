import tkinter as tk
from tkinter import ttk
from checker import check_password_strength, generate_strong_password

def analyze_password(event=None):
    password = entry.get()
    result, tips = check_password_strength(password)
    result_label.config(text=f"Result: {result}")

    tips_text.delete(1.0, tk.END)
    for tip in tips:
        tips_text.insert(tk.END, f"- {tip}\n")

def toggle_password():
    entry.config(show="" if show_password_var.get() else "*")

def generate_password():
    new_password = generate_strong_password()
    entry.delete(0, tk.END)
    entry.insert(0, new_password)
    analyze_password()

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x400")
root.resizable(False, False)

theme = ttk.Style()
theme.theme_use('clam')
theme.configure("TLabel", background="#2e2e2e", foreground="white")
theme.configure("TButton", background="#444", foreground="white")
theme.configure("TCheckbutton", background="#2e2e2e", foreground="white")
root.configure(bg="#2e2e2e")

ttk.Label(root, text="Enter your password:").pack(pady=10)
entry = ttk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()
entry.bind("<KeyRelease>", analyze_password)

show_password_var = tk.BooleanVar()
ttk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password).pack(pady=5)

ttk.Button(root, text="Generate Strong Password", command=generate_password).pack(pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

ttk.Label(root, text="Tips:").pack()
tips_text = tk.Text(root, height=6, width=50, bg="#3a3a3a", fg="white")
tips_text.pack(pady=5)

root.mainloop()

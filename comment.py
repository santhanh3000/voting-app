import tkinter as tk

root = tk.Tk()
root.title("Grace Leah")
text1 = tk.Text(root, height=30, width=70)

text1.config(state="normal")
text1.insert(tk.INSERT,"Grace is a dedicated person\n")
text1.insert(tk.INSERT,"She works hard to move up the ladder")

text1.config(state="disabled")

text1.pack()

root.mainloop()

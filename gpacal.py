import tkinter as tk
import tkinter.messagebox


letter_to_decimal = {"A+": 4.3, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7,
                     "D+": 1.3, "D": 1.0, "F": 0.0}


def calgpa():
    gpa = 0
    grade_num = 0
    if e1.get() != "":
        gpa = gpa + letter_to_decimal[e1.get()]
        grade_num = grade_num + 1
    if e2.get() != "":
        gpa = gpa + letter_to_decimal[e2.get()]
        grade_num = grade_num + 1
    if e3.get() != "":
        gpa = gpa + letter_to_decimal[e3.get()]
        grade_num = grade_num + 1
    if e4.get() != "":
        gpa = gpa + letter_to_decimal[e4.get()]
        grade_num = grade_num + 1
    if e5.get() != "":
        gpa = gpa + letter_to_decimal[e5.get()]
        grade_num = grade_num + 1
    if e6.get() != "":
        gpa = gpa + letter_to_decimal[e6.get()]
        grade_num = grade_num + 1
    if e7.get() != "":
        gpa = gpa + letter_to_decimal[e7.get()]
        grade_num = grade_num + 1
    if e8.get() != "":
        gpa = gpa + letter_to_decimal[e8.get()]
        grade_num = grade_num + 1
    if e_cco.get() != "":
        gpa = gpa + letter_to_decimal[e_cco.get()]*0.2
        grade_num = grade_num + 0.2
    tk.messagebox.showinfo(title="GPA result", message="Your GPA is " + str(round(gpa/grade_num, 2)))


# TKINTER - General
window = tk.Tk()
window.title("GPA Calculator, by Diane Z.")
window.geometry("500x500")

# TKINTER - Content
l1 = tk.Label(window, bg='white', width=40, text='\nEnter ur letter Grades:', font=('Palatino', 22), wraplength=250)
l1.pack()

# TKINTER - File Name
e1 = tk.Entry(window, show=None, font=('Palatino', 15))
e1.pack()
e2 = tk.Entry(window, show=None, font=('Palatino', 15))
e2.pack()
e3 = tk.Entry(window, show=None, font=('Palatino', 15))
e3.pack()
e4 = tk.Entry(window, show=None, font=('Palatino', 15))
e4.pack()
e5 = tk.Entry(window, show=None, font=('Palatino', 15))
e5.pack()
e6 = tk.Entry(window, show=None, font=('Palatino', 15))
e6.pack()
e7 = tk.Entry(window, show=None, font=('Palatino', 15))
e7.pack()
e8 = tk.Entry(window, show=None, font=('Palatino', 15))
e8.pack()

l3 = tk.Label(window, bg='white', width=40, text='\n', font=('Palatino', 1), wraplength=250)
l3.pack()

l2 = tk.Label(window, bg='white', width=40, text='College Readiness Grade:', font=('Palatino', 18), wraplength=250)
l2.pack()

l4 = tk.Label(window, bg='white', width=40, text='\n', font=('Palatino', 1), wraplength=250)
l4.pack()

e_cco = tk.Entry(window, show=None, font=('Palatino', 15))
e_cco.pack()

l5 = tk.Label(window, bg='white', width=40, text='\n', font=('Palatino', 1), wraplength=250)
l5.pack()

# TKINTER - Button
button = tk.Button(window, text="Calculate GPA", command=calgpa, font=('Palatino', 20), height=2, width=15)
button.pack()

# TKINTER - Run
window.mainloop()

import tkinter as tk
import time

def CREATE():
    global LL
    ele = int(entry.get())
    LL.append(ele)
    entry.delete(0, tk.END)

def DISP():
    global LL
    if len(LL) == 0:
        display_label.config(text='Linked List is empty')
    else:
        display_label.config(text='Linked List:\n' + ' '.join(map(str, LL)))
        animate_linked_list()

def Insert_Begin():
    global LL
    num = int(entry.get())
    LL.insert(0, num)
    entry.delete(0, tk.END)

def Insert_Nth_Position():
    global LL
    ele = int(entry.get())
    pos = int(position_entry.get())
    if pos < 0:
        display_label.config(text='Invalid Position')
    else:
        LL.insert(pos - 1, ele)
    entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)

def Insert_End():
    global LL
    ele = int(entry.get())
    LL.append(ele)
    entry.delete(0, tk.END)

def Delete_Begin():
    global LL
    if not LL:
        display_label.config(text='Linked List is empty')
    else:
        LL.pop(0)

def Delete_Given():
    global LL
    num = int(entry.get())
    if num not in LL:
        display_label.config(text='Number not found')
    else:
        LL.remove(num)
    entry.delete(0, tk.END)

def Delete_Last():
    global LL
    if not LL:
        display_label.config(text='Linked List is empty')
    else:
        LL.pop()

def animate_linked_list():
    global LL
    canvas.delete("linked_list")
    y = 50
    for i, num in enumerate(LL):
        x = 20 + i * 50
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="#FF9800", tags="linked_list")
        canvas.create_text(x, y, text=str(num), font=('Helvetica', 10, 'bold'), fill='white', tags="linked_list")
        time.sleep(0.3)
        window.update()

LL = []

# Create the GUI window
window = tk.Tk()
window.title('Linked List')
window.geometry('600x500')
window.configure(bg='#f1f1f1')

# Heading label
heading_label = tk.Label(window, text='Linked List GUI', font=('Helvetica', 16, 'bold'), bg='#f1f1f1')
heading_label.pack(pady=10)

# Frame for entry and buttons
frame = tk.Frame(window, bg='#f1f1f1')
frame.pack(pady=10)

# Entry field
entry = tk.Entry(frame, font=('Helvetica', 12))
entry.pack(side=tk.LEFT, padx=5)

# Buttons
create_button = tk.Button(frame, text='Add an Element', command=CREATE, font=('Helvetica', 10), bg='#4CAF50', fg='white')
create_button.pack(side=tk.LEFT, padx=5)

display_button = tk.Button(frame, text='Display', command=DISP, font=('Helvetica', 10), bg='#2196F3', fg='white')
display_button.pack(side=tk.LEFT, padx=5)

# Canvas for linked list animation
canvas = tk.Canvas(window, width=560, height=200, bg='white')
canvas.pack(pady=10)

# Insertion frame
insert_frame = tk.Frame(window, bg='#f1f1f1')
insert_frame.pack(pady=10)

# Insertion entry field
position_entry = tk.Entry(insert_frame, font=('Helvetica', 12), width=5)
position_entry.pack(side=tk.LEFT, padx=5)

position_label = tk.Label(insert_frame, text='Position:', font=('Helvetica', 10), bg='#f1f1f1')
position_label.pack(side=tk.LEFT, padx=5)

# Insertion buttons
insert_begin_button = tk.Button(insert_frame, text='Insert at Beginning', command=Insert_Begin, font=('Helvetica', 10), bg='#FF9800', fg='white')
insert_begin_button.pack(side=tk.LEFT, padx=5)

insert_nth_button = tk.Button(insert_frame, text='Insert at nth Position', command=Insert_Nth_Position, font=('Helvetica', 10), bg='#FF5722', fg='white')
insert_nth_button.pack(side=tk.LEFT, padx=5)

insert_end_button = tk.Button(insert_frame, text='Insert at End', command=Insert_End, font=('Helvetica', 10), bg='#E91E63', fg='white')
insert_end_button.pack(side=tk.LEFT, padx=5)

# Deletion frame
delete_frame = tk.Frame(window, bg='#f1f1f1')
delete_frame.pack(pady=10)

# Deletion entry field
delete_label = tk.Label(delete_frame, text='Number:', font=('Helvetica', 10), bg='#f1f1f1')
delete_label.pack(side=tk.LEFT, padx=5)

delete_entry = tk.Entry(delete_frame, font=('Helvetica', 12), width=5)
delete_entry.pack(side=tk.LEFT, padx=5)

# Deletion buttons
delete_begin_button = tk.Button(delete_frame, text='Delete from Beginning', command=Delete_Begin, font=('Helvetica', 10), bg='#9C27B0', fg='white')
delete_begin_button.pack(side=tk.LEFT, padx=5)

delete_given_button = tk.Button(delete_frame, text='Delete Given Number', command=Delete_Given, font=('Helvetica', 10), bg='#673AB7', fg='white')
delete_given_button.pack(side=tk.LEFT, padx=5)

delete_last_button = tk.Button(delete_frame, text='Delete Last', command=Delete_Last, font=('Helvetica', 10), bg='#3F51B5', fg='white')
delete_last_button.pack(side=tk.LEFT, padx=5)

# Display label
display_label = tk.Label(window, text='', font=('Helvetica', 12), bg='#f1f1f1')
display_label.pack(pady=10)

window.mainloop()

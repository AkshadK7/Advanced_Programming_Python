"""
Name: Akshad Kolhatkar
Reg No: RA1911003010842

Q] Design a GUI using tkinter for Student Registration Form

"""

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Student Registration Form by AK')
#root.iconbitmap('1.ico')
root.geometry("400x600")

conn = sqlite3.connect('student_book.db')
c = conn.cursor()


'''
# For Creating a New MYSQL Database

c.execute("""CREATE TABLE addresses (
         first_name text,
         last_name text,
         regno text,
         city text,
         state text,
         zipcode integer
     )""")

'''

def submit():
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :regno, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'regno': regno.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              }
              )

    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    regno.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
regno = Entry(root, width=30)
regno.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, pady=5)

f_name_label = Label(root, text="First Name").grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name").grid(row=1, column=0)
regno_label = Label(root, text="Reg Number").grid(row=2, column=0)
city_label = Label(root, text="City").grid(row=3, column=0)
state_label = Label(root, text="State").grid(row=4, column=0)
zipcode_label = Label(root, text="Pincode").grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID Number")
delete_box_label.grid(row=10, column=0, pady=10)

submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=117)

def delete():
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    print_records = ""
    for record in records:
        print_records += str(record[6]) + "\t" + str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

conn.commit()
conn.close()

root.mainloop()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk


# In[2]:


import tkinter as tk

window = tk.Tk()


# In[8]:


import tkinter as tk
from tkinter import messagebox

# Login page
def login():
    username = user_entry.get() 
    password = pass_entry.get()
    
    # Check credentials
    if username == 'test' and password == 'pass':
        root.destroy()
        main_menu() 
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")  
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

root.mainloop()

# Main menu 
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    
    # Frames for layout
    top_frame = tk.Frame(root)
    top_frame.pack()
    
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side='bottom')
    
    # Widgets
    title = tk.Label(top_frame, text="Dutchess Bus Transportation", font=("Helvetica", 32))
    title.pack(pady=50)
    
    search_btn = tk.Button(bottom_frame, text="Search Schedules", command=search)
    search_btn.pack(side='left', padx=20)
    
    pay_btn = tk.Button(bottom_frame, text="Make Payment", command=make_payment)
    pay_btn.pack(side='left', padx=20)

    root.mainloop()
    
# Search page    
def search():
   # Search interface
  print("Before connection")
  # Connect to database
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shannu4321",
    database="dutchess_county_bus_transportation_dbms_project"
  )
  print("After connection")
  start = start_entry.get()
  end = end_entry.get()
  day = day_entry.get()

  cursor = db.cursor()

  # Query to join tables
  query = """SELECT b.BusNumber, s.ArrivalTime, s.DepartureTime, 
            rs.NumberofStops
            FROM Schedule s
            JOIN Bus_has_Schedule bs ON s.ScheduleID = bs.Schedule_ScheduleID
            JOIN Bus b ON bs.Bus_BusID = b.BusID
            JOIN Bus_has_BusRoute bbr ON b.BusID = bbr.Bus_BusID
            JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID
            JOIN RouteStopSequence rs ON r.RouteID = rs.BusRoute_RouteID
            WHERE r.StartLocation = %s AND r.EndLocation = %s AND s.DayFlag = %s"""

  cursor.execute(query, (start, end, day))

  results = cursor.fetchall()

  # Display results in UI
  for result in results:
     bus_number.config(text=result[0])
     arrival_time.config(text=result[1])
     departure_time.config(text=result[2])
     stops.config(text=result[3])
     
  # Close database connection
  db.close()
pass
   
# Payment page   
def make_payment():
  # Payment interface
  pass


# In[1]:


import mysql.connector


# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[5]:


get_ipython().run_line_magic('pip', 'install mysql-connector-python')


# In[15]:


import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

def login():
    username = user_entry.get()
    password = pass_entry.get()

    # Check credentials (replace with actual credentials validation)
    if username == 'test' and password == 'pass':
        root.destroy()
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def main_menu():
    root = tk.Tk()
    root.title("Main Menu")

    # Rest of your main menu UI code here
    top_frame = tk.Frame(root)
    top_frame.pack()

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side='bottom')

    title = tk.Label(top_frame, text="Dutchess Bus Transportation", font=("Helvetica", 32))
    title.pack(pady=50)

    search_btn = tk.Button(bottom_frame, text="Search Schedules", command=search)
    search_btn.pack(side='left', padx=20)

    pay_btn = tk.Button(bottom_frame, text="Make Payment", command=make_payment)
    pay_btn.pack(side='left', padx=20)
    root.mainloop()

def search():
    # Database connection
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Get user input
        start = user_entry.get()
        end = user_entry.get()
        day = user_entry.get()

        # Construct and execute the database query
        query = """SELECT b.BusNumber, s.ArrivalTime, s.DepartureTime, 
            rs.NumberofStops
            FROM Schedule s
            JOIN Bus_has_Schedule bs ON s.ScheduleID = bs.Schedule_ScheduleID
            JOIN Bus b ON bs.Bus_BusID = b.BusID
            JOIN Bus_has_BusRoute bbr ON b.BusID = bbr.Bus_BusID
            JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID
            JOIN RouteStopSequence rs ON r.RouteID = rs.BusRoute_RouteID
            WHERE r.StartLocation = %s AND r.EndLocation = %s AND s.DayFlag = %s"""

        cursor.execute(query, (start, end, day))

        results = cursor.fetchall()

        # Display results in UI (sample implementation)
        result_text = ""
        for result in results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label.config(text=result_text)

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")


def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[20]:


import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

def login():
    username = user_entry.get()
    password = pass_entry.get()

    # Check credentials (replace with actual credentials validation)
    if username == 'test' and password == 'pass':
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def main_menu():
    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_entry = tk.Entry(root)
    end_entry = tk.Entry(root)
    day_entry = tk.Entry(root)

    start_entry.pack()
    end_entry.pack()
    day_entry.pack()

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()

def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Construct and execute the database query
        query = """
        SELECT b.BusNumber, s.ArrivalTime, s.DepartureTime, rs.NumberofStops
        FROM Schedule s
        JOIN Bus_has_Schedule bs ON s.ScheduleID = bs.Schedule_ScheduleID
        JOIN Bus b ON bs.Bus_BusID = b.BusID
        JOIN Bus_has_BusRoute bbr ON b.BusID = bbr.Bus_BusID
        JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID
        JOIN RouteStopSequence rs ON r.RouteID = rs.BusRoute_RouteID
        WHERE r.StartLocation = %s AND r.EndLocation = %s AND s.DayFlag = %s
        """

        cursor.execute(query, (start, end, day))

        results = cursor.fetchall()

        # Display results in UI (sample implementation)
        result_text = ""
        for result in results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[22]:


import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

# Define Entry widgets for user input
start_entry = None
end_entry = None
day_entry = None

def login():
    username = user_entry.get()
    password = pass_entry.get()

    # Check credentials (replace with actual credentials validation)
    if username == 'test' and password == 'pass':
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def main_menu():
    global start_entry, end_entry, day_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_entry = tk.Entry(root)
    end_entry = tk.Entry(root)
    day_entry = tk.Entry(root)

    start_entry.pack()
    end_entry.pack()
    day_entry.pack()

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()

def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Display results in UI (sample implementation)
        result_text = ""
        for result in results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[24]:


import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

# Define Entry widgets for user input
start_entry = None
end_entry = None
day_entry = None
arrival_time_entry = None

def login():
    username = user_entry.get()
    password = pass_entry.get()

    # Check credentials (replace with actual credentials validation)
    if username == 'test' and password == 'pass':
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_entry = tk.Entry(root)
    end_entry = tk.Entry(root)
    day_entry = tk.Entry(root)
    arrival_time_entry = tk.Entry(root)

    start_entry.insert(0, "Start Location")
    end_entry.insert(0, "End Location")
    day_entry.insert(0, "Day")
    arrival_time_entry.insert(0, "Arrival Time")

    start_entry.pack()
    end_entry.pack()
    day_entry.pack()
    arrival_time_entry.pack()

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()

def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time = arrival_time_entry.get()

    # Database connection and search functionality
    try:
        # Convert the user input arrival time to a timedelta object
        arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

        # Database connection and search functionality
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on user input arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display results in UI with color (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text, bg="lightgreen")
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[1]:


import tkinter as tk
import mysql.connector
from tkinter import messagebox
from datetime import timedelta  # Import timedelta from datetime module

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

pass_label = tk.Label(root, text="Password:")
pass_label.pack()

pass_entry = tk.Entry(root, show='*')
pass_entry.pack()

# Define Entry widgets for user input
start_entry = None
end_entry = None
day_entry = None
arrival_time_entry = None  # Add a new entry for arrival time

def login():
    username = user_entry.get()
    password = pass_entry.get()

    # Check credentials (replace with actual credentials validation)
    if username == 'test' and password == 'pass':
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack()

def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_entry = tk.Entry(root)
    end_entry = tk.Entry(root)
    day_entry = tk.Entry(root)
    arrival_time_entry = tk.Entry(root)  # Create an entry for arrival time

    start_entry.pack()
    end_entry.pack()
    day_entry.pack()
    arrival_time_entry.pack()  # Pack the arrival time entry

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()


def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time_str = arrival_time_entry.get()

    # Convert the user input arrival time to a timedelta object
    arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display filtered results in UI (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[9]:


import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database config 
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

root = tk.Tk()
root.title("Login")

# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show='*')

login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

username_label.pack()
username_entry.pack()

password_label.pack()  
password_entry.pack()

login_btn.pack()
signup_btn.pack()
forgot_pass_btn.pack()

# Sign Up page
def signup():
  signup_window = tk.Toplevel(root)

  signup_username_label = tk.Label(signup_window, text="Username:")
  signup_username_entry = tk.Entry(signup_window)

  signup_password_label = tk.Label(signup_window, text="Password:")
  signup_password_entry = tk.Entry(signup_window, show='*')

  signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

  # Pack sign up widgets
  signup_username_label.pack()
  signup_username_entry.pack()
  
  signup_password_label.pack()
  signup_password_entry.pack()
  
  signup_btn.pack()

  # Get input values
  username = signup_username_entry.get()
  password = signup_password_entry.get()

  # Sign up submit logic
  insert_sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
  cursor.execute(insert_sql, (username, password))

  db.commit()

  messagebox.showinfo("Success", "Account created!")
  signup_window.destroy()
  
# Forgot Password page  
def forgot_password():
  forgot_window = tk.Toplevel(root)

  forgot_username_label = tk.Label(forgot_window, text="Username:")
  forgot_username_entry = tk.Entry(forgot_window)

  forgot_password_label = tk.Label(forgot_window, text="New Password:")
  forgot_password_entry = tk.Entry(forgot_window, show='*')

  forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

  forgot_username_label.pack()
  forgot_username_entry.pack()

  forgot_password_label.pack()
  forgot_password_entry.pack()

  forgot_btn.pack()

  # Get input values
  username = forgot_username_entry.get()
  new_password = forgot_password_entry.get()

  # Reset password logic
  update_sql = "UPDATE users SET password = %s WHERE username = %s"
  cursor.execute(update_sql, (new_password, username))

  db.commit()

  messagebox.showinfo("Success", "Password reset successfully!")
  forgot_window.destroy()

# Login
def login():
  username = username_entry.get()
  password = password_entry.get()

  # Login validation
  cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
  if cursor.fetchone() is None:
    messagebox.showerror("Error","Invalid credentials")
  else:
    messagebox.showinfo("Success","Login successful")
    # Open main menu
    
root.mainloop()


# In[10]:


import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database configuration
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# Root window
root = tk.Tk()
root.title("Login") 

# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")  
password_entry = tk.Entry(root, show='*')

login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

# Pack Login widgets
username_label.pack()
username_entry.pack()
 
password_label.pack()
password_entry.pack()

login_btn.pack()  
signup_btn.pack()
forgot_pass_btn.pack()

# Signup
def signup():
  signup_window = tk.Toplevel(root)

  signup_username_label = tk.Label(signup_window, text="Username:")
  signup_username_entry = tk.Entry(signup_window)

  signup_password_label = tk.Label(signup_window, text="Password:")
  signup_password_entry = tk.Entry(signup_window, show='*')

  signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

  # Pack sign up widgets
  signup_username_label.pack()
  signup_username_entry.pack()
  
  signup_password_label.pack()
  signup_password_entry.pack()
  
  signup_btn.pack()
    
  # Get username and password
  username = signup_username_entry.get()
  password = signup_password_entry.get()

  # Signup logic  
  insert_sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
  cursor.execute(insert_sql, (username, password))

  db.commit()

  messagebox.showinfo("Success", "Account created!")
  signup_window.destroy()    
def signup_submit():
  signup_btn = tk.Button(command=signup_submit)
# Forgot Password
def forgot_password():
    
  forgot_window = tk.Toplevel(root)

  forgot_username_label = tk.Label(forgot_window, text="Username:")
  forgot_username_entry = tk.Entry(forgot_window)

  forgot_password_label = tk.Label(forgot_window, text="New Password:")
  forgot_password_entry = tk.Entry(forgot_window, show='*')

  forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

  forgot_username_label.pack()
  forgot_username_entry.pack()

  forgot_password_label.pack()
  forgot_password_entry.pack()

  forgot_btn.pack()
  # Get username and new password
  username = forgot_username_entry.get()
  new_password = forgot_password_entry.get()

  # Reset password logic
  update_sql = "UPDATE user SET password = %s WHERE username = %s"
  cursor.execute(update_sql, (new_password, username))

  db.commit()

  messagebox.showinfo("Success", "Password reset successfully!")
  forgot_window.destroy()
def forgot_submit():
  forgot_btn = tk.Button(command=forgot_submit)
# Login
def login():

  # Get username and password
  username = username_entry.get()
  password = password_entry.get()

  # Login validation
  cursor.execute("SELECT * FROM v_user_info WHERE username=%s AND password=%s", (username, password))
  if cursor.fetchone() is None:
    messagebox.showerror("Error","Invalid credentials")
  else:
    messagebox.showinfo("Success","Login successful")
    # Open main menu
      
root.mainloop()


# In[14]:


import tkinter as tk
from tkinter import messagebox 
import mysql.connector

# Database config
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# Root window
root = tk.Tk()
root.title("Login")

# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show='*')

login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

# Pack widgets
username_label.pack()  
username_entry.pack()

password_label.pack()
password_entry.pack()

login_btn.pack()
signup_btn.pack() 
forgot_pass_btn.pack()

# Signup
# Signup
def signup():

  signup_window = tk.Toplevel(root)

  # Labels and entries for each field
  firstname_label = tk.Label(signup_window, text="First Name:")
  firstname_entry = tk.Entry(signup_window)

  lastname_label = tk.Label(signup_window, text="Last Name:")
  lastname_entry = tk.Entry(signup_window)

  email_label = tk.Label(signup_window, text="Email:")
  email_entry = tk.Entry(signup_window)

  username_label = tk.Label(signup_window, text="Username:")
  username_entry = tk.Entry(signup_window)

  password_label = tk.Label(signup_window, text="Password:")
  password_entry = tk.Entry(signup_window, show='*')

  signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

  # Pack the widgets
  firstname_label.pack()
  firstname_entry.pack()
  
  lastname_label.pack()
  lastname_entry.pack()

  # ...other labels and entries

  signup_btn.pack()

  # Get input values
  first_name = firstname_entry.get()
  last_name = lastname_entry.get()
  email = email_entry.get()

  username = username_entry.get()
  password = password_entry.get()

  # Insert with values for all columns  
  insert_sql = "INSERT INTO v_user_info (FirstName, LastName, Email, Username, Password) VALUES (%s, %s, %s, %s, %s)"
  values = (first_name, last_name, email, username, password)
  
  cursor.execute(insert_sql, values)

  # Rest of signup
  db.commit()
  
  messagebox.showinfo("Success", "Account created!")
# Forgot password 
def forgot_password():

  forgot_window = tk.Toplevel(root)
  
  forgot_username_label = tk.Label(forgot_window, text="Username:")
  forgot_username_entry = tk.Entry(forgot_window)

  forgot_password_label = tk.Label(forgot_window, text="New Password:")
  forgot_password_entry = tk.Entry(forgot_window, show='*')
  
  forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

  # Pack widgets
  forgot_username_label.pack()
  forgot_username_entry.pack()

  forgot_password_label.pack()
  forgot_password_entry.pack()

  forgot_btn.pack()

  # Get username and new password
  username = forgot_username_entry.get()
  new_password = forgot_password_entry.get()

  # Update password in v_user_info view
  update_sql = "UPDATE v_user_info SET password = %s WHERE username = %s"
  cursor.execute(update_sql, (new_password, username))

  db.commit()

  messagebox.showinfo("Success", "Password reset successfully!")
  forgot_window.destroy()
  
# Login 
def login():

  username = username_entry.get()
  password = password_entry.get()

  # Check credentials in v_user_info view
  cursor.execute("SELECT * FROM v_user_info WHERE username=%s AND password=%s", (username, password))

  if cursor.fetchone() is None: 
    messagebox.showerror("Error","Invalid credentials")
  else:
    messagebox.showinfo("Success","Login successful")
  
def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_entry = tk.Entry(root)
    end_entry = tk.Entry(root)
    day_entry = tk.Entry(root)
    arrival_time_entry = tk.Entry(root)  # Create an entry for arrival time

    start_entry.pack()
    end_entry.pack()
    day_entry.pack()
    arrival_time_entry.pack()  # Pack the arrival time entry

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()


def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time_str = arrival_time_entry.get()

    # Convert the user input arrival time to a timedelta object
    arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display filtered results in UI (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[33]:


import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import timedelta
from PIL import Image, ImageTk

# Database config
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Root window
root = tk.Tk()
root.title("Login")

# Database connection and cursor
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Load and display login image
image_path = "C:/Users/shanm/OneDrive/Desktop/DBMS/DBMS.jpg.png"
login_image = Image.open(image_path)
login_image_tk = ImageTk.PhotoImage(login_image)
image_label = ttk.Label(root, image=login_image_tk)
image_label.image = login_image_tk  # Keep a reference to the image
image_label.pack()


# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show='*')

login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

# Pack widgets
username_label.pack()  
username_entry.pack()

password_label.pack()
password_entry.pack()

login_btn.pack()
signup_btn.pack() 
forgot_pass_btn.pack()

# Login 
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check credentials in v_user_info view
    cursor.execute("SELECT * FROM v_user_info WHERE username=%s AND password=%s", (username, password))

    if cursor.fetchone() is None: 
        messagebox.showerror("Error","Invalid credentials")
    else:
        messagebox.showinfo("Success","Login successful")
        main_menu()

# Signup
def signup():
    signup_window = tk.Toplevel(root)

    # Labels and entries for each field
    firstname_label = tk.Label(signup_window, text="First Name:")
    firstname_entry = tk.Entry(signup_window)

    lastname_label = tk.Label(signup_window, text="Last Name:")
    lastname_entry = tk.Entry(signup_window)

    email_label = tk.Label(signup_window, text="Email:")
    email_entry = tk.Entry(signup_window)

    username_label = tk.Label(signup_window, text="Username:")
    username_entry = tk.Entry(signup_window)

    password_label = tk.Label(signup_window, text="Password:")
    password_entry = tk.Entry(signup_window, show='*')

    signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

    # Pack the widgets
    firstname_label.pack()
    firstname_entry.pack()
    
    lastname_label.pack()
    lastname_entry.pack()

    email_label.pack()
    email_entry.pack()

    username_label.pack()
    username_entry.pack()

    password_label.pack()
    password_entry.pack()

    signup_btn.pack()

# Signup submit
def signup_submit():
    first_name = firstname_entry.get()
    last_name = lastname_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Insert with values for all columns  
    insert_sql = "INSERT INTO v_user_info (FirstName, LastName, Email, Username, Password) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, username, password)
    
    cursor.execute(insert_sql, values)

    # Rest of signup
    db.commit()
    
    messagebox.showinfo("Success", "Account created!")

# Forgot password 
def forgot_password():
    forgot_window = tk.Toplevel(root)
    
    forgot_username_label = tk.Label(forgot_window, text="Username:")
    forgot_username_entry = tk.Entry(forgot_window)

    forgot_password_label = tk.Label(forgot_window, text="New Password:")
    forgot_password_entry = tk.Entry(forgot_window, show='*')
    
    forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

    # Pack widgets
    forgot_username_label.pack()
    forgot_username_entry.pack()

    forgot_password_label.pack()
    forgot_password_entry.pack()

    forgot_btn.pack()

# Forgot password submit
def forgot_submit():
    username = forgot_username_entry.get()
    new_password = forgot_password_entry.get()

    # Update password in v_user_info view
    update_sql = "UPDATE v_user_info SET password = %s WHERE username = %s"
    cursor.execute(update_sql, (new_password, username))

    db.commit()

    messagebox.showinfo("Success", "Password reset successfully!")
    forgot_window.destroy()

# Main menu
def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_label = tk.Label(root, text="Start Location:")
    start_entry = tk.Entry(root)

    end_label = tk.Label(root, text="End Location:")
    end_entry = tk.Entry(root)

    day_label = tk.Label(root, text="Day:")
    day_entry = tk.Entry(root)

    arrival_time_label = tk.Label(root, text="Arrival Time (HH:MM):")
    arrival_time_entry = tk.Entry(root)  # Create an entry for arrival time

    start_label.pack()
    start_entry.pack()

    end_label.pack()
    end_entry.pack()

    day_label.pack()
    day_entry.pack()

    arrival_time_label.pack()
    arrival_time_entry.pack()  # Pack the arrival time entry

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()


# Search
def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time_str = arrival_time_entry.get()

    # Convert the user input arrival time to a timedelta object
    arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display filtered results in UI (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

# Make payment
def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[26]:


from PIL import ImageTk


# In[27]:


pip install pillow


# In[14]:



import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import timedelta
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Make login_image_tk a global variable
login_image_tk = None

# Database config
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Root window
root = tk.Tk()
root.title("Login")

# Database connection and cursor
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Load and display login image
image_url = "https://ibb.co/QM5B7Dg"
image_data = requests.get(image_url).content

# Debug prints
print("Content Type:", requests.head(image_url).headers['Content-Type'])
print("Image Data:", image_data)

# Try saving the content to a file (debugging purposes)
with open("debug_image.jpg", "wb") as f:
    f.write(image_data)

try:
    login_image = Image.open(BytesIO(image_data))
    login_image_tk = ImageTk.PhotoImage(login_image)
    image_label = ttk.Label(root, image=login_image_tk)
    image_label.image = login_image_tk  # Keep a reference to the image
    image_label.pack()
except Exception as e:
    print("Error:", e)

# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show='*')

login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

# Pack widgets
username_label.pack()  
username_entry.pack()

password_label.pack()
password_entry.pack()

login_btn.pack()
signup_btn.pack() 
forgot_pass_btn.pack()

# Login 
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check credentials in v_user_info view
    cursor.execute("SELECT * FROM v_user_info WHERE username=%s AND password=%s", (username, password))

    if cursor.fetchone() is None: 
        messagebox.showerror("Error","Invalid credentials")
    else:
        messagebox.showinfo("Success","Login successful")
        main_menu()

# Signup
def signup():
    signup_window = tk.Toplevel(root)

    # Labels and entries for each field
    firstname_label = tk.Label(signup_window, text="First Name:")
    firstname_entry = tk.Entry(signup_window)

    lastname_label = tk.Label(signup_window, text="Last Name:")
    lastname_entry = tk.Entry(signup_window)

    email_label = tk.Label(signup_window, text="Email:")
    email_entry = tk.Entry(signup_window)

    username_label = tk.Label(signup_window, text="Username:")
    username_entry = tk.Entry(signup_window)

    password_label = tk.Label(signup_window, text="Password:")
    password_entry = tk.Entry(signup_window, show='*')

    signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

    # Pack the widgets
    firstname_label.pack()
    firstname_entry.pack()
    
    lastname_label.pack()
    lastname_entry.pack()

    email_label.pack()
    email_entry.pack()

    username_label.pack()
    username_entry.pack()

    password_label.pack()
    password_entry.pack()

    signup_btn.pack()

# Signup submit
def signup_submit():
    first_name = firstname_entry.get()
    last_name = lastname_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Insert with values for all columns  
    insert_sql = "INSERT INTO v_user_info (FirstName, LastName, Email, Username, Password) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, username, password)
    
    cursor.execute(insert_sql, values)

    # Rest of signup
    db.commit()
    
    messagebox.showinfo("Success", "Account created!")

# Forgot password 
def forgot_password():
    forgot_window = tk.Toplevel(root)
    
    forgot_username_label = tk.Label(forgot_window, text="Username:")
    forgot_username_entry = tk.Entry(forgot_window)

    forgot_password_label = tk.Label(forgot_window, text="New Password:")
    forgot_password_entry = tk.Entry(forgot_window, show='*')
    
    forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

    # Pack widgets
    forgot_username_label.pack()
    forgot_username_entry.pack()

    forgot_password_label.pack()
    forgot_password_entry.pack()

    forgot_btn.pack()

# Forgot password submit
def forgot_submit():
    username = forgot_username_entry.get()
    new_password = forgot_password_entry.get()

    # Update password in v_user_info view
    update_sql = "UPDATE v_user_info SET password = %s WHERE username = %s"
    cursor.execute(update_sql, (new_password, username))

    db.commit()

    messagebox.showinfo("Success", "Password reset successfully!")
    forgot_window.destroy()

# Main menu
def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_label = tk.Label(root, text="Start Location:")
    start_entry = tk.Entry(root)

    end_label = tk.Label(root, text="End Location:")
    end_entry = tk.Entry(root)

    day_label = tk.Label(root, text="Day:")
    day_entry = tk.Entry(root)

    arrival_time_label = tk.Label(root, text="Arrival Time (HH:MM):")
    arrival_time_entry = tk.Entry(root)  # Create an entry for arrival time

    start_label.pack()
    start_entry.pack()

    end_label.pack()
    end_entry.pack()

    day_label.pack()
    day_entry.pack()

    arrival_time_label.pack()
    arrival_time_entry.pack()  # Pack the arrival time entry

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()


# Search
def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time_str = arrival_time_entry.get()

    # Convert the user input arrival time to a timedelta object
    arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

    # Database connection and search functionality
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display filtered results in UI (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

        # Close the database connection
        db.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

# Make payment
def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[21]:


import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import timedelta
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Make login_image_tk a global variable
login_image_tk = None

# Database config
config = {
    "host": "localhost",
    "user": "root",
    "password": "shannu4321",
    "database": "dutchess_county_bus_transportation_dbms_project"
}

# Root window
root = tk.Tk()
root.title("Login")

# Database connection and cursor
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Load and display login image
image_url = "http://localhost:8888/view/Untitled%20Folder/download.jpeg"
image_data = requests.get(image_url).content

try:
    login_image = Image.open(BytesIO(image_data))
    login_image_tk = ImageTk.PhotoImage(login_image)
    image_label = ttk.Label(root, image=login_image_tk)
    image_label.image = login_image_tk  # Keep a reference to the image
    image_label.pack()
except Exception as e:
    print("Error:", e)

# Login page
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show='*')

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check credentials in v_user_info view
    cursor.execute("SELECT * FROM v_user_info WHERE username=%s AND password=%s", (username, password))

    if cursor.fetchone() is None: 
        messagebox.showerror("Error","Invalid credentials")
    else:
        messagebox.showinfo("Success","Login successful")
        main_menu()
        
# Forgot password 
# Make entry variables global
forgot_username_entry = None
forgot_password_entry = None
forgot_window = None
# ...

# Forgot password 
def forgot_password():
    global forgot_username_entry, forgot_password_entry
    forgot_window = tk.Toplevel(root)
    
    forgot_username_label = tk.Label(forgot_window, text="Username:")
    forgot_username_entry = tk.Entry(forgot_window)

    forgot_password_label = tk.Label(forgot_window, text="New Password:")
    forgot_password_entry = tk.Entry(forgot_window, show='*')
    
    forgot_btn = tk.Button(forgot_window, text="Reset Password", command=forgot_submit)

    # Pack widgets
    forgot_username_label.pack()
    forgot_username_entry.pack()

    forgot_password_label.pack()
    forgot_password_entry.pack()

    forgot_btn.pack()

# Forgot password submit
def forgot_submit():
    global forgot_username_entry, forgot_password_entry, forgot_window
    username = forgot_username_entry.get()
    new_password = forgot_password_entry.get()

    # Update password in v_user_info view
    update_sql = "UPDATE v_user_info SET password = %s WHERE username = %s"
    cursor.execute(update_sql, (new_password, username))

    db.commit()

    messagebox.showinfo("Success", "Password reset successfully!")

    # Check if forgot_window exists before destroying
    if forgot_window:
        forgot_window.destroy()


# Make entry variables global
firstname_entry = None
lastname_entry = None
DOB_entry = None
email_entry = None
username_entry2 = None
password_entry2 = None


# Signup
def signup():
    global firstname_entry, lastname_entry, email_entry, username_entry2, password_entry2
    signup_window = tk.Toplevel(root)

    # Labels and entries for each field
    firstname_label = tk.Label(signup_window, text="First Name:")
    firstname_entry = tk.Entry(signup_window)

    lastname_label = tk.Label(signup_window, text="Last Name:")
    lastname_entry = tk.Entry(signup_window)
    
    DOB_label = tk.Label(signup_window, text="Date_of_Birth(MM/DD/YYY):")
    DOB_entry = tk.Entry(signup_window)

    email_label = tk.Label(signup_window, text="Email:")
    email_entry = tk.Entry(signup_window)

    username_label = tk.Label(signup_window, text="Username:")
    username_entry2 = tk.Entry(signup_window)

    password_label = tk.Label(signup_window, text="Password:")
    password_entry2 = tk.Entry(signup_window, show='*')

    signup_btn = tk.Button(signup_window, text="Sign Up", command=signup_submit)

    # Pack the widgets
    firstname_label.pack()
    firstname_entry.pack()

    lastname_label.pack()
    lastname_entry.pack()
    
    DOB_label.pack()
    DOB_entry.pack()

    email_label.pack()
    email_entry.pack()

    username_label.pack()
    username_entry2.pack()

    password_label.pack()
    password_entry2.pack()

    signup_btn.pack()

# Signup submit
def signup_submit():
    global firstname_entry, lastname_entry, email_entry, username_entry, password_entry
    first_name = firstname_entry.get()
    last_name = lastname_entry.get()
    DOB = DOB_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Insert with values for all columns  
    insert_sql = "INSERT INTO User (FirstName, LastName, DOB, Email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, DOB, email, username, password)
    
    cursor.execute(insert_sql, values)

    # Rest of signup
    db.commit()
    
    messagebox.showinfo("Success", "Account created!")

    
login_btn = tk.Button(root, text="Login", command=login)
signup_btn = tk.Button(root, text="Sign Up", command=signup)
forgot_pass_btn = tk.Button(root, text="Forgot Password?", command=forgot_password)

# Pack widgets

username_label.pack()  
username_entry.pack()

password_label.pack()
password_entry.pack()

login_btn.pack()
signup_btn.pack() 
forgot_pass_btn.pack()


# Main menu
def main_menu():
    global start_entry, end_entry, day_entry, arrival_time_entry  # Declare as global variables

    # Clear the login window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Menu")

    # Create Entry widgets for user input
    start_label = tk.Label(root, text="Start Location:")
    start_entry = tk.Entry(root)

    end_label = tk.Label(root, text="End Location:")
    end_entry = tk.Entry(root)

    day_label = tk.Label(root, text="Day:")
    day_entry = tk.Entry(root)

    arrival_time_label = tk.Label(root, text="Arrival Time (HH:MM):")
    arrival_time_entry = tk.Entry(root)  # Create an entry for arrival time

    start_label.pack()
    start_entry.pack()

    end_label.pack()
    end_entry.pack()

    day_label.pack()
    day_entry.pack()

    arrival_time_label.pack()
    arrival_time_entry.pack()  # Pack the arrival time entry

    search_btn = tk.Button(root, text="Search Schedules", command=search)
    search_btn.pack()

    pay_btn = tk.Button(root, text="Make Payment", command=make_payment)
    pay_btn.pack()


# Search
def search():
    # Get user input
    start = start_entry.get()
    end = end_entry.get()
    day = day_entry.get()
    arrival_time_str = arrival_time_entry.get()

    # Convert the user input arrival time to a timedelta object
    arrival_time = timedelta(hours=int(arrival_time_str.split(':')[0]), minutes=int(arrival_time_str.split(':')[1]))

    # Database connection and search functionality
    try:
        # Construct and execute the database query
        cursor.execute("SELECT * FROM BusScheduleView")
        results = cursor.fetchall()

        # Filter results based on arrival time
        filtered_results = [result for result in results if result[1] >= arrival_time]

        # Display filtered results in UI (sample implementation)
        result_text = ""
        for result in filtered_results:
            result_text += f"Bus Number: {result[0]}\n"
            result_text += f"Arrival Time: {result[1]}\n"
            result_text += f"Departure Time: {result[2]}\n"
            result_text += f"Number of Stops: {result[3]}\n"
            result_text += "---------------------------\n"

        result_label = tk.Label(root, text=result_text)
        result_label.pack()

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

# Make payment
def make_payment():
    # Payment page functionality
    pass

root.mainloop()


# In[ ]:





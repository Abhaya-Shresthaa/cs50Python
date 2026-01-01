import tkinter as tk
from gameLogic import generate_question

points = 0
correct_answer = 0
time_left = 10
user_name = ""

root = tk.Tk()
root.title("Math Quiz")



def load_question():
    global correct_answer, time_left
    expr, correct_answer = generate_question()
    question_label.config(text=f"Solve: {expr}")
    time_left = 10
    update_timer()

def submit():
    global points
    try:
        user_ans = int(entry.get())
        if user_ans == correct_answer:
            points += 1
            points_label.config(text=f"Points: {points}")
        else:
            question_label.config(text="Wrong answer")
    except ValueError:
        question_label.config(text="Enter a number")

    entry.delete(0, tk.END)
    load_question()

def update_timer():
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        question_label.config(text="Time's up!")
        load_question()

def user_name():
    global user_name
    user_label.config(text = f"Enter Your Name: ")
    user_name = user_entry.get()
    
    
# --- NAME SCREEN ---
user_label = tk.Label(root, text="Enter Your Name:", font=("Arial", 20))
user_entry = tk.Entry(root, font=("Arial", 20))
start_btn = tk.Button(root, text="Start Quiz")

# --- QUIZ SCREEN ---
timer_label = tk.Label(root, font=("Arial", 20))
question_label = tk.Label(root, font=("Arial", 22))
entry = tk.Entry(root, font=("Arial", 20))
submit_btn = tk.Button(root, text="Submit", command=submit)
points_label = tk.Label(root, text="Points: 0", font=("Arial", 18))
    
# user_label = tk.Label(root, font=("Arial", 18))
# user_label.pack()
# user_entry = tk.Entry(root, font=("Arial", 20))
# user_entry.pack()
# submit_btn = tk.Button(root, text="Start QUIZ", command=submit)
# submit_btn.pack(pady=20)
# user_name()

# timer_label = tk.Label(root, font=("Arial", 20))
# timer_label.pack(pady=10)

# question_label = tk.Label(root, font=("Arial", 22))
# question_label.pack(pady=20)

# entry = tk.Entry(root, font=("Arial", 20))
# entry.pack()

# submit_btn = tk.Button(root, text="Submit", command=submit)
# submit_btn.pack(pady=20)

# points_label = tk.Label(root, text="Points: 0", font=("Arial", 18))
# points_label.pack()

user_label.pack(pady=10)
user_entry.pack(pady=10)
start_btn.pack(pady=20)

def start_quiz():
    global user_name
    user_name = user_entry.get().strip()

    if not user_name:
        user_label.config(text="Please enter your name!")
        return

    # Remove name screen
    user_label.pack_forget()
    user_entry.pack_forget()
    start_btn.pack_forget()

    # Show quiz screen
    timer_label.pack(pady=10)
    question_label.pack(pady=20)
    entry.pack()
    submit_btn.pack(pady=20)
    points_label.pack()

    load_question()

start_btn.config(command=start_quiz)

load_question()
root.mainloop()
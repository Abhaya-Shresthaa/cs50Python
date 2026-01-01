import tkinter as tk
# Assuming gameLogic.py has: def generate_question(): return "2 + 2", 4
try:
    from gameLogic import generate_question
except ImportError:
    # Fallback for demonstration if gameLogic is missing
    import random
    def generate_question():
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b}", a + b

# --- Global Variables ---
points = 0
correct_answer = 0
time_left = 10
user_name_val = ""
timer_id = None


root = tk.Tk()
root.title("Math Quiz")
root.geometry("400x400")

# --- Logic Functions ---

def clear_screen():
    """Removes all widgets from the screen."""
    for widget in root.winfo_children():
        widget.pack_forget()

def start_quiz():
    global user_name_val, points
    user_name_val = user_entry.get().strip()
    
    if not user_name_val:
        user_label.config(text="Please enter your name!", fg="red")
        return

    points = 0 # Reset points for new game
    show_quiz_screen()
    load_question()

def level_select():
    global points
    level =1
    if points < 2:
        level = 1
    elif points < 6:
        level = 2
    elif points < 14:
        level = 3
    elif points < 26:
        level = 4
    else:
        ## game ends "YOU WON"
        pass
    return level
    
 
def load_question():
    global correct_answer, time_left, timer_id, points

    if timer_id is not None:
        root.after_cancel(timer_id)

    
    # expr, correct_answer = generate_question(level_select())
    expr, correct_answer = generate_question(level_select())
    
    question_label.config(text=f"Solve: {expr}", fg="white")
    entry.delete(0, tk.END)
    leveled_time_left()
    update_timer()
    
def leveled_time_left():
    global time_left
    level = level_select()
    if level == 1:
        time_left = 10
    elif level == 2:
        time_left = 12
    elif level == 3:
        time_left = 15
    else:
        time_left = 20
    
def points_update():
    global points
    if points < 2:
        points += 1
    elif points < 6:
        points += 2
    elif points < 14:
        points += 4
    elif points < 26:
        points += 6
    else: 
        end_game("You won")
        

        
def submit(event=None): # Added event=None to allow 'Enter' key support
    global points, timer_id

    try:
        user_ans = int(entry.get())
        if user_ans == correct_answer:
            points_update()
            points_label.config(text=f"Points: {points}")
            level_label.config(text=f"Level: {level_select()}")
            load_question()
        else:
            end_game("Wrong Answer!")
    except ValueError:
        question_label.config(text="Enter a valid number", fg="red")

def update_timer():
    global time_left, timer_id

    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        timer_id = root.after(1000, update_timer)
    else:
        end_game("Time's Up!")

def end_game(reason):
    """Stops timer and shows the Game Over screen."""
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
    
    show_game_over_screen(reason)

# --- Screen UI Builders ---

def show_start_screen():
    clear_screen()
    user_label.config(text="Enter Your Name:", fg="grey")
    user_label.pack(pady=20)
    user_entry.pack(pady=10)
    user_entry.delete(0, tk.END)
    start_btn.pack(pady=20)

def show_quiz_screen():
    clear_screen()
    timer_label.pack(pady=10)
    question_label.pack(pady=20)
    entry.pack(pady=10)            
    entry.focus_set() # Puts cursor in box automatically
    submit_btn.pack(pady=10)
    points_label.config(text=f"Points: {points}")
    points_label.pack(pady=10)
    level_label.config(text=f"Level: {level_select()}")
    level_label.pack(pady=10)
    
def restart_game():
    global points
    points = 0
    show_quiz_screen()
    load_question()

def show_game_over_screen(reason):
    clear_screen()
    
    # Show Reason (Wrong Ans / Time Up)
    reason_label = tk.Label(root, text=reason, font=("Arial", 24, "bold"), fg="red")
    reason_label.pack(pady=20)
    
    # Show Score
    score_label = tk.Label(root, text=f"{user_name_val}, your score: {points}", font=("Arial", 18))
    score_label.pack(pady=10)
    
    # Navigation Buttons
    restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 14), 
                           command=restart_game, bg="lightblue")
    restart_btn.pack(pady=10)
    
    exit_btn = tk.Button(root, text="Exit", font=("Arial", 14), 
                         command=root.quit, bg="pink")
    exit_btn.pack(pady=10)

# --- Initialize Widget Objects (but don't pack them yet) ---

user_label = tk.Label(root, font=("Arial", 20))
user_entry = tk.Entry(root, font=("Arial", 20))
start_btn = tk.Button(root, text="Start Quiz", font=("Arial", 18), command=start_quiz)

timer_label = tk.Label(root, font=("Arial", 20))
question_label = tk.Label(root, font=("Arial", 22))
entry = tk.Entry(root, font=("Arial", 20))
entry.bind('<Return>', submit) # Pressing Enter key submits
submit_btn = tk.Button(root, text="Submit", font=("Arial", 18), command=submit)
points_label = tk.Label(root, font=("Arial", 18))
level_label = tk.Label(root, font=("Arial", 18))

# Start the app
show_start_screen()
root.mainloop()
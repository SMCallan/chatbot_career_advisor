from openai import OpenAI
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="sk-proj-VwWGuDVfRYI2LCGdcA1ST3BlbkFJk4nvGkyl8qFeZWAkQowl")

# Function to generate career advice
def generate_career_advice(user_input):
    """This function uses the OpenAI API to generate career advice based on the user's input."""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a career advisor, skilled in identifying the ideal job for your clients. Here is a client seeking your expertise. In the response field, provide a role recommendation for the client based on the input. Format the response with the job title, a brief 1-2 line sentence describing the role, and 3 bullet points of tips to get into the role. At the end say goodbye to the user."},
            {"role": "user", "content": user_input},
        ]
    )
    return completion.choices[0].message.content

def send_message():
    if len(questions) > 0:
        question = questions.pop(0)
        conversation.configure(state=tk.NORMAL)
        conversation.insert(tk.END, "Career Advisor: " + question + "\n", "bot")
        conversation.configure(state=tk.DISABLED)
        conversation.see(tk.END)
        user_input = user_entry.get()
        user_entry.delete(0, tk.END)
        user_inputs.append(user_input)

        if len(questions) == 0:
            user_input = f"The user's name is {user_name.get()}\n" + "\n".join(f"Q: {q}\nA: {a}" for q, a in zip(user_questions, user_inputs))
            career_advice = generate_career_advice(user_input)
            conversation.configure(state=tk.NORMAL)
            conversation.insert(tk.END, "Career Advice:\n" + career_advice + "\n", "advice")
            conversation.configure(state=tk.DISABLED)
            conversation.see(tk.END)
            send_button.config(state=tk.DISABLED)
    else:
        user_input = user_entry.get()
        user_entry.delete(0, tk.END)
        conversation.configure(state=tk.NORMAL)
        conversation.insert(tk.END, "Career Advisor: I'm sorry, but I am not programmed to handle general conversation. My purpose is to provide career advice based on your responses to specific questions. If you would like to start the career advisory process, please click the 'Start Career Advice' button.\n", "bot")
        conversation.configure(state=tk.DISABLED)
        conversation.see(tk.END)

def start_career_advice():
    global questions, user_questions, user_inputs
    questions = [
        "What is your educational background?",
        "What are your skills and strengths?",
        "What industries or fields are you interested in?",
        "What type of work environment do you prefer?",
        "What are your long-term career goals?",
    ]
    user_questions = questions.copy()
    user_inputs = []
    send_button.config(state=tk.NORMAL)
    conversation.configure(state=tk.NORMAL)
    conversation.insert(tk.END, "Career Advisor: Hello! What is your name?\n", "bot")
    conversation.configure(state=tk.DISABLED)
    conversation.see(tk.END)

# Create the main window
window = tk.Tk()
window.title("Career Advisor")
window.configure(bg="white")

# Load and display the logo
logo = Image.open("logo.png")
logo = logo.resize((300, 300), resample=Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo)
logo_label = ttk.Label(window, image=logo_photo, background="white")
logo_label.pack(pady=10)

# Create conversation history text area
conversation = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=59, height=15, font=("Arial", 12))
conversation.pack(pady=10)
conversation.tag_config("bot", foreground="black" )
conversation.tag_config("advice", foreground="black")
conversation.configure(state=tk.DISABLED)

# Create user input entry and send button
input_frame = ttk.Frame(window)
input_frame.pack(fill=tk.X, padx=10, pady=5)

user_name = tk.StringVar()
user_entry = ttk.Entry(input_frame, textvariable=user_name, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

start_button = ttk.Button(window, text="Start Career Advice", command=start_career_advice)
start_button.pack(pady=10)

# Start the main event loop
window.mainloop()
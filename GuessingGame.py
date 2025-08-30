import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("450x300")
        self.master.configure(bg="#f0f4f7")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(master, text="Guess the Number!", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
        self.title_label.pack(pady=15)

        self.instruction_label = tk.Label(master, text="I'm thinking of a number between 1 and 100.", font=("Helvetica", 12), bg="#f0f4f7")
        self.instruction_label.pack(pady=5)

        self.entry = tk.Entry(master, font=("Helvetica", 14), justify='center')
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=15)
        self.submit_button.pack(pady=5)

        self.feedback = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f4f7", fg="#555")
        self.feedback.pack(pady=10)

        self.reset_button = tk.Button(master, text="🔄 Restart Game", command=self.reset_game, font=("Helvetica", 10), bg="#2196F3", fg="white")
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.feedback.config(text="📉 Too low! Try again.")
            elif guess > self.number_to_guess:
                self.feedback.config(text="📈 Too high! Try again.")
            else:
                messagebox.showinfo("🎉 Correct!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback.config(text="⚠️ Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

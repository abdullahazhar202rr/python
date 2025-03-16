import random
import tkinter as tk
from tkinter import messagebox

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("400x300")

        self.random_no = random.randint(1, 100)
        self.guesses = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.submit_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.highscore_label = tk.Label(root, text=f"High Score: {self.get_high_score()}", font=("Arial", 12))
        self.highscore_label.pack(pady=10)

    def get_high_score(self):
        try:
            with open("highscore.txt", "r") as h:
                return int(h.read())
        except FileNotFoundError:
            return float('inf')  # Return a very high value if the file doesn't exist

    def save_high_score(self, score):
        with open("highscore.txt", "w") as g:
            g.write(str(score))

    def submit_guess(self):
        user_guess = self.entry.get()
        if not user_guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        user_guess = int(user_guess)
        self.guesses += 1

        if user_guess == self.random_no:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.guesses} attempts.")
            high_score = self.get_high_score()
            if self.guesses < high_score:
                self.save_high_score(self.guesses)
                self.highscore_label.config(text=f"High Score: {self.guesses} (New High Score!)")
            self.reset_game()
        elif user_guess > self.random_no:
            messagebox.showinfo("Too High", "Enter a lower number please.")
        elif user_guess < self.random_no:
            messagebox.showinfo("Too Low", "Enter a higher number please.")

        self.entry.delete(0, tk.END)  # Clear the entry box

    def reset_game(self):
        self.random_no = random.randint(1, 100)
        self.guesses = 0

def main():
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

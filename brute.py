import random as rdm
import customtkinter as ctk

# Load BIP-39 word list (should be in the same directory as `bip39_words.txt` or embedded directly into the script)
with open('bip39_words.txt', 'r') as f:
    WORD_LIST = f.read().splitlines()

# Initialize CustomTkinter
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

# Main Functionality
def generate_seed_phrase(word_count):
    """Generate a random seed phrase of given word count."""
    return " ".join(rdm.choices(WORD_LIST, k=word_count))

def generate_phrase():
    """Callback function to generate and display the seed phrase."""
    word_count = 12 if seedLength.get() == "12 Words" else 24
    phrase = generate_seed_phrase(word_count)
    outputLabel.configure(text=phrase)

# GUI Setup
root = ctk.CTk()
root.geometry("600x400")
root.title("Seed Phrase Guesser")

# Frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title
titleLabel = ctk.CTkLabel(master=frame, text="Seed Phrase Guesser", font=("Tahoma", 24))
titleLabel.pack(pady=10)

# Dropdown to Select Seed Length
seedLength = ctk.StringVar(value="12 Words")
dropdown = ctk.CTkOptionMenu(master=frame, variable=seedLength, values=["12 Words", "24 Words"])
dropdown.pack(pady=20)

# Generate Button
generateButton = ctk.CTkButton(master=frame, text="Generate Seed Phrase", command=generate_phrase)
generateButton.pack(pady=20)

# Output Label
outputLabel = ctk.CTkLabel(master=frame, text="", font=("Tahoma", 16), wraplength=500, anchor="center")
outputLabel.pack(pady=20)

# Run the GUI
root.mainloop()

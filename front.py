import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load the click sound
click_sound_path = r"C:\Users\ANANDA KRISHNAN.M\Desktop\python projects\animal detection\click.wav"
if not os.path.exists(click_sound_path):
    print(f"Error: Sound file not found at {click_sound_path}")
    exit()

click_sound = pygame.mixer.Sound(click_sound_path)

def start_detection():
    # Play the click sound
    click_sound.play()

    # Path to detection script
    script_path = r"C:\Users\ANANDA KRISHNAN.M\Desktop\python projects\animal detection\anidetect.py"

    # Check if the script exists
    if not os.path.exists(script_path):
        messagebox.showerror("Error", f"File not found: {script_path}")
        return

    # Run the detection script
    try:
        messagebox.showinfo("Starting Detection", "Launching Animal Detection...")
        root.destroy()  # Close the front page
        subprocess.run(["python", script_path], check=True)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Detection script failed:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch detection:\n{e}")

def exit_application():
    root.destroy()

# GUI Code
root = tk.Tk()
root.title("Animal Detection System")
root.geometry("800x600")

# Background Image
background_image_path = r"C:\Users\ANANDA KRISHNAN.M\Desktop\python projects\animal detection\background.jpg"
if not os.path.exists(background_image_path):
    print(f"Error: Background image not found at {background_image_path}")
    exit()

background_image = Image.open(background_image_path)
background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Title Label
title_label = tk.Label(root, text="Welcome to Animal Detection", font=("Arial", 28, "bold"), bg="#000000", fg="white")
title_label.place(relx=0.5, rely=0.2, anchor="center")

# Start Button
start_button = tk.Button(root, text="Start Detection", font=("Arial", 16, "bold"), bg="green", fg="white", command=start_detection)
start_button.place(relx=0.5, rely=0.5, anchor="center")

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 16, "bold"), bg="red", fg="white", command=exit_application)
exit_button.place(relx=0.5, rely=0.6, anchor="center")

# Run GUI
root.mainloop()

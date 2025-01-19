import pyautogui
import time
import pygame
import tkinter as tk
from tkinter import messagebox
import platform

print("Move your mouse to where you want it and wait for 5 seconds...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Mouse position: {x}, {y}")

if platform.system() == 'Windows':
    sound_file = 'C:/Windows/Media/notify.wav'
elif platform.system() == 'Darwin':  
    sound_file = '/System/Library/Sounds/Glass.aiff'
else:  
    sound_file = '/usr/share/sounds/freedesktop/stereo/complete.oga'

pygame.mixer.init()
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

root = tk.Tk()
root.withdraw()

root.attributes('-topmost', True)
root.after(0, lambda: root.attributes('-topmost', True))

def custom_message_box():
    top = tk.Toplevel(root)
    top.title("Mouse Position")
    top.geometry("300x100")
    tk.Label(top, text=f"Mouse position: {x}, {y}").pack(pady=10)
    tk.Button(top, text="Copy", command=lambda: [copy_to_clipboard(f"{x}, {y}"), top.destroy(), root.quit()]).pack(side=tk.LEFT, padx=20)
    tk.Button(top, text="Close", command=lambda: [top.destroy(), root.quit()]).pack(side=tk.RIGHT, padx=20)
    top.attributes('-topmost', True)
    top.after(0, lambda: top.attributes('-topmost', True))

custom_message_box()
root.mainloop()

time.sleep(5)
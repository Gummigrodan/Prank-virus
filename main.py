import tkinter as tk
import random
import os
import vlc
import sys

# Dynamisk sökväg till videon beroende på om det är en exe eller skript
if getattr(sys, 'frozen', False):
    # Körs som exe
    base_path = os.path.dirname(sys.executable)
else:
    # Körs som skript
    base_path = os.path.dirname(os.path.abspath(__file__))

video_path = os.path.join(base_path, "fish.mp4")

root = tk.Tk()
root.geometry("300x200+100000+100000")
root.overrideredirect(True)

count = 0
max_windows = 100  # Max antal videofönster

def skapa_videofonster():
    global count
    count += 1

    x = random.randint(0, 1920 - 300)
    y = random.randint(0, 1080 - 200)
    
    win = tk.Toplevel(root)
    win.geometry(f"300x200+{x}+{y}")
    win.configure(bg="black")
    win.overrideredirect(True)
    
    video_frame = tk.Frame(win, bd=0, highlightthickness=0)
    video_frame.pack(fill="both", expand=True)
    
    try:
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(video_path)
        player.set_media(media)
        
        win.update()
        if sys.platform == "win32":
            player.set_hwnd(video_frame.winfo_id())
        else:
            player.set_xwindow(video_frame.winfo_id())
        
        player.play()
    except Exception as e:
        print(f"Fel vid VLC: {e}")
    
    if count < max_windows:
        root.after(1000, skapa_videofonster)

root.after(1000, skapa_videofonster)
root.mainloop()
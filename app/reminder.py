import json
import schedule
import time
import tkinter as tk

with open('app/config.json', 'r') as f:
    config = json.load(f)


def job():
    window = tk.Tk()
    window.title("Eye Strain Reminder")
    window.withdraw()  
    popup = tk.Toplevel(window)
    popup.geometry("500x100") 
    tk.Label(popup, text=config['reminder_message'], font=("Comfortaa", 16)).pack()

    destroy_id = popup.after(config['reminder_duration'], lambda: popup.destroy())

    dismiss_button = tk.Button(popup, text="OK, I will look away",
                               command=lambda: [popup.after_cancel(destroy_id), popup.destroy()], 
                               font=("Comfortaa", 16))
    dismiss_button.pack()

    window.mainloop()

schedule.every(config['time_between_reminders']).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

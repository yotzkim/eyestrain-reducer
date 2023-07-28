import schedule
import time
import tkinter as tk

def job():
    window = tk.Tk()
    window.title("Eye Strain Reminder")
    window.withdraw()  
    popup = tk.Toplevel(window)
    popup.geometry("500x50")
    popup.configure(bg = 'white')
    tk.Label(popup, text="Look at something 20 feet away for 20 seconds!", fg = "red", bg="white").pack()
    window.after(4000, lambda: window.destroy())
    window.mainloop()


schedule.every(20).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

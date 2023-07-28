import schedule
import time
import tkinter as tk

def job():
    window = tk.Tk()
    window.withdraw()  
    popup = tk.Toplevel(window)
    popup.geometry("200x50")  
    tk.Label(popup, text="Look away from the screen!").pack()
    window.after(2000, lambda: window.destroy())
    window.mainloop()


schedule.every(20).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

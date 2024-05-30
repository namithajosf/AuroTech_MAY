from tkinter import messagebox
import tkinter as tk
import time

class Timer:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Timer & Stopwatch")

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:00:00")

        self.time_elapsed = tk.StringVar()
        self.time_elapsed.set("00:00:00")

        self.running = False
        self.paused = False
        self.start_time = 0
        self.pause_time = 0

        # Countdown Timer UI
        self.timer_label = tk.Label(parent, text='Countdown Timer')
        self.timer_label.pack()

        self.entry_time = tk.Entry(parent, textvariable=self.time_left_var, width=10)
        self.entry_time.pack()

        self.start_timer_button = tk.Button(parent, text='Start', command=self.start_timer)
        self.start_timer_button.pack()

        self.stop_timer_button = tk.Button(parent, text='Stop', command=self.stop_timer)
        self.stop_timer_button.pack()

        # Stopwatch UI
        self.stopwatch_label = tk.Label(parent, text='Stopwatch')
        self.stopwatch_label.pack()

        self.time_elapsed_label = tk.Label(parent, textvariable=self.time_elapsed)
        self.time_elapsed_label.pack()

        self.start_stopwatch_button = tk.Button(parent, text='Start', command=self.start_stopwatch)
        self.start_stopwatch_button.pack()

        self.pause_stopwatch_button = tk.Button(parent, text='Pause', command=self.pause_stopwatch)
        self.pause_stopwatch_button.pack()

        self.reset_stopwatch_button = tk.Button(parent, text='Reset', command=self.reset_stopwatch)
        self.reset_stopwatch_button.pack()

    def start_timer(self):
        try:
            time_left = self.entry_time.get()
            h, m, s = map(int, time_left.split(":"))
            self.time_left = h * 3600 + m * 60 + s
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter time in HH:MM:SS format")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_left_var.set(time.strftime('%H:%M:%S', time.gmtime(self.time_left)))
            self.parent.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "The countdown has finished")

    def stop_timer(self):
        self.time_left = 0

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - (self.pause_time if self.paused else 0)
            self.update_stopwatch()
        
    def pause_stopwatch(self):
        if self.running:
            self.running = False
            self.paused = True
            self.pause_time = time.time() - self.start_time

    def reset_stopwatch(self):
        self.running = False
        self.paused = False
        self.time_elapsed.set("00:00:00")

    def update_stopwatch(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.time_elapsed.set(time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
            self.parent.after(1000, self.update_stopwatch)

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()

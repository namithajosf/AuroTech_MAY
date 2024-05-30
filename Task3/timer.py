from tkinter import messagebox
import tkinter as tk
import time

class Timer:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Timer & Stopwatch")

        self.time_left = tk.StringVar()
        self.time_left.set("00:00:00")

        self.time_elapsed = tk.StringVar
        self.time_elapsed.set("00:00:00")

        self.running = False
        self.pause = False
        self.start_time = 0
        self.pause_time = 0

        #Countdown Timer UI

        self.timer_label = tk.Label(parent, text = 'Countdown Timer')
        self.timer_label.pack()

        self.entry_time = tk.Entry(parent, textvariable = self.time_left, width=10)
        self.entry_time.pack()

        self.start_timer_button = tk.Button('Start', command=self.start_timer)
        self.start_timer_button.pack()

        self.stop_timer_button = tk.Button('Stop', command=self.stop_timer)
        self.stop_timer_button.pack()

        #Stopwatch UI

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

        

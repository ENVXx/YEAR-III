print("MCE 433 - Assignment #1\nElias Newall-Vuillemot - 9/10/2025\nQuestion 2 + EC - Prime Hunter")
input()
import tkinter as tk
from tkinter import messagebox
global primes, isprime
primes = [int(2)]
##
def primecheck(N):
    np = 0
    if N > 10 and str(N)[-1] in [0,2,4,5,6,8]: # no need to check evens or fives
        return 0
    else:
        for p in primes:
            #print(p)
            if p > N/2:
                break
            if N%p == 0:
                return 0
                np = 1
                break
        if np == 0:
            return 1
def primeranger(N):
    n = int(3)
    while n <= N:
        isprime = primecheck(n)
        if isprime == 1:
            primes.append(n)
        n = n+2
##              
def switchmode():
    #this lets me switch between the range and single check using the radio buttons
    if mode_var.get() == "single":
        single_entry.config(state="normal")
        bottom_entry.config(state="disabled")
        top_entry.config(state="disabled")
        result_label.config(text="")
    else:
        single_entry.config(state="disabled")
        bottom_entry.config(state="normal")
        top_entry.config(state="normal")
        result_label.config(text="")
##
def calculate():
    global primes
    #this passes values from the input box up to the prime ranger and prime check functions
    mode = mode_var.get()
    if mode == "single":# Single check
        try:
            number = int(single_entry.get())
            if number <= 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Not so fast!", "inputs have to be positive integers bigger than 2.")
            return
        primeranger(number)
        print(primes)
        if primecheck(number) == 1:
            result_label.config(text="The number is prime! :)", fg="green")
        else:
            result_label.config(text="The number is NOT prime. :(", fg="red")

    elif mode == "range":# range checks
        try:
            bottom = int(bottom_entry.get())
            top = int(top_entry.get())
            if bottom >= top or bottom < 2:
                raise ValueError
        except ValueError: #Prevents the user from putting in invalid inputs
            messagebox.showerror("Nope", "Bottom has to be smaller than Top, both must be integers bigger than 2")
            return
        primeranger(top)
        filtered_primes = [p for p in primes if bottom < p < top] # removing the primes out of the range
        #List window makeer
        range_window = tk.Toplevel(GUI)
        range_window.title("Primes in Range")
        range_window.geometry("300x400")

        tk.Label(range_window, text=f"All the primes between {bottom} and {top}:").pack(pady=5)
        text_box = tk.Text(range_window, wrap=tk.WORD, height=20, width=30)
        text_box.pack(padx=10, pady=5)
        if filtered_primes:
            text_box.insert(tk.END, ", ".join(map(str, filtered_primes)))
        else:
            text_box.insert(tk.END, "But nobody came :(")
    primes = [int(2)]
##    
# Gooey!
GUI = tk.Tk()
GUI.title("Prime Hunter")
GUI.geometry("400x300")
#Radio buttons for mode pick
mode_var = tk.StringVar(value="single")
radio_frame = tk.Frame(GUI)
radio_frame.pack(pady=10)
# these call the switch mode function above to enable/disable entry boxes
tk.Radiobutton(radio_frame, text="Single Prime Check",
               variable=mode_var, value="single", command=switchmode).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(radio_frame, text="Primes in Range",
               variable=mode_var, value="range", command=switchmode).pack(side=tk.LEFT, padx=10)
#Single input
single_frame = tk.Frame(GUI)
single_frame.pack(pady=10)
tk.Label(single_frame, text="Number:").pack(side=tk.LEFT, padx=5)
single_entry = tk.Entry(single_frame)
single_entry.pack(side=tk.LEFT, padx=5)
#Range input
range_frame = tk.Frame(GUI)
range_frame.pack(pady=10)
tk.Label(range_frame, text="Bottom:").pack(side=tk.LEFT, padx=5)
bottom_entry = tk.Entry(range_frame, state="disabled")
bottom_entry.pack(side=tk.LEFT, padx=5)
tk.Label(range_frame, text="Top:").pack(side=tk.LEFT, padx=5)
top_entry = tk.Entry(range_frame, state="disabled")
top_entry.pack(side=tk.LEFT, padx=5)
#Calculate button
calc_button = tk.Button(GUI, text="Calculate", command=calculate)
calc_button.pack(pady=20)
#single prime check
result_label = tk.Label(GUI, text="", font=("Arial", 12))
result_label.pack(pady=10)
#Start it up
GUI.mainloop()
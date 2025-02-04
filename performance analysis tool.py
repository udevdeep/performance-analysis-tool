import tkinter as tk 
from tkinter import scrolledtext 
 
class Process: 
    def _init_(self, arrival_time, 
burst_time): 
        self.arrival_time = arrival_time 
        self.burst_time = burst_time 
        self.waiting_time = 0 
 
def fcfs_schedule(processes): 
    time = 0 
    for process in processes: 
        if process.arrival_time > time: 
            time = process.arrival_time 
        process.waiting_time = time - 
process.arrival_time 
        time += process.burst_time 
 
def rr_schedule(processes, time_quantum): 
    queue = [] 
    time = 0 
    current_process = None 
    i = 0 
 
    while i < len(processes) or 
current_process: 
        while i < len(processes) and 
processes[i].arrival_time <= time: 
            queue.append(processes[i]) 
31  
            i += 1 
 
        if current_process: 
            remaining_time = 
min(time_quantum, 
current_process.burst_time) 
            current_process.burst_time -= 
remaining_time 
            time += remaining_time 
 
            if current_process.burst_time == 
0: 
                current_process.waiting_time 
= time - current_process.arrival_time 
                current_process = None 
            else: 
                queue.append(current_process
 ) 
                current_process = None 
        elif queue: 
            current_process = queue.pop(0) 
        else: 
            time += 1 
 
def sjf_schedule(processes): 
    time = 0 
    processed = [] 
    while processes: 
        eligible_processes = [p for p in 
processes if p.arrival_time <= time] 
32  
        if eligible_processes: 
            shortest_job = 
min(eligible_processes, key=lambda p: 
p.burst_time) 
            processes.remove(shortest_job) 
            shortest_job.waiting_time = time - shortest_job.arrival_time 
            time += shortest_job.burst_time 
            processed.append(shortest_job) 
        else: 
            time += 1 
    # Reorder processes to match the 
original order 
    for p in processed: 
        processes.append(p) 
 
def simulate_scheduling(): 
    selected_algorithm = 
algorithm_choice.get() 
     
    processes = [] 
    for i in range(len(arrival_entries)): 
        arrival_time = 
int(arrival_entries[i].get()) 
        burst_time = 
int(burst_entries[i].get()) 
        processes.append(Process(arrival_tim
 e, burst_time)) 
     
    if selected_algorithm == "FCFS": 
33  
        fcfs_schedule(processes) 
    elif selected_algorithm == "Round 
Robin": 
        time_quantum = 
int(time_quantum_entry.get()) 
        rr_schedule(processes, time_quantum) 
    elif selected_algorithm == "Shortest Job 
First": 
        sjf_schedule(processes) 
     
    result_text.config(state=tk.NORMAL) 
    result_text.delete(1.0, tk.END) 
     
    total_waiting_time = 0 
    for i, process in enumerate(processes): 
        result_text.insert(tk.END, f"Process 
{i + 1}: Waiting Time = 
{process.waiting_time}\n") 
        total_waiting_time += 
process.waiting_time 
     
    if processes: 
        avg_waiting_time = 
total_waiting_time / len(processes) 
        result_text.insert(tk.END, 
f"\nAverage Waiting Time: 
{avg_waiting_time:.2f}\n") 
    else: 
34  
        result_text.insert(tk.END, "\nNo 
processes to calculate average waiting 
time.\n") 
     
    result_text.config(state=tk.DISABLED) 
 
def clear_entries(): 
    for entry in arrival_entries: 
        entry.delete(0, tk.END) 
    for entry in burst_entries: 
        entry.delete(0, tk.END) 
    result_text.config(state=tk.NORMAL) 
    result_text.delete(1.0, tk.END) 
    result_text.config(state=tk.DISABLED) 
 
# Create the main window 
root = tk.Tk() 
root.title("Process Scheduler") 
 
# Labels and Entry widgets for arrival time 
and burst time 
arrival_label = tk.Label(root, text="Arrival 
Time") 
arrival_label.grid(row=0, column=0) 
burst_label = tk.Label(root, text="Burst 
Time") 
burst_label.grid(row=0, column=1) 
 
arrival_entries = [] 
burst_entries = [] 
35  
 
for i in range(5): 
    arrival_entry = tk.Entry(root) 
    burst_entry = tk.Entry(root) 
    arrival_entry.grid(row=i+1, column=0) 
    burst_entry.grid(row=i+1, column=1) 
    arrival_entries.append(arrival_entry) 
    burst_entries.append(burst_entry) 
 
# Label and Entry widget for time quantum 
(for RR) 
time_quantum_label = tk.Label(root, 
text="Time Quantum") 
time_quantum_label.grid(row=7, column=0) 
time_quantum_entry = tk.Entry(root) 
time_quantum_entry.grid(row=7, column=1) 
 
# Dropdown menu for selecting the scheduling 
algorithm 
algorithm_label = tk.Label(root, 
text="Scheduling Algorithm") 
algorithm_label.grid(row=8, column=0) 
algorithm_choices = ["FCFS", "Round Robin", 
"Shortest Job First"] 
algorithm_choice = tk.StringVar() 
algorithm_choice.set("FCFS")  # Default 
choice 
algorithm_menu = tk.OptionMenu(root, 
algorithm_choice, *algorithm_choices) 
algorithm_menu.grid(row=8, column=1) 
36  
 
# Buttons to simulate and clear 
simulate_button = tk.Button(root, 
text="Simulate", 
command=simulate_scheduling) 
clear_button = tk.Button(root, text="Clear", 
command=clear_entries) 
simulate_button.grid(row=9, column=0) 
clear_button.grid(row=9, column=1) 
 
# Text widget to display results with 
scrollbar 
result_text = 
scrolledtext.ScrolledText(root, height=10, 
width=40, wrap=tk.WORD) 
result_text.grid(row=10, columnspan=2) 
 
# Start the GUI main loop 
root.mainloop() 
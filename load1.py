import time
import threading
import random

def simulate_task(task_name, burst_time):
    print(f"Task {task_name} started.")
    time.sleep(burst_time)
    print(f"Task {task_name} completed.")

def main():
    num_tasks = int(input("Enter the number of tasks: "))
    scheduling_algorithm = input("Enter scheduling algorithm (FCFS/SJF/RR/Priority): ")

    tasks = []
    for i in range(num_tasks):
        burst_time = random.randint(1, 10)  # Random burst time for simplicity
        tasks.append((i + 1, burst_time))

    if scheduling_algorithm == "FCFS":
        tasks.sort(key=lambda x: x[0])
    elif scheduling_algorithm == "SJF":
        tasks.sort(key=lambda x: x[1])
    # Add more algorithms as needed.

    threads = []
    for task in tasks:
        thread = threading.Thread(target=simulate_task, args=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

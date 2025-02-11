from multiprocessing import Process, cpu_count
import time

def count(num):
    while num > 0:
        num -= 1
        time.sleep(0.5)
def spawn(num_pro):
    processes = [Process(target = count, args=(1000,)) for i in range(num_pro)]
    for p in processes:
        p.start()
        print(f"Started Process: {p.pid}")
    for p in processes:
        p.join()
        print(f"Process {p.pid} has finished!")

def main():
    processors = cpu_count()
    print("Num of Processors", processors)
    processes = processors  * 300
    print(f"Create {processes} Processes")
    
    spawn(processes)
    
if __name__ == "__main__":
    main()
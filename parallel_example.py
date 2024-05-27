import multiprocessing #umozni vice procesu
import os #os funkce

def worker(num): #vraci na kterem bezi procesu
    print(f'Worker {num} is running on process ID {os.getpid()}')
    return num * num

if __name__ == '__main__':
    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(worker, range(100))
    print(results)
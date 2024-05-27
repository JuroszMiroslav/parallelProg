import multiprocessing

def worker(num):
    return num * num

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
    print(results)

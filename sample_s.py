def worker(num):
    return num * num

if __name__ == '__main__':
    results = [worker(i) for i in range(10)]
    print(results)

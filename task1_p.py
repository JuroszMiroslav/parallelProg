"""Uživatel zadá hodnoty do seznamu. Poté se spustí dva vlákna.
První vlákno najde největší hodnotu v seznamu.
Druhé vlákno najde nejmenší hodnotu v seznamu.
Výsledky se zobrazí na obrazovce
"""

from concurrent.futures import ThreadPoolExecutor


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


if __name__ == '__main__':
    numbers = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_max = executor.submit(find_max, numbers)
        future_min = executor.submit(find_min, numbers)

        max_value = future_max.result()
        min_value = future_min.result()

    print(f'Největší hodnota je: {max_value}')
    print(f'Nejmenší hodnota je: {min_value}')
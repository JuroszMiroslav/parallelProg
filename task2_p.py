"""Uživatel zadá hodnoty do seznamu.
 Poté se spustí dvě vlákna.
 První vlákno vypočítá součet prvků v seznamu.
 Druhé vlákno najde průměrnou hodnotu v seznamu. Výsledek se zobrazí na obrazovce.
"""

from concurrent.futures import ThreadPoolExecutor


def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    numbers = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_sum = executor.submit(calculate_sum, numbers)
        future_average = executor.submit(calculate_average, numbers)

        total_sum = future_sum.result()
        average_value = future_average.result()

    print(f'Součet prvků je: {total_sum}')
    print(f'Průměrná hodnota je: {average_value}')

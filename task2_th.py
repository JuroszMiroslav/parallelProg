"""Uživatel zadá hodnoty do seznamu.
 Poté se spustí dvě vlákna.
 První vlákno vypočítá součet prvků v seznamu.
 Druhé vlákno najde průměrnou hodnotu v seznamu. Výsledek se zobrazí na obrazovce.
"""
import threading


# Funkce pro výpočet součtu
def calculate_sum(numbers):
    total_sum = sum(numbers)
    print(f'Součet prvků je: {total_sum}')


# Funkce pro výpočet průměru
def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    print(f'Průměrná hodnota je: {average}')


# Hlavní část programu
if __name__ == '__main__':
    # Uživatel zadá hodnoty do seznamu
    numbers = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

    # Vytvoření a spuštění vláken
    sum_thread = threading.Thread(target=calculate_sum, args=(numbers,))
    average_thread = threading.Thread(target=calculate_average, args=(numbers,))

    sum_thread.start()
    average_thread.start()

    sum_thread.join()
    average_thread.join()

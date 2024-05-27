"""Uživatel zadá hodnoty do seznamu. Poté se spustí dva vlákna.
První vlákno najde největší hodnotu v seznamu.
Druhé vlákno najde nejmenší hodnotu v seznamu.
Výsledky se zobrazí na obrazovce
"""
import threading


# Funkce pro nalezení největší hodnoty
def find_max(numbers):
    max_value = max(numbers)
    print(f'Největší hodnota je: {max_value}')


# Funkce pro nalezení nejmenší hodnoty
def find_min(numbers):
    min_value = min(numbers)
    print(f'Nejmenší hodnota je: {min_value}')


# Hlavní část programu
if __name__ == '__main__':
    # Uživatel zadá hodnoty do seznamu
    numbers = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

    # Vytvoření a spuštění vláken
    max_thread = threading.Thread(target=find_max, args=(numbers,))
    min_thread = threading.Thread(target=find_min, args=(numbers,))

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

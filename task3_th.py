"""Uživatel zadá cestu k souboru obsahujícímu sadu čísel.
Poté se spustí dva vlákna. První vlákno vytvoří nový soubor, do kterého zapíše pouze sudé prvky ze seznamu.
Druhé vlákno vytvoří nový soubor, do kterého zapíše pouze liché prvky ze seznamu. Vypište počet sudých a lichých prvků
"""
import threading


# Funkce pro zápis sudých čísel do souboru
def write_even_numbers(numbers, filename):
    even_numbers = [num for num in numbers if num % 2 == 0]
    with open(filename, 'w') as f:
        for num in even_numbers:
            f.write(f'{num}\n')
    print(f'Počet sudých čísel: {len(even_numbers)}')


# Funkce pro zápis lichých čísel do souboru
def write_odd_numbers(numbers, filename):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    with open(filename, 'w') as f:
        for num in odd_numbers:
            f.write(f'{num}\n')
    print(f'Počet lichých čísel: {len(odd_numbers)}')


# Hlavní část programu
if __name__ == '__main__':
    # Uživatel zadá cestu k souboru
    file_path = input("Zadejte cestu k souboru: ")

    # Načtení čísel ze souboru
    with open(file_path, 'r') as f:
        numbers = list(map(int, f.read().split()))

    # Vytvoření a spuštění vláken
    even_thread = threading.Thread(target=write_even_numbers, args=(numbers, 'even_numbers.txt'))
    odd_thread = threading.Thread(target=write_odd_numbers, args=(numbers, 'odd_numbers.txt'))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

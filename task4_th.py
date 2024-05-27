"""Uživatel zadá cestu k souboru a hledané slovo.
Poté se spustí vlákno, které hledá slovo v souboru.
 Výsledek se vypíše na obrazovku.
"""

import threading


# Funkce pro hledání slova v souboru
def search_word_in_file(file_path, search_word):
    found = False
    with open(file_path, 'r') as f:
        for line in f:
            if search_word in line:
                found = True
                break
    if found:
        print(f'Slovo "{search_word}" bylo nalezeno v souboru.')
    else:
        print(f'Slovo "{search_word}" nebylo nalezeno v souboru.')


# Hlavní část programu
if __name__ == '__main__':
    # Uživatel zadá cestu k souboru a hledané slovo
    file_path = input("Zadejte cestu k souboru: ")
    search_word = input("Zadejte hledané slovo: ")

    # Vytvoření a spuštění vlákna
    search_thread = threading.Thread(target=search_word_in_file, args=(file_path, search_word))

    search_thread.start()
    search_thread.join()

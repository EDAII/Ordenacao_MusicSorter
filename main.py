# main.py
from musicas_base import musicas_iniciais
import time
import copy

# Helper to convert mm:ss to seconds (int)
def mmss_to_seconds(mmss):
    try:
        parts = mmss.strip().split(':')
        minutes = int(parts[0])
        seconds = int(parts[1])
        return minutes * 60 + seconds
    except:
        return 0

# Display formatting
def format_musica(m):
    return f"{m['titulo']} - {m['artista']} ({m['duracao']})"

# Sorting algorithms implemented to sort list of dicts by key function

def bubble_sort(arr, key_func):
    n = len(arr)
    a = arr[:]  # work on a copy
    swaps = 0
    comps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comps += 1
            if key_func(a[j]) > key_func(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    return a, comps, swaps

def insertion_sort(arr, key_func):
    a = arr[:]
    comps = 0
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if key_func(a[j]) > key_func(key):
                a[j+1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j+1] = key
    return a, comps, shifts

def quick_sort(arr, key_func):
    a = arr[:]
    comps = {'count': 0}
    def _qs(low, high):
        if low < high:
            p = partition(low, high)
            _qs(low, p-1)
            _qs(p+1, high)
    def partition(low, high):
        pivot = key_func(a[high])
        i = low - 1
        for j in range(low, high):
            comps['count'] += 1
            if key_func(a[j]) <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        return i+1
    _qs(0, len(a)-1)
    return a, comps['count'], None

# Timing wrapper
def timed_sort(func, arr, key_func):
    start = time.perf_counter()
    sorted_arr, comps, aux = func(arr, key_func)
    end = time.perf_counter()
    return sorted_arr, comps, aux, end - start

# Key function factory
def key_by(field):
    if field == 'titulo':
        return lambda m: m['titulo'].lower()
    if field == 'artista':
        return lambda m: m['artista'].lower()
    if field == 'duracao':
        return lambda m: mmss_to_seconds(m['duracao'])
    return lambda m: m['titulo'].lower()

# Menu functions
musicas = [dict(m) for m in musicas_iniciais]  # working copy

def listar_musicas(lista=None, limit=20):
    if lista is None:
        lista = musicas
    print(f"\n--- Listando {len(lista)} músicas (mostrando até {limit}) ---")
    for i, m in enumerate(lista[:limit], 1):
        print(f"{i}. {format_musica(m)}")
    if len(lista) > limit:
        print(f"... e mais {len(lista)-limit} músicas\n")
    else:
        print()

def inserir_musica():
    titulo = input("Título: ").strip()
    artista = input("Artista: ").strip()
    duracao = input("Duração (mm:ss): ").strip()
    # basic validation for duration
    if ':' not in duracao:
        print("Formato de duração inválido. Use mm:ss\n")
        return
    musicas.append({'titulo': titulo, 'artista': artista, 'duracao': duracao})
    print("Música adicionada!\n")

def ordenar_menu():
    print("Escolha o critério:")
    print("1. Título")
    print("2. Artista")
    print("3. Duração")
    campo_opt = input("Opção: ").strip()
    campo = {'1': 'titulo', '2': 'artista', '3': 'duracao'}.get(campo_opt, 'titulo')
    keyfunc = key_by(campo)

    print("Escolha o algoritmo:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    alg_opt = input("Algoritmo: ").strip()

    if alg_opt == '1':
        sorted_arr, comps, aux, elapsed = timed_sort(bubble_sort, musicas, keyfunc)
    elif alg_opt == '2':
        sorted_arr, comps, aux, elapsed = timed_sort(insertion_sort, musicas, keyfunc)
    else:
        sorted_arr, comps, aux, elapsed = timed_sort(quick_sort, musicas, keyfunc)

    print(f"\nOrdenação concluída em {elapsed:.6f} segundos (comparações: {comps})\n")
    listar_musicas(sorted_arr, limit=50)

def comparar_todos():
    key_choice = input("Comparar por (1) Título (2) Artista (3) Duração: ").strip()
    campo = {'1':'titulo','2':'artista','3':'duracao'}.get(key_choice, 'titulo')
    keyfunc = key_by(campo)
    print(f"\nComparando algoritmos por '{campo}' em {len(musicas)} músicas...\n")
    funcs = [('Bubble', bubble_sort), ('Insertion', insertion_sort), ('Quick', quick_sort)]
    results = []
    for name, func in funcs:
        # use a fresh copy for each
        sorted_arr, comps, aux, elapsed = timed_sort(func, musicas, keyfunc)
        results.append((name, elapsed, comps))
        print(f"{name}: {elapsed:.6f}s (comparisons: {comps})")
    print()

def main():
    while True:
        print("=== MusicSorter ===")
        print("1. Inserir música")
        print("2. Listar músicas")
        print("3. Ordenar músicas")
        print("4. Comparar todos os algoritmos")
        print("0. Sair")
        opt = input("Escolha uma opção: ").strip()
        if opt == '1':
            inserir_musica()
        elif opt == '2':
            listar_musicas()
        elif opt == '3':
            ordenar_menu()
        elif opt == '4':
            comparar_todos()
        elif opt == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == '__main__':
    main()

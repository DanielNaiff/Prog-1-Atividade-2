import random
import time
# Classe sort é responsavel por por encapsular os métodos de ordenação e os contadores de comparações e trocas
class Sort:
    def __init__(self, data):
        self.data = data
        self.comparisons = 0
        self.swaps = 0

    def reset_counters(self):
        self.comparisons = 0
        self.swaps = 0
    # Implementação do algoritmo bubblesort
    def bubble_sort(self):
        self.reset_counters()
        start_time = time.time()
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                self.comparisons += 1
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    self.swaps += 1
        end_time = time.time()
        return end_time - start_time
    # Implementação do algoritmo selectionsort
    def selection_sort(self):
        self.reset_counters()
        start_time = time.time()
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.comparisons += 1
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.swaps += 1
        end_time = time.time()
        return end_time - start_time
    # Implementação do algoritmo insertionsort
    def insertion_sort(self):
        self.reset_counters()
        start_time = time.time()
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i-1
            while j >= 0 and key < self.data[j]:
                self.comparisons += 1
                self.data[j + 1] = self.data[j]
                j -= 1
                self.swaps += 1
            self.data[j + 1] = key
        end_time = time.time()
        return end_time - start_time
# A função generate data gera os dados de forma aleatoria ou decrescente de acordo com a escolha
def generate_data(size, order):
    if order == "decrescente":
        return list(range(size, 0, -1))
    elif order == "aleatorio":
        data = list(range(size))
        random.shuffle(data)
        return data
# A função main presenta um menu para o usuário escolher a quantidade de valores, a disposição dos valores e o algoritmo de ordenação, exibe o vetor antes e depois da ordenação, além do tempo de execução, número de comparações e trocas.
def main():
    sizes = [10, 100, 1000, 10000]
    orders = ["decrescente", "aleatorio"]
    algorithms = ["bubblesort", "selectionsort", "insertionsort"]

    print("Escolha a quantidade de valores:")
    for i, size in enumerate(sizes):
        print(f"{i+1}. {size}")
    size_choice = int(input("Digite o número correspondente: ")) - 1

    print("Escolha a disposição dos valores:")
    for i, order in enumerate(orders):
        print(f"{i+1}. {order}")
    order_choice = int(input("Digite o número correspondente: ")) - 1

    print("Escolha o algoritmo de ordenação:")
    for i, algo in enumerate(algorithms):
        print(f"{i+1}. {algo}")
    algo_choice = int(input("Digite o número correspondente: ")) - 1

    data = generate_data(sizes[size_choice], orders[order_choice])
    sorter = Sort(data.copy())

    print("Vetor antes da ordenação:", data)

    if algorithms[algo_choice] == "bubblesort":
        exec_time = sorter.bubble_sort()
    elif algorithms[algo_choice] == "selectionsort":
        exec_time = sorter.selection_sort()
    elif algorithms[algo_choice] == "insertionsort":
        exec_time = sorter.insertion_sort()

    print("Vetor após a ordenação:", sorter.data)
    print(f"Tempo de execução: {exec_time:.6f} segundos")
    print(f"Número de comparações: {sorter.comparisons}")
    print(f"Número de trocas: {sorter.swaps}")

if __name__ == "__main__":
    main()
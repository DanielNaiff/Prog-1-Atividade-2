import random
import time

#Alunos:
#Daniel Naiff da Costa
#Lucas Correa Magno

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
    # Implementação do algoritmo quicksort
    def quick_sort(self):
        self.reset_counters()
        start_time = time.time()
        self._quick_sort(0, len(self.data) - 1)
        end_time = time.time()
        return end_time - start_time

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)
    # Metodo auxiliar para organização da sublista
    def _partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.swaps += 1
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.swaps += 1
        return i + 1
    # Implementação do algoritmo radixsort
    def radix_sort(self):
        self.reset_counters()
        start_time = time.time()
        max_val = max(self.data)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(exp)
            exp *= 10
        end_time = time.time()
        return end_time - start_time
    # Metodo auxiliar usado para ordenar os números com base no digito isolado por exp
    def _counting_sort(self, exp):
        n = len(self.data)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self.data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = self.data[i] // exp
            output[count[index % 10] - 1] = self.data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            self.data[i] = output[i]
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
    algorithms = ["bubblesort", "quicksort", "radixsort"]

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
    elif algorithms[algo_choice] == "quicksort":
        exec_time = sorter.quick_sort()
    elif algorithms[algo_choice] == "radixsort":
        exec_time = sorter.radix_sort()

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    print("Vetor após a ordenação:", sorter.data)
    print(f"Tempo de execução: {exec_time:.6f} segundos")
    print(f"Número de comparações: {sorter.comparisons}")
    print(f"Número de trocas: {sorter.swaps}")

if __name__ == "__main__":
    main()
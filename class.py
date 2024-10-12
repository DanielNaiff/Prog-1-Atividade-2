import random
import time

class TADOrdenacao:
    def __init__(self):
        self.vetor = []
        self.comparacoes = 0
        self.trocas = 0

    def gerar_vetor(self, quantidade, tipo):
        if tipo == "aleatorio":
            self.vetor = [random.randint(1, 10000) for _ in range(quantidade)]
        elif tipo == "decrescente":
            self.vetor = list(range(quantidade, 0, -1))

    def mergesort(self, vetor):
        if len(vetor) <= 1:
            return vetor

        meio = len(vetor) // 2
        esquerda = self.mergesort(vetor[:meio])
        direita = self.mergesort(vetor[meio:])

        resultado = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):
            self.comparacoes += 1
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
            self.trocas += 1

        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    def ordenar(self):
        inicio = time.time()
        self.vetor = self.mergesort(self.vetor)
        tempo_execucao = time.time() - inicio
        return tempo_execucao

def main():
    print("Escolha a quantidade de valores (10, 100, 1000, 10000): ")
    quantidade = int(input())
    
    print("Escolha o tipo de entrada (aleatorio, decrescente): ")
    tipo = input()

    print("Escolha o algoritmo de ordenação (mergesort, quicksort, heapsort): ")
    algoritmo = input()

    ordenacao = TADOrdenacao()
    ordenacao.gerar_vetor(quantidade, tipo)

    print("Vetor antes da ordenação:", ordenacao.vetor)

    if algoritmo == "mergesort":
        tempo_execucao = ordenacao.ordenar()
    else:
        print("Algoritmo não implementado.")

    print("Vetor ordenado:", ordenacao.vetor)
    print("Tempo de execução:", tempo_execucao)
    print("Número de comparações:", ordenacao.comparacoes)
    print("Número de trocas:", ordenacao.trocas)

if __name__ == "__main__":
    main()

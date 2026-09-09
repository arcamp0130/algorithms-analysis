import random

class Algorithms:
    def __init__(self):
        pass

    def bubble_sort_brute_force(arr):
        n = len(arr)
        # Ciclo externo corre n veces de forma fija
        for i in range(n):
        # Ciclo interno compara elementos adyacentes
            for j in range(0, n - 1):
                if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def insertion_sort(self, lista):
        """
        Ordenamiento por Inserción.
        Complejidad: O(N^2)
        """
        arr = lista.copy()
        for i in range(1, len(arr)):
            clave = arr[i]
            j = i - 1
            # Compara la clave con los elementos anteriores y los desplaza
            while j >= 0 and arr[j] > clave:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = clave
        return arr

    def gnome_sort(self, lista):
        arr = lista.copy()
        i = 0
        n = len(arr)
        
        while i < n:
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1  # Avanza si está en orden
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Intercambia
                i -= 1  # Retrocede un paso
                
        return arr

    def stooge_sort_rec(self, arr, l, h):
        if l >= h:
            return

        # Si el primer elemento es mayor que el último, intercambiar
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]

        # Si hay 3 o más elementos en el rango
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            # Aplicar fuerza bruta a los 3 tercios superpuestos
            self.stooge_sort_rec(arr, l, h - t)       # Primeros 2/3
            self.stooge_sort_rec(arr, l + t, h)       # Últimos 2/3
            self.stooge_sort_rec(arr, l, h - t)       # Primeros 2/3 de nuevo

    def stooge_sort(self, lista):
        arr = lista.copy()
        self.stooge_sort_rec(arr, 0, len(arr) - 1)
        return arr

    def exchange_sort(self, lista):
        """
        Ordenamiento por Intercambio Directo (Exchange Sort).
        Complejidad: O(N^2)
        """
        arr = lista.copy()
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Si el elemento posterior es menor, intercambia de inmediato
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

class Utils:
    def __init__(self):
        pass

    def generateArray(self, size, minVal, maxVal):
        aux = [random.randint(minVal, maxVal) for i in range(size)]
        return aux
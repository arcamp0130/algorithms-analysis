class Algorithms:
  def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      # Suponemos que el primer elemento no ordenado es el menor
      min_idx = i
      # Buscamos en el resto de la lista
      for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
          min_idx = j
          # Intercambiamos el menor encontrado con el primer elemento actual
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

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
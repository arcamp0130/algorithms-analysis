import time
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

start_time = time.perf_counter() # Start timer
array = [6,5,3,1,8,7,2,4]
bubble_sort(array)

print("\n")
print("Lista ordenada:", array, "\n")
print("------------------------------")
end_time = time.perf_counter() # Start timer
exec_time = end_time - start_time
print(f"Execution time: {exec_time:.6f} seconds")

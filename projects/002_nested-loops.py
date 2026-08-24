import time

n = [1,2,3,4,5,6,7]
k = 300

start_time = time.perf_counter() # Start timer

print("Primer for", "\n")
for i in range(k):
    print(i)

print("-------------------------")

print("\n")
print("Segundo for", "\n")
for i in range(k):
    print(i)

end_time = time.perf_counter() # End timer
exec_time = end_time - start_time
print(f"Execution time: {exec_time:.6f} seconds")

def fibonacci_dp(n):
    fib = [0] * (n + 1)
    
    if n >= 1:
        fib[1] = 1
    
   
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib

n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_dp(n)

print("Fibonacci sequence:")
print(fib_sequence)

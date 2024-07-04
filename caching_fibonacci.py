def caching_fibonacci():
    cache = {}
    def fibonacci(n: int) -> int: 
        if n <= 0: return 0
        if n <= 1: return 1
        if n in cache: return cache[n]
            
        cache[n] = fibonacci(n - 1) + fibonacci(n-2)
        return cache[n]    
    return fibonacci

fibonacci = caching_fibonacci()

print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(15))
print(fibonacci(150)) # return cached result


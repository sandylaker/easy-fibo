def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(f"n must be non-negative, but got {n}")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
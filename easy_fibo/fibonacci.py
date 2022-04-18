def fibonacci(n: int) -> int:
    """Compute the fibonacci number.

    Args:
        n: Index of the fibonacci number.

    Returns:
        The n-th fibonacci number.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, but got {n}")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
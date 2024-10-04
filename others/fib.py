def fib(n:int|None=5) -> int:
    """fibonacci sequence function

    Args:
        n: sequence end
    Returns:
        fib number
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
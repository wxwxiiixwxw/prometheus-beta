def find_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs are positive integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Find GCD using Euclidean algorithm
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
    
    # LCM formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)
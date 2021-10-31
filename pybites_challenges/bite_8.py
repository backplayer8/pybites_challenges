# Bite 8: Rotate String Characters


def rotate(string: str, n: int):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    return f"{string[n:]}{string[:n]}"  # I see the redundancy with f string, now

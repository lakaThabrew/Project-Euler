def is_s_number(square, root):
    s = str(square)
    n = len(s)
    # Generate all bitmasks for split positions (n-1 bits for n-digit number)
    for mask in range(1, 1 << (n - 1)):  # skip mask = 0 (single part)
        total = 0
        part = ''
        for i in range(n):
            part += s[i]
            if i == n - 1 or (mask & (1 << i)):
                total += int(part)
                part = ''
        if total == root:
            return True
    return False

def compute_T(limit):
    from math import isqrt
    total = 0
    for i in range(1, isqrt(limit) + 1):
        sq = i * i
        if is_s_number(sq, i):
            total += sq
    return total

# ⚡ Fast answer to T(10^12)
print("T(10^12) =", compute_T(10**12))

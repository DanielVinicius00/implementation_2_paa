def horspool_matching(P, T):
    m = len(P)
    n = len(T)
    table = shift_table(P)
    
    i = m - 1
    while i < n:
        k = 0
        while k < m and P[m - 1 - k] == T[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            i += table[T[i]]
    
    return -1

# Exemplo
P = "example"
T = "this is an example"
print(horspool_matching(P, T))  # Saída: 11 (posição onde "example" começa em T)

from algoritmo.shift_table import create_shift_table

def HorspoolMatching(P, T):
    m = len(P)
    n = len(T)
    table = create_shift_table(P)  # Use create_shift_table instead of table
    
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
print(HorspoolMatching(P, T))  # Saída: 11 (posição onde "example" começa em T)

def shift_table(P):
    m = len(P)
    table = {chr(i): m for i in range(256)}
    
    for j in range(m - 1):
        table[P[j]] = m - 1 - j
    
    return table

# Exemplo
P = "example"
table = shift_table(P)
print(table)  # Exemplo de saída: {'e': 1, 'x': 5, 'a': 4, 'm': 3, 'p': 2, 'l': 1, ...}

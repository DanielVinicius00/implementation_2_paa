def preprocess_bad_character_rule(P):
    m = len(P)
    bad_char_shift = {chr(i): m for i in range(256)}
    
    for j in range(m - 1):
        bad_char_shift[P[j]] = m - 1 - j
    
    return bad_char_shift

def preprocess_good_suffix_rule(P):
    m = len(P)
    good_suffix_shift = [0] * m
    z = [0] * m
    z_box(P[::-1], z)
    z = z[::-1]
    
    longest = 0
    for j in range(m):
        if z[j] > 0:
            longest = j
        good_suffix_shift[m - z[j]] = j
    
    for j in range(m - 1, 0, -1):
        if z[j] > 0:
            for k in range(j + 1 - z[j], j + 1):
                if good_suffix_shift[k] == 0:
                    good_suffix_shift[k] = j
    
    for j in range(m - 1):
        if good_suffix_shift[j] == 0:
            good_suffix_shift[j] = longest
    
    return good_suffix_shift

def z_box(S, Z):
    n = len(S)
    Z[0] = n
    L, R = 0, 0
    
    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and S[R] == S[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < n and S[R] == S[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1

def boyer_moore(T, P):
    m = len(P)
    n = len(T)
    
    bad_char_shift = preprocess_bad_character_rule(P)
    good_suffix_shift = preprocess_good_suffix_rule(P)
    
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and P[j] == T[s + j]:
            j -= 1
        if j < 0:
            print(f"Padrão encontrado na posição {s}")
            s += good_suffix_shift[0]
        else:
            s += max(good_suffix_shift[j], bad_char_shift[T[s + j]] - m + 1 + j)

# Exemplo
P = "example"
T = "this is an example"
boyer_moore(T, P)  # Saída: Padrão encontrado na posição 11

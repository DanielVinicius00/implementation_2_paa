def distribution_counting_sort(A, l, u):
    n = len(A)
    count = [0] * (u - l + 1)
    B = [0] * n
    
    for i in range(n):
        count[A[i] - l] += 1
    
    for j in range(1, u - l + 1):
        count[j] += count[j - 1]
    
    for i in range(n - 1, -1, -1):
        B[count[A[i] - l] - 1] = A[i]
        count[A[i] - l] -= 1
    
    return B

# Exemplo
A = [3, 1, 2, 2]
print(distribution_counting_sort(A, 1, 3))  # Saída: [1, 2, 2, 3]

def comparison_counting_sort(A):
    n = len(A)
    B = [0] * n
    for i in range(n):
        count = 0
        for j in range(n):
            if A[j] < A[i] or (A[j] == A[i] and j < i):
                count += 1
        B[count] = A[i]
    return B

# Exemplo
A = [3, 1, 2, 2]
print(comparison_counting_sort(A))  # Saída: [1, 2, 2, 3]
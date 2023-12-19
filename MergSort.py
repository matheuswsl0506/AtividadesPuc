def merge(A, B):
    resultado = []

    while A and B:
        if A[0] < B[0]:
            resultado.append(A.pop(0))
        else:
            resultado.append(B.pop(0))

    while A:
        resultado.append(A.pop(0))
    while B:
        resultado.append(B.pop(0))

    return resultado


A = [12, 35, 52, 64]
B = [5, 15, 23, 55, 75]
R = merge(A, B)

print("Fila A:",A)
print("Fila B:", B)
print("Resultado:",R)
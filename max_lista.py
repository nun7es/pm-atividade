def max_lista(arr):
    if len(arr) == 1:
        return arr[0]
    max_restante = max_lista(arr[1:])
    return arr[0] if arr[0] > max_restante else max_restante

# Teste
print(max_lista([1, 5, 10, 25, 3]))  # Deve mostrar 25

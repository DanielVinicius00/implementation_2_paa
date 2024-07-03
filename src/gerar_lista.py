def gerar_lista(tamanho, tipo):
    if tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho - 1, -1, -1))
    elif tipo == 'aleatoria':
        lista = list(range(tamanho))
        random.shuffle(lista)
        return lista
    else:
        raise ValueError(
            "Tipo de lista desconhecido. Use 'ordenada', 'inversa' ou 'aleatoria'.")
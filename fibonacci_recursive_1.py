def fibonacci(quantidade, sequencia=(0, 1)):
    # importante: condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros parâmetros da sequência
    for fib in fibonacci(20):
        print(fib)

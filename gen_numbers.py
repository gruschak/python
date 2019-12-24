def gen_numbers(n: int, prefix=None):
    """ Генерирует список всех чисел BASE-ричной системы счисления,
        имеющих n разрядов
    """
    BASE = 10    # основание системы счисления = 2
    prefix = prefix or []
    if (n == 0):
        print(*prefix)
    else:
        for digit in range(BASE):
            prefix.append(digit)
            gen_numbers(n - 1, prefix)
            prefix.pop()


gen_numbers(2)

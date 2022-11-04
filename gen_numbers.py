RADIX = 16  # Must not be greater than 16
LENGTH = 3  # Number of digits of the generated numbers


def generate_numbers(radix: int, n: int, prefix: list = None):
    """ Генерирует список всех чисел BASE-ричной системы счисления,
        имеющих n разрядов
    """
    if radix > 16:
        raise ValueError("Radix must not be greater than 16")

    prefix = prefix or []
    if n == 0:
        print(*prefix)
    else:
        for digit in range(radix):
            prefix.append(hex(digit)[2:].upper() if 9 < digit < 16 else digit)
            generate_numbers(radix, n - 1, prefix)
            prefix.pop()


if __name__ == '__main__':
    generate_numbers(radix=RADIX, n=LENGTH)

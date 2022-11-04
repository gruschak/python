"""
This program is an example of recurrent algorithm usage.

Task: Generate and print the numbers of the given radix
having the given length (number of digits) in its numeric representation.
"""

RADIX = 16  # Must not be greater than 16
LENGTH = 4  # Number of digits of the generated numbers


def generate_numbers(radix: int, tail_length: int, prefix: list = None):
    """ Generate numbers of the given radix
    :param radix: base number of the positional numeral system
    :param tail_length: number of digits to generate
    :param prefix: the given list of digits that compose a prefix for a number representation
    """
    if not (1 < radix < 17):
        raise ValueError("Radix must be between 2 and 16")

    prefix = prefix or []
    if tail_length == 0:
        print(*prefix)
    else:
        for digit in range(radix):
            prefix.append(hex(digit)[2:].upper())
            generate_numbers(radix, tail_length - 1, prefix)
            prefix.pop()


if __name__ == '__main__':
    generate_numbers(radix=RADIX, tail_length=LENGTH)

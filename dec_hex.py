# Преобразование к шестнадцатеричному представлению числа

x = int(input("input number --> "))
digits = []

while x > 0:
	digit = x % 0x10
	x //= 0x10
	digits.append(hex(digit))

print(digits[::-1])

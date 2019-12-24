x = int(input())
while x > 0: 
	digit = x % 0x10
	print( hex(digit), end=' ' )
	x //= 0x10

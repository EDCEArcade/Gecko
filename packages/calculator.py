import os
clear = lambda: os.system("cls")
def main():
	clear()
	print("Please enter digit #1")
	d1 = int(input())
	print("Please enter digit #2")
	d2 = int(input())
	print("Please enter operator a, s, d, m")
	op = input()
	if op == "a":
		result = d1 + d2
	if op == "s":
		result = d1 - d2
	if op == "d":
		result = d1 / d2
	if op == "m":
		result = d1 * d2
	print("The answer is " + result)

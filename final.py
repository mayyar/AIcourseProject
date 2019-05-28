import numpy as np
import sys
import random

A = list()
def printResult():
	#see the result
	for i in A:
		for j in i:
			print(j, end=" ")
		print()

def main():
	# print (sys.argv[1])
	with open(sys.argv[1], 'r') as f:
		size = int(f.readline())
		
		for line in f:
			data = list()
			for alphabet in line.split(" "):
				data.append(alphabet[0])
			A.append(data)
		printResult()
		# print(A)
	firstorNot = input("User go first or not(Y/N):")
	if firstorNot == 'Y':
		color = input("Enter your color(B/R): ")
		while A != [['X'] * size] * size:
			row = input("Enter a row: ")
			col = input("Enter a col: ")

			while A[int(row)-1][int(col)-1] != color:
				print("Wrong position... try again")
				row = input("Enter a row: ")
				col = input("Enter a col: ")
				
			A[int(row)-1][int(col)-1] = 'X'
			printResult()

			#上：檢查左右上 A[int(row)-1-1][int(col)-1]


			#下：檢查左右下 A[int(row)][int(col)-1]


			#左：檢查左上下 A[int(row)-1][int(col)-1-1]


			#右：檢查右上下 A[int(row)-1][int(col)]


			AIrow = random.randint(1,size)
			AIcol = random.randint(1,size)
			
			while(A[int(AIrow)-1][int(AIcol)-1] == 'X' or A[int(AIrow)-1][int(AIcol)-1] == color):
				AIrow = random.randint(1,size)
				AIcol = random.randint(1,size)

			print("AI Enter a row: " , AIrow)
			print("AI Enter a col: " , AIcol)

			A[int(AIrow)-1][int(AIcol)-1] = 'X'

			printResult()





	elif firstorNot == 'N':
		pass
	else:
		pass


if __name__ == "__main__":
	main()
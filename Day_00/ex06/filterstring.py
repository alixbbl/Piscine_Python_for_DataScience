# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 6b *******************

import sys

def main():
	if len(sys.argv) != 3 or not (isinstance(sys.argv[1], str) and isinstance(sys.argv[2], int)):
		print("AssertionError: the arguments are bad")
		sys.exit(1)
	else:
		N = int(sys.argv[2])
		try:
			list_words = sys.argv[1].split(" ")
			is_valid = lambda word: len(word) > N
			filtered_list = [word for word in list_words if is_valid(word)]
		except Exception as e:
			print(e)
			sys.exit(1)
		print(filtered_list)

if __name__ == "__main__":
	main()

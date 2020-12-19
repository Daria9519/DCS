if __name__ == "__main__":
	try:
		with open("name.txt") as f:
			name = f.readline().strip()
	except FileNotFoundError as e:
		print("File not found!")
		exit(1)

	print(f"This is my {name} with docker!")


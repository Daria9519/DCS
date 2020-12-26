if __name__ == "__main__":
	try:
		with open("home/text_file/created_text.txt", 'r') as f:
			name = f.readline().strip()
	except FileNotFoundError as e:
		print("File not found!")
		exit(1)
	print(f"True or false?: {name}")

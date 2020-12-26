if __name__ == "__main__":
	try:
		with open("home/text_file/name.txt", 'r') as f:
			name = f.readline().strip()
	except FileNotFoundError as e:
		print("File not found!")
		exit(1)
	text = f"This is my {name} with docker!"
	print(text)
	with open("home/text_file/created_text.txt", 'w') as new_file:
		new_file.write(text)
		new_file.close()
	

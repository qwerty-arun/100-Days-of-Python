def check_for_line():
	word = "Arun"
	data = True
	line_no = 1
	with open("practice.txt", "r") as f:
		while data:
			data = f.readline()
			if(word in data):
				print(line_no)
			line_no+=1


with open("practice.txt","a") as f:
	f.write("Virtual Machine Grandmaster\n")
	f.write("Arun")
	f.close()

check_for_line()

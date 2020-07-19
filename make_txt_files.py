alllines = ""
with open("AllStories.csv","r") as fp:
	alllines = fp.read()

stories = alllines.split("\n\n")

for story in stories:
	output = ""
	storylist = story.split("\n")
	filename = storylist.pop(0) + ".txt"
	print(filename)
	#print(storylist)
	with open(filename, "w") as fp:
		for line in storylist:
			if line != "\n":
				output += line + "\n"
		print(output.rstrip("\n"))
		fp.write(output)
	print("********************************")

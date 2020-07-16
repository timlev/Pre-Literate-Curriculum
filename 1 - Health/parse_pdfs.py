import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input_directory", nargs='+', default=".")
parser.add_argument("-nc", "--noconvert", action="store_true", help="don't convert pdfs into pngs")
args = parser.parse_args()
print(args)


#Convert all likely story pages (10-13) into pngs
if not args.noconvert:
	pdffiles = [x for x in os.listdir(args.input) if x.endswith(".pdf")]
	print(pdffiles)
	for f in pdffiles:
		week, name = f.split(" ")[0], f.split(" ")[1].replace(".pdf","")
		print(week)
		print(name)
		os.system("pdftoppm -f 10 -l 13 -png '" + f + "' " + week + name + "-story")


#Cut story up into pictures
storyfiles = ["1Body-story-12.png","1Body-story-13.png"]
sf = "1BodyStory.pdf"
sf = "2AilmentsStory.pdf"
tp = [150, 30, 1160, 640]
p1 = [70, 700, 600, 1090]
p2 = [650, 700, 1180, 1090]
p3 = [70, 1140 , 600, 1510]
p4 = [650, 1140, 1180, 1510]

#title
os.system("pdftoppm -f 1 -l 1 -png -x " + str(tp[0]) + " -y " + str(tp[1]) + " -W " + str(tp[2]-tp[0]) + " -H " + str(tp[3] - tp[1]) + " " + sf + " title")

#p1
os.system("pdftoppm -f 1 -l 1 -png -x " + str(p1[0]) + " -y " + str(p1[1]) + " -W " + str(p1[2]-p1[0]) + " -H " + str(p1[3] - p1[1]) + " " + sf + " p1")

#p2
os.system("pdftoppm -f 1 -l 1 -png -x " + str(p2[0]) + " -y " + str(p2[1]) + " -W " + str(p2[2]-p2[0]) + " -H " + str(p2[3] - p2[1]) + " " + sf + " p2")

#p3
os.system("pdftoppm -f 1 -l 1 -png -x " + str(p3[0]) + " -y " + str(p3[1]) + " -W " + str(p3[2]-p3[0]) + " -H " + str(p3[3] - p3[1]) + " " + sf + " p3")

#p4
os.system("pdftoppm -f 1 -l 1 -png -x " + str(p4[0]) + " -y " + str(p4[1]) + " -W " + str(p4[2]-p4[0]) + " -H " + str(p4[3] - p4[1]) + " " + sf + " p4")

"""
pdftk 1\ Body.pdf cat 12-13 output 1BodyStory.pdf
pdfimages -all 1BodyStory.pdf /tmp/out
"""

"""
#Get matching page
pdftoppm -f 4 -l 4 -png 1\ Body.pdf matching

#Get Story
pdftoppm -f 12 -l 13 -png 1\ Body.pdf body-story

#Get Comprehension
pdftoppm -f 22 -l 22 -png -x 0 -y 100 -W 700 -H 670 1\ Body.pdf comprehension
"""

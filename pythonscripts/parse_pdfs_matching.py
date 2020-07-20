import os
import argparse
import glob

parser = argparse.ArgumentParser()
#parser.add_argument("input_directory", nargs='+', default=".")
parser.add_argument("-nc", "--noconvert", action="store_true", help="don't convert pdfs into pngs")
args = parser.parse_args()
print(args)


#Convert all likely story pages (10-13) into pngs
if not args.noconvert:
	pdffiles = [x for x in glob.glob("./*/Stories/*.pdf") if "story" not in x]
	print(pdffiles)
	for f in pdffiles:
		#f = os.path.basename(f)
		week, name = os.path.basename(f).split(" ")[0], os.path.basename(f).split(" ")[1].replace(".pdf","")
		print(week)
		print(name)
		os.system("pdftoppm -f 3 -l 4 -png '" + f + "' " + week + name + "-matching")
	quit()

originalfiles = {'5 Housing Ads.pdf': [9,10], '3 Settings.pdf': [12,13], '1 Rooms in my house.pdf': [12,13], '2 Furniture in my house.pdf': [12,13], '4 Problems in my apartment.pdf': [12,13]}
newfiles = []

for f in originalfiles:
	print(f, originalfiles[f])
	#os.system("pdftk '" + f + "' cat " + str(originalfiles[f][0]) + "-" + str(originalfiles[f][1]) + " output '" + f.replace(".pdf","story.pdf'"))
	newfiles.append(f.replace(".pdf","story.pdf"))

print(newfiles)


#Cut story up into pictures
#sf = "1BodyStory.pdf"
#sf = "2AilmentsStory.pdf"
tp = [150, 30, 1160, 640]
p1 = [0, 710, 600, 1100]
p2 = [640, 710, 1180, 1100]
p3 = [0, 1160 , 600, 1510]
p4 = [640, 1165, 1180, 1510]
p5 = [0, 30, 600, 450]
p6 = [640, 30, 1200, 450]
p7 = [0, 550, 600, 900]
p8 = [640, 530, 1200, 900]
p9 = [0, 1060, 600, 1350]

for sf in newfiles:
	print(sf.replace(".pdf",""))
	#title
	os.system("pdftoppm -f 1 -l 1 -png -x " + str(tp[0]) + " -y " + str(tp[1]) + " -W " + str(tp[2] - tp[0]) + " -H " + str(tp[3] - tp[1]) + " '" + sf + "' 'p0." + sf.replace(".pdf","'"))
	#p1
	os.system("pdftoppm -f 1 -l 1 -png -x " + str(p1[0]) + " -y " + str(p1[1]) + " -W " + str(p1[2] - p1[0]) + " -H " + str(p1[3] - p1[1]) + " '" + sf + "' 'p1." + sf.replace(".pdf","'"))
	#p2
	os.system("pdftoppm -f 1 -l 1 -png -x " + str(p2[0]) + " -y " + str(p2[1]) + " -W " + str(p2[2] - p2[0]) + " -H " + str(p2[3] - p2[1]) + " '" + sf + "' 'p2." + sf.replace(".pdf","'"))
	#p3
	os.system("pdftoppm -f 1 -l 1 -png -x " + str(p3[0]) + " -y " + str(p3[1]) + " -W " + str(p3[2] - p3[0]) + " -H " + str(p3[3] - p3[1]) + " '" + sf + "' 'p3." + sf.replace(".pdf","'"))
	#p4
	os.system("pdftoppm -f 1 -l 1 -png -x " + str(p4[0]) + " -y " + str(p4[1]) + " -W " + str(p4[2] - p4[0]) + " -H " + str(p4[3] - p4[1]) + " '" + sf + "' 'p4." + sf.replace(".pdf","'"))
	#2nd page
	#p5
	os.system("pdftoppm -f 2 -l 2 -png -x " + str(p5[0]) + " -y " + str(p5[1]) + " -W " + str(p5[2] - p5[0]) + " -H " + str(p5[3] - p5[1]) + " '" + sf + "' 'p5." + sf.replace(".pdf","'"))
	#p6
	os.system("pdftoppm -f 2 -l 2 -png -x " + str(p6[0]) + " -y " + str(p6[1]) + " -W " + str(p6[2] - p6[0]) + " -H " + str(p6[3] - p6[1]) + " '" + sf + "' 'p6." + sf.replace(".pdf","'"))
	#p7
	os.system("pdftoppm -f 2 -l 2 -png -x " + str(p7[0]) + " -y " + str(p7[1]) + " -W " + str(p7[2] - p7[0]) + " -H " + str(p7[3] - p7[1]) + " '" + sf + "' 'p7." + sf.replace(".pdf","'"))
	#p8
	os.system("pdftoppm -f 2 -l 2 -png -x " + str(p8[0]) + " -y " + str(p8[1]) + " -W " + str(p8[2] - p8[0]) + " -H " + str(p8[3] - p8[1]) + " '" + sf + "' 'p8." + sf.replace(".pdf","'"))
	#p9
	os.system("pdftoppm -f 2 -l 2 -png -x " + str(p9[0]) + " -y " + str(p9[1]) + " -W " + str(p9[2] - p9[0]) + " -H " + str(p9[3] - p9[1]) + " '" + sf + "' 'p9." + sf.replace(".pdf","'"))




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

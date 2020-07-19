import os, glob


matchingfiles = glob.glob("*//PPTX/*.html")

print(matchingfiles)


for f in matchingfiles:
	with open(f,"r") as fp:
		blob = fp.read()
	#css
	blob = blob.replace("./../drag_n_drop_theme.css","../../drag_n_drop_theme.css")
	#script
	blob = blob.replace("../jquery.ui.touch-punch.min.js","../../jquery.ui.touch-punch.min.js")
	#stylesheet
	blob = blob.replace("../sliders.css","../../sliders.cs")
	#sounds
	blob = blob.replace("../sounds/","../../units/sounds/")
	print(blob)
	with open(f, "w") as fp:
		fp.write(blob)

import os

pptxfiles = [x for x in os.listdir(".") if x.endswith(".pptx")]

os.mkdir("PPTX")

for f in pptxfiles:
		week, name = f.split(" ")[0], f.split(" ")[1].replace(".pptx","")
		print(week)
		print(name)
		#Move all PPTX into PPTX folder
		os.rename(f,os.path.join("PPTX",f))
		os.chdir("PPTX")
		os.system("libreoffice --headless --convert-to pdf '" + f +"'")
		os.system("convert -density 400 '" + f.replace(".pptx",".pdf") + "' " + week + name + "%d.png")
		os.chdir("..")



"""


Well, I added

  <policy domain="coder" rights="read | write" pattern="PDF" />

just before </policymap> in /etc/ImageMagick-6/policy.xml and that makes it work again, but not sure about the security implications of that.
"""

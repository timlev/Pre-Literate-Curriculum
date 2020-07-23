import glob, shutil, os


#Still need to do this for food unit

oldfiles = glob.glob("../*/PPTX/*.html")
print(oldfiles)

for of in oldfiles:
    nf = os.path.basename(of)
    print(nf)
    shutil.move(nf,of)

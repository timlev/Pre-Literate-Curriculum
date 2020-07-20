import os, glob
from bs4 import BeautifulSoup

matchingfiles = glob.glob("*//PPTX/*.html")

##print(matchingfiles)

soundfilesrequired = []
wordsrequired = []
soundfilesdownloaded = [os.path.basename(x) for x in glob.glob("units/sounds/*")]
soundfilesneeded = []

for filename in matchingfiles:
	soup = BeautifulSoup(open(filename), "html5lib")
	soundtags = soup.find_all("audio")
	##print(soundtags)
	for tag in soundtags:
		soundfilesrequired.append(os.path.basename(tag["src"]))
		wordsrequired.append(os.path.basename(tag["src"]).replace(".mp3",""))
	#with open(f,"r") as fp:
		#blob = fp.read()

wordsrequired = list(set(wordsrequired))
soundfilesrequired = list(set(soundfilesrequired))

#print(len(soundfilesdownloaded),len(soundfilesrequired))
soundfilesneeded = [x for x in soundfilesrequired if x not in soundfilesdownloaded]
#print([x.replace(".mp3","") for x in soundfilesneeded], len(soundfilesneeded))
for x in soundfilesdownloaded:
	print(x.replace(".mp3",""))

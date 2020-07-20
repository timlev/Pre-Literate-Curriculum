import os, glob
from bs4 import BeautifulSoup

matchingfiles = glob.glob("../*//PPTX/*.html")

##print(matchingfiles)

soundfilesrequired = []
wordsrequired = []
soundfilesdownloaded = [os.path.basename(x) for x in glob.glob("../units/sounds/*")]
soundfilesneeded = []

learning_english_sound_files = [os.path.basename(x) for x in os.listdir("/home/levtim/GitProjects/Learning-English-HTML/sounds/") if x.endswith(".mp3")]
read_story_sound_files = [os.path.basename(x) for x in os.listdir("/home/levtim/GitProjects/read-story/sounds/") if x.endswith(".mp3")]
combined_sound_files = soundfilesdownloaded + learning_english_sound_files + read_story_sound_files

#print(combined_sound_files)
#print(len(combined_sound_files))

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
soundfilesneeded = [x for x in soundfilesrequired if x not in combined_sound_files]
#print([x.replace(".mp3","") for x in soundfilesneeded], len(soundfilesneeded))
for x in soundfilesneeded:
	print(x.replace(".mp3",""))
print(len(soundfilesneeded))

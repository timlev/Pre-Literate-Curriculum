import urllib
import urllib.parse
import urllib.request
import os
import tempfile
import platform
import bs4

def check_downloaded_word(word, directory="./"):
    soundfiles = os.listdir(directory)
    #strip extension
    downloaded_words = [os.path.splitext(x)[0] for x in soundfiles]
    if word in downloaded_words:
        return True
    else:
        return False

def get_wiki(word, directory="./"):
    if check_downloaded_word(word, directory):
        print(word + " already downloaded")
        return 0
    #search for wiktionary word
    base = "https://en.wiktionary.org/wiki/"
    query = base + urllib.parse.quote(word)
    print(query)
    try:
        response = urllib.request.urlopen(query)
        print(response)
    except:
        print("Couldn't find", word)
        return 1
    print("Processing response")
    index = bs4.BeautifulSoup(response,"html5lib")
    filenameguess = "File:en-us-" + word + ".ogg"
    #print(index.find(title=filenameguess))
    #Jump to file wiktionary page
    query = base + filenameguess
    try:
        response = urllib.request.urlopen(query)
    except:
        print("HTTP error for " + query)
        return 2
    print(response)
    index = bs4.BeautifulSoup(response, "html5lib")
    links = index.find_all("a")
    oggsource = ""
    for link in links:
        href = str(link.get("href"))
        if "upload" in href and "n-us" in href and ".ogg" in href and word in href:
            oggsource = "https:" + href

    print("Downloading to: " + os.path.join(directory, word + ".ogg"))
    try:
        print("Getting ogg...")
        getogg = urllib.request.urlopen(oggsource)
        print("Saving file ...")
        ofp = open(os.path.join(directory, word + ".ogg"),'wb')
        print("Writing file ...")
        ofp.write(getogg.read())
        ofp.close()
        return os.path.join(directory, word + ".ogg")
    except:
        #print("Could not download:", word)
        return 2

    # oggsource = ""
    # for line in response:
        # if "src" in line and "n-us" in line and ".ogg" in line:
            # print(line)
            # start = line.find("""src="//""") + len("""src="//""")
            # end = line.find(".ogg") + len(".ogg")
            # oggsource = line[start:end]
            # oggsource = "https://" + oggsource
            # print(oggsource)
            # break
    # print(query)
    # print(oggsource)
    # print("Downloading to:", os.path.join(directory, word + ".ogg"))
    # try:
        # print("Getting ogg...")
        # getogg = urllib.urlopen(oggsource)
        # print("Saving file ...")
        # ofp = open(os.path.join(directory, word + ".ogg"),'wb')
        # print("Writing file ...")
        # ofp.write(getogg.read())
        # ofp.close()
        # return os.path.join(directory, word + ".ogg")
    # except:
        # #print("Could not download:", word)
        # return 2

#download wiktionary ogg file

def download_gstatic(word, directory="./"):
    if check_downloaded_word(word, directory):
        return 0
    base = "https://ssl.gstatic.com/dictionary/static/sounds/de/0/"
    query = base + word + ".mp3"
    print(query)
    try:
        response = urllib.urlopen(query)
    except:
        print("Couldn't find", word)
        return 1
    try:
        print("Getting mp3...")
        getmp3 = urllib.urlopen(query)
        print("Saving file ...")
        ofp = open(os.path.join(directory, word + ".mp3"),'wb')
        print("Writing file ...")
        ofp.write(getmp3.read())
        ofp.close()
        return os.path.join(directory, word + ".mp3")
    except:
        #print("Could not download:", word)
        return 2

#convert ogg to mp3

def convert_ogg_to_mp3(oggfile, remove_ogg = False):
    oggpath = os.path.abspath(oggfile)
    ogg_dir = os.path.dirname(oggfile)
    oggfile = os.path.basename(oggfile)
    mp3file = oggfile.replace(".ogg", ".mp3")
    mp3path = oggpath.replace(".ogg",".mp3")
    os.system('ffmpeg -i "' + oggpath + '" -acodec libmp3lame "' + mp3path + '"')
    if remove_ogg:
        os.remove(oggpath)
    return mp3path

if __name__ == "__main__":
    #if get_wiki("joyful") == 0:
    #    convert_ogg_to_mp3("i'm" + ".ogg", True)
    #print(download_gstatic("blowhole"))
    #print(download_gstatic("myword"))
    #wordlist = ["zero", "ten", "twenty", "one", "eleven", "twenty-one", "two", "twelve", "twenty-two", "three", "thirteen", "twenty-three", "four", "fourteen", "twenty-four", "five", "fifteen", "twenty-five", "six", "sixteen", "twenty-six", "seven", "seventeen", "twenty-seven", "eight", "eighteen", "twenty-eight", "nine", "nineteen", "twenty-nine", "thirty", "forty", "seventy", "thirty-one", "fifty", "eighty", "thirty-two", "sixty", "ninety"]
    #wordlist = ["musician"]
    wordlist = ['', 'in', 'sink', 'he', 'open', 'officers', 'brown', 'hat', 'money', 'minnesota', 'appointment', 'different', 'fighters', 'back', 'pants', 'it', 'stomach', 'ad', 'crossing', 'kitchen,', 'driver', 'cord', 'glue', 'backpack', 'rug', 'restroom', 'is', 'university', 'rice', 'underwear', 'colors', 'takes', 'moves', 'usa', 'pencils', 'fare', 'library', 'his', 'having', 'a', 'am', 'short', 'down', 'boots', 'emergency?', 'name', 'oh', 'dining', 'st', 'dresser', 'from', 'cars', 'pay', 'syrup', 'date', 'kitchen', 'children', 'across', 'neighborhood', 'coat', 'eye', 'big', 'purple', 'exit', 'shopping', 'fever', 'runny', 'farm', 'window', 'city', 'security', 'learn', 'scarf', 'yellow', 'scissors', 'what’s', 'sister', 'shorts', 'upstairs', 'comes', 'have', 'smoking', 'point', 'whiteboard', 'old', 'teacher', 'locked', 'home', 'janitor', 'couch', 'no!', 'these', 'socks', 'listen', 'medium', 'count', 'teach', 'right', 'phone', 'straight', 'leaking', 'front', 'boat', 'they', 'i’m', 'broken', 'erasers', 'stop', 'mittens', 'transfer', 'ave', 'family', 'young', 'red', 'deposit', 'plane', 'we', 'number', 'work', 'daughter', 'ambulance', 'english', 'happy', 'women’s', 'circle', '612-543-6719', 'walks', 'room,', 'bedroom,', 'goes', 'it’s', 'look', 'room', 'elementary', 'ramsey', 'write', 'school', 'doctor', 'dc', 'truck', 'to', 'attack', '16', 'stove', 'fix', 'aids', 'letter', 'tv', 'restrooms', 'cold', 'police', 'eat', 'wears', 'mother', 'do', 'social', 'the', 'arms', 'walk', 'office', 'leg', 'son', 'sore', 'ready', 'post', 'interpreter', '$900', 'your', 'neck', 'bathroom', 'address', 'turn', 'signs', 'apply', 'ask', 'needs', 'toilet', '2', 'for', 'color', 'attack!', 'swimming', 'flu', 'shoes', 'men’s', 'headache', 'blue', 'are', 'garage', 'bicycle', 'small', 'mechanic', 'clean', 'me', 'stairs', 'babies', 'copy', 'too', 'sweater', 'college', 'application', 'clothes', 'orange', 'factory', 'card', 'at', 'county', 'insurance', 'an', 'check-out', 'folders', 'shower', 'pregnant', 'signature', 'healthy', 'door', 'has', 'weather', 'experience', 'legs', 'grow', 'hurts', 'large', 'and', 'don’t', 'mirror', 'clock', 'clinic', 'come', 'problems', 'book', 'i', 'tall', 'shirts', 'telephone', 'food', 'my', 'out', 'sign', 'cough', 'middle', 'nose', 'closets', 'fit!', 'station', 'table', 'tub', 'no', 'bedrooms', 'paul', 'heart', 'worker', 'hospital', 'many', 'sandals', 'bed', 'chest', 'medicine', 'manager', 'doesn’t', 'make', 'rent', '3301', 'preschool', 'two', 'off', 'chairs', 'green', 'bank', 'give', 'wait', 'fridge', 'bus', 'on', 'accident', 'apartment', 'class', 'list', 'cashier', 'bhutan', 'this', 'al', 'cream', 'works', 'pull', 'need', 'go', 'head', 'she', 'birth', 'one', 'dale', 'lamp', 'take', 'say,', 'see', 'wife', 'emergency', 'band', 'fire', 'show', 'farmer', 'computer', 'train', 'body', 'suit', 'high', 'lost', 'left', 'throat', 'help', 'aspirin', 'you”', 'mail', 'of', 'living', 'store', '911', 'tapti', 'shirt', 'buying', 'extra', 'notebooks', 'job', 'things', 'you', '“thank', 'call', 'buys', 'ointment', 'some', 'drops', 'drive', 'sit', 'read', 'check']
    print(len(wordlist))
    missing_words = []
    for word in wordlist:
        get_wiki(word)
        try:
            convert_ogg_to_mp3(word + ".ogg", True)
        except:
            print("************\n Problem with " + word + "\n******************\n")
            missing_words.append(word)
    print(missing_words)

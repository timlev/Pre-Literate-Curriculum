import csv, os
from bs4 import BeautifulSoup

def produce_blob(filename,wordlist, soup):
    index = 0
    #print(wordlist)
    if len(wordlist) == 7:
        columns = seven
        p_and_d_table_id = "threecolspictures_and_destinations"
    elif len(wordlist) == 8:
        columns = eight
        p_and_d_table_id = "threecolspictures_and_destinations"
    elif len(wordlist) == 9:
        columns = nine
        p_and_d_table_id = "threecolspictures_and_destinations"
    elif len(wordlist) == 10:
        columns = ten
        p_and_d_table_id = "fourcolspictures_and_destinations"
    elif len(wordlist) == 11:
        columns = eleven
        p_and_d_table_id = "fourcolspictures_and_destinations"
    elif len(wordlist) == 12:
        columns = twelve
        p_and_d_table_id = "fourcolspictures_and_destinations"
    else:
        print("Wordlist is too large")
        quit()
    #Add Title
    title = soup.new_tag("title")
    title.string = filename
    soup.head.append(title)
    #Add header
    soup.body.append(create_header(filename))
    #Add pictures and destinations table
    picture_and_destinations_table = soup.new_tag("table", id= p_and_d_table_id )
    for row in columns:
        tr = soup.new_tag("tr", id = str(columns.index(row) + 1))
        picture_and_destinations_table.append(tr)
        #picture_and_destinations_table.append(soup.new_tag("tr", id = str(columns.index(row) + 1)))
        for col in row:
            tr.append(create_pic_dest_td(col,index))
            index += 1
    soup.body.append(picture_and_destinations_table)
    #Add answers_div
    index = 0
    answers_div = soup.new_tag("div",id="answers_div")
    for row in columns:
        for col in row:
            answers_div.append(create_answer(col,index))
            answers_div.append(create_audio(col,index))
            index += 1
    soup.body.append(answers_div)
    add_scripts()
    return filename, soup.prettify()

seven = [["1a","1b","1c"],["2a","2b","2c"],["3a"]]
eight = [["1a","1b","1c"],["2a","2b","2c"],["3a","3b"]]
nine = [["1a","1b","1c"],["2a","2b","2c"],["3a","3b","3c"]]
ten = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a"]]
eleven = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a","3b","3c"]]
twelve = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a","3b","3c","3d"]]


def create_header(filename):
    header = soup.new_tag("div",id="header")
    back_button = soup.new_tag("div", id="back_button")
    img = soup.new_tag("img", src="../images/arrow_back-24px.png")
    back_button.append(img)
    back_button_text = soup.new_tag("div", id="back_button_text")
    back_button_text.string = "Back"
    back_button.append(back_button_text)
    header.append(back_button)
    header_title = soup.new_tag("div", id="title")
    header_title.string = os.path.basename(filename)
    header.append(header_title)
    return header

def create_pic_dest_td(col, index):
    td = soup.new_tag("td", id = str(col))
    image_div = soup.new_tag("div")
    image_div["class"] = "image"
    image = soup.new_tag("img", src="imgs/" + wordlist[index] + ".jpg")
    image_div.append(image)
    td.append(image_div)
    destination_div = soup.new_tag("div", id="droppable")
    destination_div["class"] = "destination"
    destination_div["name"] = str(col[0]) + """,""" + str(col[1])
    td.append(destination_div)
    return td


def create_answer(col, index):
    #answer_div can be added to container div id="answers_div"
    answer_div = soup.new_tag("div" , id=str(wordlist[index]))
    answer_div["name"] = str(col[0]) + """,""" + str(col[1])
    answer_div["class"] = "source"
    text_div = soup.new_tag("div")
    text_div.string = wordlist[index]
    answer_div.append(text_div)
    sound_button_image = soup.new_tag("img", src="../images/volume_up-24px_purple.png", id=str(wordlist[index]) + "_sound_button")
    sound_button_image["class"] = "sound_button"
    answer_div.append(sound_button_image)
    #soup.body.append(answer_div)
    return answer_div

def create_audio(col,index):
    base_src = "../units/sounds/"
    audio_div = soup.new_tag("audio", id=wordlist[index] + "_audio", src=base_src + wordlist[index] +".mp3")
    audio_div["name"] = str(col[0]) + """,""" + str(col[1])
    audio_div["class"] = "source_audio"
    #soup.body.append(audio_div)
    return audio_div

def add_scripts():
	script = soup.new_tag("script", src="../js/matching.js")
	soup.body.append(script)
	
def writefile(blobtup):
    #print(blobtup[0])
    with open(blobtup[0] + ".html", "w") as fp:
        fp.write(blobtup[1])

#For ALL FILES
with open("AllMatching.csv","r") as fp:
    allmatching = fp.read().split("\n\n")

#print(allmatching)
matchingindexjson = {}

for lesson in allmatching:
    lesson = list(filter(None,lesson.split("\n")))
    base = "../"
    unit = lesson.pop(0)
    name = lesson.pop(0)
    if unit not in matchingindexjson:
        matchingindexjson[unit] = []
    matchingindexjson[unit].append(os.path.join(unit,name) + ".html")
    name = os.path.join(base,unit,name)
    wordlist = lesson
    soup = BeautifulSoup(open("header_starter.html"),"html5lib")
    #print(produce_blob(name, wordlist, soup))
    #print(name)
    #print([x.decode("utf-8").replace(u'\u2019', "'") for x in wordlist])
    writefile(produce_blob(name, wordlist,soup))

#For matchingindex.html

print(matchingindexjson)

#Run fix_food_unit.py
import fix_food_unit

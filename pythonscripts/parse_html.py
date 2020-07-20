# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, Tag
import string
import re
import argparse
import sys
import os
import download_wiktionary_word
import copy
import glob

def stripID(audioID):
    chunk = audioID[audioID.index("_") + 1:]
    return chunk

def tokenize_word(word):
    token = str(word).lower()
    acceptableCharacters = string.ascii_letters + string.digits     + "-" +"'"
    token = "".join([x for x in token if x in acceptableCharacters])
    if token != "":
        print(token)
        return token
    else:
        return False


def buildAllAudio(master_word_list):
    for token in master_word_list:
        audioID = token + "_audio"
        source = "../sounds/" + token + ".mp3"
        audio = soup.new_tag("audio", id=audioID, src=source, type="audio/mpeg", preload="auto")#, oncanplaythrough="console.log(this)")
        #print( audio)
        body.insert(0, audio)


def buildSpan(word, token, pnum, wnum):
    spanID = str(pnum) + str(wnum) + "_" + token
    tag = soup.new_tag("span", id=spanID, onclick="play(this)")
    word += ' '
    tag.insert(0, word)
    print(tag)
    return tag

def download_sound_files(master_word_list):
    print( "Downloading sound files ...")
    soundfiles = [f.replace(".mp3","") for f in os.listdir("./sounds/") if f.endswith(".mp3")]

    for word in [word for word in master_word_list if word not in soundfiles]:
        downloaded_word = False
        try:
            oggpath = download_wiktionary_word.get_wiki(word, "./sounds/")
            if oggpath != 2:
                download_wiktionary_word.convert_ogg_to_mp3(oggpath, True)
                downloaded_word = True
        except:
            print( "Could't convert from wiki", word)
        if downloaded_word == False:
            try:
                mp3path = download_wiktionary_word.download_gstatic(word, "./sounds/")
            except:
                print( "Couldn't download from GStatic")


parser = argparse.ArgumentParser()
parser.add_argument("input", nargs='+')
parser.add_argument("--output_dir", default=".")
parser.add_argument("--index", default="./index.html")
parser.add_argument("--skip_sounds", action="store_true")
parser.add_argument("--skip_index", action="store_true")
args = parser.parse_args(sys.argv[1:])

allfilenames = args.input

print( "Files to analyze: {}".format(allfilenames))

for filename in allfilenames:
    print( "Processing {} ...".format(filename))

    base_name = os.path.basename(filename)
    short_name = os.path.splitext(base_name)[0]
    print(short_name)
    with open(filename, "r") as fp:
        lines = fp.readlines()
    print(lines)
    #soup = BeautifulSoup(open(filename), "lxml")
    #soup = BeautifulSoup(open(filename), "html.parser")
    soup = BeautifulSoup("","html5lib")
    #soup = BeautifulSoup(open(filename), "html5lib")
    #paragraphs = soup.findAll('p')
    #print(paragraphs)
    html = soup.new_tag("html")
    soup.append(html)
    new_header = soup.new_tag("head")
    html.append(new_header)
    script = soup.new_tag("script", src="../../js/playsound.js")
    new_header.append(script)
    new_header.append(soup.new_tag("title"))
    new_header.title.string = short_name
    style = soup.new_tag('style', 'word-wrap: normal;')
    new_header.append(style)

    #styles = soup.findAll('style')
    """
    for style in styles:
        if style.string is not None and "font-size" in style.string:
            style.string = re.sub("font-size\s*?:.*?;","font-size:2em;", style.string)
        if style.string is not None and "line-height" in style.string:
            style.string = re.sub("line-height\s*?:.*?%","", style.string)
        new_header.insert(0, style)
        """
    font = soup.new_tag('link', href="https://fonts.googleapis.com/css?family=Didact+Gothic", rel="stylesheet")
    new_header.append(font)

    fontstyles = soup.new_tag('style')
    fontstyles.string = "p {font-family: 'Didact Gothic', sans-serif; line-height: 1.5; font-size:2em; text-indent: 5%;}\n span:hover {cursor: pointer;}"
    new_header.append(fontstyles)

    html.append(new_header)


    body = soup.new_tag('body')
    html.append(body)
    body['style'] = "font-size:2em"
    #arguments = [('id','player')]
    audio = soup.new_tag("audio", id="player", type="audio/mpeg", preload="auto")
    body.append(audio)

    fspimg = soup.new_tag("img", src="../../images/plus-800px.png", onclick='increaseFont()')
    fsmimg = soup.new_tag("img", src="../../images/minus-800px.png", onclick='decreaseFont()')
    body.append(fsmimg)
    body.append(fspimg)

    #Build Master Word List
    master_word_list = []
    for pnum, p in enumerate(lines):
        words = p.split(" ")
        print("enumerate")
        print( words)
        if pnum < 5:
            img = soup.new_tag("img", src= os.path.join("imgs","p" + str(pnum) + "." + short_name + "-1.png"))
        else:
            img = soup.new_tag("img", src= os.path.join("imgs","p" + str(pnum) + "." + short_name + "-2.png"))
        body.append(img)
        ptag = soup.new_tag("p")
        """
        for pos, word in enumerate(words):
            if u'\u2019' in word:
                words[pos] = word.replace(u'\u2019', "'")
            if u'\u201c' in word:
                words[pos] = word.replace(u'\u201c', '"')
            if u'\u201d' in word:
                words[pos] = word.replace(u'\u201d', '"')
            if u'\u2014' in word:
                words[pos] = word.replace(u'\u2014', '--')
        #words = [x.encode('ascii', errors='ignore') for x in words]"""

        #words = [word.encode('ascii', 'xmlcharrefreplace') for word in words]
        """if 'style' in p and "line-height" in p['style']:
            #print( p['style'])
            p['style'] = re.sub("line-height\s*?:.*?%","", p['style"""
        for wnum, word in enumerate(words):
            token = tokenize_word(word)
            if token != False:
                master_word_list.append(token)
                ptag.insert(wnum, buildSpan(word, token, pnum, wnum))
        body.append(ptag)

    p = soup.new_tag("p")
    body.append(p)
    master_word_list = list(set(master_word_list))
    buildAllAudio(master_word_list)

    #Write out new html file
    newfile = args.output_dir + "/new_" + base_name.replace(".txt",".html")
    print( "Saving new file ...")
    #print(soup.encode("utf-8"))
    with open(newfile, "wb") as wb:
        wb.write(soup.encode("utf-8"))
    print( "File saved at", newfile)

    #Add to Index
    # if not args.skip_index:
    #     index = BeautifulSoup(open(args.index), "html5lib")
    #     new_link = index.new_tag('a', href = newfile)
    #     new_link.string = short_name
    #     index.body.append(index.new_tag('br'))
    #     index.body.append(new_link)
    #
    #     #Write Index file
    #     print( "Updating index.html...")
    #     with open(args.index, "wb") as wb:
    #       wb.write(index.encode("utf-8"))
    #     print( "File saved at " + args.index)

    #Download Words
    if not args.skip_sounds:
        download_sound_files(master_word_list)

    soundfiles = [f.replace(".mp3","") for f in os.listdir("./sounds/") if f.endswith(".mp3")]
    missing_words = "\n".join([word for word in master_word_list if word not in soundfiles])

    with open("missing_words/" + base_name + "_missing_words.txt","w+") as wb:
        wb.write(missing_words)

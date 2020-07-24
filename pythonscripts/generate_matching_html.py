import csv, os
from bs4 import BeautifulSoup

header_starter = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<link href="https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap" rel="stylesheet">
		 <link href="https://fonts.googleapis.com/css2?family=Sen&display=swap" rel="stylesheet">

  <link rel="stylesheet" type="text/css" href="../drag_n_drop_theme.css" />
<link href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.2/css/lightness/jquery-ui-1.10.2.custom.min.css" rel="stylesheet">
<script src="https://code.jquery.com/jquery-1.7.2.min.js"></script>
<script src="https://code.jquery.com/ui/1.8.21/jquery-ui.min.js"></script>
<script src="../jquery.ui.touch-punch.min.js"></script>
<script>
var i = 0;
var all_words = document.getElementsByClassName("source");

function finished_playing_list(event){
	console.log(event.target.id + "Finished");
	var txtObj = document.getElementById(event.target.id.replace("_audio",""));
	txtObj.style.backgroundColor = 'transparent';
	play_sound(play_sound);
}

function finished_playing(event){
	console.log(event.target.id + "Finished");
        var txtid = event.target.id.replace("_audio","");
	var txtObj = document.getElementById(txtid);
	txtObj.style.backgroundColor = 'transparent';
}

function play_sound(play_sound){
	if (i < all_words.length){
		var word = all_words[i].id;
		console.log(word);
		var next_word = word + "_audio";
		txtObj = document.getElementById(word);
		audioObj = document.getElementById(next_word);
		//audioObj.onended = finished_playing;
		$(audioObj).on("ended", finished_playing_list);
		txtObj.style.backgroundColor = "yellow";
		document.getElementById(next_word).play();
		i += 1;
	}
	else {
		i = 0;
		$(".source_audio").off();
		$(".source_audio").on("ended",finished_playing);
		//document.getElementById("playallbutton").remove();
	}
}

function tapHandler(event){
    var audioId = event.target.id;
    if (audioId.includes("_sound_button")){
        audioId = audioId.replace("_sound_button","_audio");
    }
    else {
        audioId = audioId + "_audio";
    }
    txtObj = document.getElementById(audioId.replace("_audio",""));
    console.log(txtObj);
    audioObj = document.getElementById(audioId);
    audioObj.addEventListener("ended",finished_playing);
    txtObj.style.backgroundColor = "yellow";
    audioObj.play();
};

$(function() {
  var score = 0;
window.words_remaining = 0;
console.log(window.orientation);

  $(".source").on("dragstart", tapHandler );
  $(".sound_button").on("click",tapHandler);
  $( ".source" ).draggable({ revert: "invalid", scroll: false});
  $( ".destination" ).droppable({
    drop: function( event, ui ) {
      var dragged_category = ui.draggable.attr("name").split(",")[0];
      var dropped_category = $(this).attr("name").split(",")[0];
      if (ui.draggable.attr("name") == $(this).attr("name")){
          ui.draggable.draggable("disable");
          // $(this).css({"background-color":"#70db70"});
    		$(this).removeClass("wrong_answer");
    		$(this).addClass("correct_answer");
            document.getElementById(ui.draggable.attr("id") + "_sound_button").remove();
          $(this).html(ui.draggable.html());
          ui.draggable.hide();
  //$(this).toggleClass("source");
          score += 1;
  $(this).droppable({disabled: true});
  console.log(window.words_remaining);
          window.words_remaining -= 1;
          moves += 1;
          $("#status").text("Current score: " + score + " Words remaining: " + window.words_remaining);
          if (window.words_remaining == 0){
             document.getElementById("menu_link").innerHTML = "Finished!<br>Current score: " + score + " Words remaining: " + window.words_remaining + "<br>Moves: " + moves
          }
    }
    else{
        //ui.draggable.css({"color":"red"});
				ui.draggable.addClass("wrong_answer");
        moves += 1;

    }

    }
  });
});

    var score = 0;
    var moves = 0;
</script></html>"""

def produce_blob(filename,wordlist, soup):
    index = 0
    #print(wordlist)
    if len(wordlist) == 7:
        columns = seven
    elif len(wordlist) == 8:
        columns = eight
    elif len(wordlist) == 9:
        columns = nine
    elif len(wordlist) == 10:
        columns = ten
    elif len(wordlist) == 11:
        columns = eleven
    elif len(wordlist) == 12:
        columns = twelve
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
    picture_and_destinations_table = soup.new_tag("table", id="pictures_and_destinations")
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
    back_button.string = "Back"
    img = soup.new_tag("img", src="../images/back_button.png")
    back_button.append(img)
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
    sound_button_image = soup.new_tag("img", src="../images/sound_button.png", id=str(wordlist[index]) + "_sound_button")
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
    soup = BeautifulSoup(header_starter,"html5lib")
    #produce_blob(name, wordlist, soup)
    #print(name)
    #print([x.decode("utf-8").replace(u'\u2019', "'") for x in wordlist])
    writefile(produce_blob(name, wordlist,soup))

#For matchingindex.html

print(matchingindexjson)

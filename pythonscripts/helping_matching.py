import csv


def produce_blob(filename,wordlist):
    index = 0
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
    blob = """<html>
    <head>
      <link rel="stylesheet" type="text/css" href="./../drag_n_drop_theme.css" />
    <link
    href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.css" rel="stylesheet">
    <link
    href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.2/css/lightness/jquery-ui-1.10.2.custom.min.css" rel="stylesheet">
    <link href="../sliders.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-1.7.2.min.js"></script>
    <script
    src="https://code.jquery.com/ui/1.8.21/jquery-ui.min.js"></script>
    <script src="../jquery.ui.touch-punch.min.js"></script>

    <link href="https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap" rel="stylesheet">
    <style>
    * {
        font-family: 'Didact Gothic', sans-serif;
        }
    #pictures_and_destinations {
      border: 1px;
      }

    #answers {
      width: 90vw;
    }
    #answers {
      text-align: center;
      border-style: dotted;
    }

    .image {
    margin: auto;
    }

    .image > img {
     margin: auto;
     height:15vh;
     border-style: solid;
    }
    .destination {
      border-style: dashed;
      text-align: center;
      padding: 10px;
      }

    </style>
    <script>
    function tapHandler(event){
        var audioId = event.target.id + "_audio";
        console.log(event.target.id);
        //alert(audioId);
        txtObj = document.getElementById(event.target.id);
        audioObj = document.getElementById(audioId);
        audioObj.addEventListener("ended", function(){
          txtObj.style.backgroundColor = "transparent";
        });
        txtObj.style.backgroundColor = "yellow";
        document.getElementById(audioId).play();
    }
    $(function() {
      var score = 0;
    window.words_remaining = 0;
      $(".source").on("dragstart", tapHandler );
      $( ".source" ).draggable({ revert: "invalid", scroll: false});
      $( ".destination" ).droppable({
        drop: function( event, ui ) {
          var dragged_category = ui.draggable.attr("name").split(",")[0];
          var dropped_category = $(this).attr("name").split(",")[0];
          if (ui.draggable.attr("name") == $(this).attr("name")){
              ui.draggable.draggable("disable");
              $(this).css({"background-color":"#70db70"});
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
            ui.draggable.css({"color":"red"});
            moves += 1;

        }

        }
      });
      var slidetoggleinteraction = document.getElementById("toggleinteraction");
      slidetoggleinteraction.addEventListener("click",function(){
        if (slidetoggleinteraction.checked == false){
          $( ".source" ).draggable("enable");
        }
        else {
          $(".source").on("click", tapHandler );
          $(".source").draggable("disable");
        }
      });
    });

        var score = 0;
        var moves = 0;
    </script>
    <title>"""
    blob += filename.replace(".html","")

    blob += """
    </title>
    </head>

    <body>
      <div id="header">
        <label class="switch">
         <input id="toggleinteraction" type="checkbox">
         <span class="slider round"></span>
       </label>
       <span id="toggleinteractiontext">Lock</span>
     </div>
    <table id="pictures_and_destinations">
    <tr>"""

    for row in columns:
        blob += '<tr>'
        for col in row:
            blob += '<td id="'+col+'">'
            blob += '<div class="image"><img src="imgs/'+ wordlist[index] + '.png"/></div>'
            blob += '<div class="destination" name="' + col[0] + ',' + col[1] + '" id="droppable"></div>'
            blob += '</td>'
            index += 1
        blob += '</tr>'
    blob += """</td>
    </tr>
    </table>
    <table id="answers">
    <tr>"""

    index = 0

    for row in columns:
        for col in row:
            blob += '<td id="'+col+'">'
            blob += '<div name="' + col[0] + ',' + col[1] + '" id="'+ wordlist[index] + '" class="source">'+ wordlist[index] + '</div>'
            blob += '<audio name="'+ col[0] + ',' + col[1] + '" id="'+ wordlist[index] + '_audio" src="../sounds/'+ wordlist[index] + '.mp3"></audio>'
            blob += '</td>'
            index += 1


    blob += """</tr>
    </table>



    </body>
    </html>"""

    #print(blob)
    return filename, blob

def writefile(blobtup):
    with open(blobtup[0] + ".html", "w") as fp:
        fp.write(blobtup[1])


fourcol = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a","3b","3c","3d"]]
threecol = [["1a","1b","1c"],["2a","2b","2c"],["3a","3b"]]
seven = [["1a","1b","1c"],["2a","2b","2c"],["3a"]]
eight = [["1a","1b","1c"],["2a","2b","2c"],["3a","3b"]]
nine = [["1a","1b","1c"],["2a","2b","2c"],["3a","3b","3c"]]
ten = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a"]]
eleven = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a","3b","3c"]]
twelve = [["1a","1b","1c","1d"],["2a","2b","2c","2d"],["3a","3b","3c","3d"]]

with open("../../AllMatching.csv","r") as fp:
    allmatching = fp.read().split("\n\n")

#print(allmatching)

for lesson in allmatching:
    lesson = filter(None,lesson.split("\n"))
    name = lesson.pop(0)
    wordlist = lesson
    #print(name)
    #print([x.decode("utf-8").replace(u'\u2019', "'") for x in wordlist])
    writefile(produce_blob(name, wordlist))

var i = 0;
var all_words = document.getElementsByClassName("source");

function finished_playing_list(event){
	console.log(event.target.id + "Finished");
	var txtObj = document.getElementById(event.target.id.replace("_audio",""));
        $(txtObj).toggleClass("playing");
	play_all_sounds(play_allsound_sounds);
}

function finished_playing(event){
	console.log(event.target.id + "Finished");
        var txtid = event.target.id.replace("_audio","");
	var txtObj = document.getElementById(txtid);
	$(txtObj).toggleClass("playing");
}

function play_sound(event){
    console.log(event.target.id);
    var audioId = event.target.id.replace("_sound_button","_audio");
    var audioObj = document.getElementById(audioId);
    var txtid = event.target.id.replace("_sound_button","")
    var txtObj = document.getElementById(txtid);
    $(txtObj).toggleClass("playing");
    $(audioObj).on("ended", finished_playing);
    audioObj.play();
}

function play_all_sounds(play_sound){
	if (i < all_words.length){
		var word = all_words[i].id;
		console.log(word);
		var next_word = word + "_audio";
		txtObj = document.getElementById(word);
		audioObj = document.getElementById(next_word);
		//audioObj.onended = finished_playing;
		$(audioObj).on("ended", finished_playing_list);
		$(txtObj).toggleClass("playing");
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
    $(txtObj).toggleClass("playing")
    audioObj.play();
};

function adjustColumns(){
    console.log($(".source").length);
};

function adjustOrientation(event){
    console.log(event.orientation);
};

$(function() {
  var score = 0;
  window.words_remaining = 0;
  //~ $(window).on("orientationchange", adjustOrientation);
  adjustColumns();
  window.setTimeout(function() {window.scrollTo(0,document.getElementById("header").offsetHeight)}, 2000);
  $("#back_button").on("click",function(){window.location = "../matchingindex.html";});
  $(".source").on("dragstart", tapHandler );
  $(".sound_button").on("click",play_sound);
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
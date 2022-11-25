window.onload=function() {
   var images = document.getElementsByTagName("img");
   for (var i=0;i<images.length; i++){
     images[i].onmouseover=showAnswer;
     images[i].onmouseout=reblur;
   }

   document.onclick=hideDetails;
 }

function showAnswer(eventObj) {
   var image = eventObj.target
   var name=image.id;
   name+=".jpg";
   image.src="static/img/"+name;
}

function reblur(eventObj) {
  var image=eventObj.target;
  var name=image.id;
  name+="blur.jpg";
  image.src="static/img/"+name;
}

function hideDetails() {
  var details = document.querySelector('details');
  details.open = false;
}

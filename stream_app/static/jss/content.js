// var randomLoc=Math.floor(Math.random()*5);
// var location1=randomLoc;
// var location2=location1+1;
// var location3=location2+1;
//
// var isSunk=false;
//
// var guess; //номер текущей попытки
// var hits=0; // кол-во попаданий
// var guesses=0; // кол-во попыток
//
//
// while(isSunk == false){
//   guess=prompt("Ready, Aim, Fire! (enter a number 0-6): ");
//   if (guess <0 || guess >6){
//     alert("Please enter valid cell number!");
//   } else{
//     guesses=guesses+1;
//     if (guess==location1 || guess==location2 || guess==location3 ){
//       hits=hits+1;
//       alert('HIT');
//       if (hits==3){
//         isSunk=true;
//         alert("You sank my battleship!");
//       }
//     }else{
//       alert("MISS");
//     }
//   }
// }
//
// var stats="You took " + guesses + " guesses to sink the battleship, " + "which means your shooting accuracy was " + (3/guesses);
// alert(stats);


var scores=[60,50,60,58,54,54,98,35,45,15,78,48,51,25,45,45,15,48,45,95,62,15,15,58,98];


function printAndGetHighScore(scores) {
  var output;
  var highScore = 0;

  for (var i=0; i<scores.length; i++){
    console.log("Bubble solution #" +i+ " score: " + scores[i]);
    if (scores[i]>highScore){
      highScore=scores[i];
    }
  }
  return highScore;
}


function getBestResults(scores,highScore) {
  var bestSolutions=[];

  for (var i=0; i<scores.length; i++){
    if(scores[i]==highScore){
      bestSolutions.push(i);
    }
  }
  return bestSolutions
}


var highScore=printAndGetHighScore(scores);
var bestSolutions=getBestResults(scores,highScore);


console.log("Highest bubble score: " + highScore);
console.log("Bubbles tests: " + scores.length);
console.log("Solutions with the highest score: "+bestSolutions);

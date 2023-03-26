var choiceHeading = document.querySelector("#choice-heading");
var pChoice = document.querySelector("#pchoice-display");
var comChoice = document.querySelector("#comchoice-display");
var result = document.querySelector("#result-display");

var winCount = document.querySelector("#win-count-display");
var loseCount = document.querySelector("#lose-count-display");
var tieCount = document.querySelector("#tie-count-display");

var rockButton = document.querySelector("#rock-button");
var paperButton = document.querySelector("#paper-button");
var scissorsButton = document.querySelector("#scissors-button");

var choice = "";

rockButton.onclick = function () {
	console.log("the rock button was clicked");
	pChoice.innerHTML = "ROCK" ;
	choice = "ROCK";
	console.log("choice = " + choice);
	var comChoice = play(choice);
	
	result.innerHTML = getWinner(choice, comChoice);
	console.log(result.innerHTML);
	var r = result.innerHTML;
	tally(r);
	addToPreviousGames(choice, comChoice, r);
}
	
paperButton.onclick = function () {
	console.log("the paper button was clicked");
	pChoice.innerHTML = "PAPER" ;
	choice = "PAPER";
	console.log("choice = " + choice);
	var comChoice = play(choice);
	
	result.innerHTML = getWinner(choice, comChoice);
	console.log(result.innerHTML);
	var r = result.innerHTML;
	tally(r);
	addToPreviousGames(choice, comChoice, r);
}

scissorsButton.onclick = function () {
	console.log("the scissors button was clicked");
	pChoice.innerHTML = "SCISSORS" ;
	choice = "SCISSORS";
	console.log("choice = " + choice);
	var comChoice = play(choice);
	
	result.innerHTML = getWinner(choice, comChoice);
	console.log(result.innerHTML);
	var r = result.innerHTML;
	tally(r);
	addToPreviousGames(choice, comChoice, r);
}


function play(choice) {
	var randomIndex = Math.floor(Math.random() * 3);
	var comChoice = choices[randomIndex];
	var comChoiceDiv = document.querySelector("#comchoice-display");
	comChoiceDiv.innerHTML = comChoice;
	return comChoice;
}

var winner = "?";

function getWinner(choice1, choice2) {
	if (choice1 == "ROCK" && choice2 == "ROCK") {
		winner = "It's a tie!";
	} else if (choice1 == "ROCK" && choice2 == "PAPER") {
		winner = "You lose!";
	} else if (choice1 == "ROCK" && choice2 == "SCISSORS") {
		winner = "You win!";
		
	} else if (choice1 == "PAPER" && choice2 == "ROCK") {
		winner = "You win!";
	} else if (choice1 == "PAPER" && choice2 == "PAPER") {
		winner = "It's a tie!";
	} else if (choice1 == "PAPER" && choice2 == "SCISSORS") {
		winner = "You lose!";
		
	} else if (choice1 == "SCISSORS" && choice2 == "ROCK") {
		winner = "You lose!";
	} else if (choice1 == "SCISSORS" && choice2 == "PAPER") {
		winner = "You win!";
	} else if (choice1 == "SCISSORS" && choice2 == "SCISSORS") {
		winner = "It's a tie!";
	} else {
		winner = "error";
	}
	return winner;
}

var wins = 0;
var losses = 0;
var ties = 0;

var rDisplay = document.querySelector("#results");
var winLossTieDisplay = document.querySelector("#tally");
var red = "#FF0000";
var green = "#00FF00";
var white = "#FFFFFF";

function tally(result) {
	if (result == "You win!") {
		wins += 1;
		console.log(wins);
		winCount.innerHTML = wins;
		colorChange(rDisplay, green);
	} else if (result == "You lose!") {
		losses += 1;
		loseCount.innerHTML = losses;
		colorChange(rDisplay, red);
	} else {
		ties += 1;
		tieCount.innerHTML = ties;
		colorChange(rDisplay, white);
	}
	// compare wins to losses and change color
	if (wins > losses) {
		colorChange(winLossTieDisplay, green);
	} else if (wins < losses) {
		colorChange(winLossTieDisplay, red);
	} else if (wins == losses){
		colorChange(winLossTieDisplay, white);
	} else {
		console.log("color change error");
	}
}

function addToPreviousGames (result1, result2, result) {
	var pGamesList = document.querySelector("#previous-games-list");
	var newItem = document.createElement("li");
	newItem.innerHTML = result1 + " vs " + result2 + ": "  + result;
	pGamesList.appendChild(newItem);
}


function colorChange (target, color) {
	target.style.borderColor = color;
	// console.log("color change target: ", target);
}


// var choices = ["ROCK", "PAPER", "SCISSORS"];
var choices = [];

fetch("https://api.jsonbin.io/v3/b/63cee22aebd26539d0661b6f").then(function (response) {
	response.json().then(function (data) {
		console.log("data received from server: ", data);
		choices = data["record"];
	})
})
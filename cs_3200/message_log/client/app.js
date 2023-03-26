var myButton = document.querySelector("#add-game-button");
console.log("#button 1", myButton);

myButton.onclick = function () {
	console.log("the button was clicked");
	
	var gameNameInput = document.querySelector("#game-name");
	console.log("my input element:", gameNameInput);
	console.log("input element text:", gameNameInput.value);
	
	createGameOnServer(gameNameInput.value);
	
	gameNameInput.value = "";
};

var input = document.getElementById("game-name");
input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("add-game-button").click();
    }
});
	
var myGames = [];

var randomButton = document.querySelector("#random-game-button");
console.log("random button query", randomButton);

randomButton.onclick = function () {
	console.log("the random button was clicked");
	
	// random index to pick a game (0 to length of games)
	var randomIndex = Math.floor(Math.random() * myGames.length);
	// index my array of games: variable with the string
	var randomName = myGames[randomIndex];
	// query the span
	var randomNameSpan = document.querySelector("#random-game-name");
	// assign innerHTML of the span to be the game name string
	randomNameSpan.innerHTML = randomName;
};


function loadGamesFromServer () {

    fetch("http://localhost:8080/games").then(function (response) {
    	response.json().then(function (data) {
    		console.log("data received from server: ", data);
    		// myGames = [];
    		myGames = data;
    		
    		var gamesList = document.querySelector("#my-game-list");
    	    console.log("#my Games element:", myGames);
    	    gamesList.innerHTML = "";
    	    
    		
    		// for game in myGames
    		myGames.forEach(function (game) {
    		    console.log(game);
    		    var newItem = document.createElement("li");
                
                var nameDiv = document.createElement("div");
                nameDiv.innerHTML = game;
                nameDiv.classList.add("game-name");
                newItem.appendChild(nameDiv);
                
    	        // newItem.innerHTML = gamNameInput.value;
    	        gamesList.appendChild(newItem);
    		});
    	});
    });    
};

function createGameOnServer (gameName) {
    console.log("Attempting to create game", gameName, "on server");
    
    var data = "name=" + encodeURIComponent(gameName);
    console.log("Sending data to server", data);
    
    fetch("http://localhost:8080/games", {
        // request details
        method: "POST",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
    }).then(function (response) {
        // when the server responds:
        if (response.status == 201) {
            loadGamesFromServer();
        } else {
            console.log("server responded with", response.status, "when trying to create a game");
        };
        
    });
};

loadGamesFromServer();
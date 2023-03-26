console.log("Hello world");

var x = 5;

// tag selector, can be more than 1, returns first one it finds
// var h1element = document.querySelector("h1");

// class selector, .some-class

// id selector is better, #some-id
var h1element = document.querySelector("#my-heading");
console.log("#my h1 element", h1element);



// button
var myButton = document.querySelector("#add-friend-button");
console.log("#button 1", myButton);
myButton.onclick = function () {
	console.log("the button was clicked");
	// h1element.innerHTML = "I'm different now.";
	// // can assign any css style this way
	// h1element.style.color = "#FF0000";
	// // change hyphens to camelCase
	// h1element.style.backgroundColor = "#0000FF";
	
	var friendNameInput = document.querySelector("#friend-name");
	console.log("my input element", friendNameInput);
	console.log("input element text", friendNameInput.value);
	
	var myList = document.querySelector("#my-friend-list");
	console.log("#my list element", myList);
	
	var newItem = document.createElement("li");
	newItem.innerHTML = friendNameInput.value;
	myList.appendChild(newItem);
	friendNameInput.value = "";
	
	// keydown event for enter key look it up
	
// var myArray = ["apple", "banana", "cherry"];
// 
// var myObject = {"name": "apple", "color": "red"};
// 
// var myFriends = [{
	// "name": "Joe",
	// "hometown": "Atlanta",
	// "hobby": "tennis"
// }, {
	// "name": "Steve",
	// "hometown": "SLC",
	// "hobby": "acting"
// }]
};
	
var myFriends = ["Joe", "Steve", "Bob", "John"];	

var randomButton = document.querySelector("#random-friend-button");
console.log("random button query", randomButton);

randomButton.onclick = function () {
	console.log("the random button was clicked");
	
	// random index to pick a friend (0 to length of friends)
	var randomIndex = Math.floor(Math.random() * myFriends.length);
	// index my array of friends: variable with the string
	var randomName = myFriends[randomIndex];
	// query the span
	var randomNameSpan = document.querySelector("#random-friend-name");
	// assign innerHTML of the span to be the friend name string
	randomNameSpan.innerHTML = randomName;
};








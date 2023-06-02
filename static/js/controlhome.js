const user_input = document.getElementById('search-textbox').value;
// redirect by changing link address of webpage
window.location.replace(window.location.href + user_input)  //+ 'user input' --> query for flask application
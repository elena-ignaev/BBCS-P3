const user_input = document.getElementById('search-textbox').value;
const pic1 = document.getElementById('pic1');
const loc1 = document.getElementById('loc1');
const des1 = document.getElementById('des1');
function search() {
    // redirect by changing link address of webpage
    window.location.replace(window.location.href)  //+ 'user input' --> query for flask application
    // somehow receive data from python
    // edit html file
    pic1.src = "";
    loc1
    // elements: search-textbox, search-button, pic1, pic2, pic3, loc1, loc2, loc3, des1, des2, des3
}


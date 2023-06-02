const user_input = document.getElementById('search-textbox').value;

const pic1 = document.getElementById('pic1');
const loc1 = document.getElementById('loc1');
const des1 = document.getElementById('des1');

const pic2 = document.getElementById('pic2');
const loc2 = document.getElementById('loc2');
const des2 = document.getElementById('des2');

const pic3 = document.getElementById('pic3');
const loc3 = document.getElementById('loc3');
const des3 = document.getElementById('des3');
function search() {
    // redirect by changing link address of webpage
    window.location.replace(window.location.href + "suggestions")  //+ 'user input' --> query for flask application
    // edit html file, text content wait for model 2 to be completed
    pic1.src = 'static/locationpictures/img1';
    loc1.textContent = "";
    des1.textContent = "";

    pic2.src = 'static/locationpictures/img2';
    loc2.textContent = "";
    des2.textContent = "";

    pic3.src = 'static/locationpictures/img3';
    loc3.textContent = "";
    des3.textContent = "";
}


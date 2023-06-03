const loc1 = document.getElementById('loc1');
const des1 = document.getElementById('des1');

const loc2 = document.getElementById('loc2');
const des2 = document.getElementById('des2');

const loc3 = document.getElementById('loc3');
const des3 = document.getElementById('des3');

// edit html file, text content wait for model 2 to be completed
/*loc1.textContent = "";
des1.textContent = "";

loc2.textContent = "";
des2.textContent = "";

loc3.textContent = "";
des3.textContent = "";*/
document.getElementById("search-button").onclick = function () {
    // redirect by changing link address of webpage
    window.location.href = "/suggestions?query="+document.getElementById("search-textbox").value;  //+ 'user input' --> query for flask application
    // edit html file, text content wait for model 2 to be completed
    /*loc1.textContent = "";
    des1.textContent = "";

    loc2.textContent = "";
    des2.textContent = "";

    loc3.textContent = "";
    des3.textContent = "";*/
}
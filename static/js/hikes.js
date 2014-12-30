function toggleDisplay(myId){
    var toToggle = document.getElementById(myId);
    if (toToggle.style.display == 'block'){
        toToggle.style.display = 'none';
    }
    else{
        toToggle.style.display = 'block';
    }
}
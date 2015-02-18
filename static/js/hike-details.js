(function (){

    var ajaxRequest;

    function initSave() {
//      set up AJAX request
        ajaxRequest = getXmlHttpObject();
        if (ajaxRequest == null) {
            alert("This browser does not support HTTP Request");
            return;
        }

 //      grab form elements and call the save function
        var saveButton = document.getElementById("save");
        saveButton.onclick = function () {
            var formDataList = [];
            var name = document.getElementById("hike");
            var difficulty = document.getElementById("diff_exp_form");
            var description = document.getElementById("add_descrip_form");
            formDataList.push("name=" + encodeURIComponent(name.value));
            formDataList.push("difficulty=" + encodeURIComponent(difficulty.value));
            formDataList.push("description=" + encodeURIComponent(description.value));
            console.log("variables initialized");
            saveForm(formDataList.join("&"));
            }

    }

    function saveForm(formData){
//      stuff here to POST
//      send form data to django database then call the state change test function
        console.log("saveForm called");
        ajaxRequest.open("POST","/hikes/hikesajax",true);
        ajaxRequest.onload = fetch;
        ajaxRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        ajaxRequest.send(formData);

    }

    function fetch() {
        console.log('fetch called');
        ajaxRequest.onload = undefined;
        ajaxRequest.onreadystatechange = stateChanged();
        ajaxRequest.open("GET", "/hikes/hikesajax", true);
        ajaxRequest.send();
    }


    function refreshDetails(data) {
//     callback function
//     print form inputs back to the page
        console.log("callback function");
        var descripResults = document.getElementById("hike_descrp");
        var diffResults = document.getElementById("diff_exp");

        descripResults.innerHTML = data;
    }


    function getXmlHttpObject() {
//      test browser and build XHR object

        if (window.XMLHttpRequest) {
            return new XMLHttpRequest();
        }
        if (window.ActiveXObject) {
            return new ActiveXObject("Microsoft.XMLHTTP");
        }
        return null;
    }

   function stateChanged() {
//      test ajax state and call callback function
        console.log('statechanged called');
        if (ajaxRequest.readyState == 4) {
            //use the info here that was returned
            if (ajaxRequest.status == 200) {
                var data = JSON.parse(ajaxRequest.responseText);
                refreshDetails(data);
            }
        }
    }

    initSave();
})();
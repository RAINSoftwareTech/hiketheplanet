(function() {
    var ajaxRequest,
        searchType;

    function initSearch() {
        // set up AJAX request
        ajaxRequest = getXmlHttpObject();
        if (ajaxRequest == null) {
            alert("This browser does not support HTTP Request");
            return;
        }
        var searchField1 = document.getElementById("hike_search");
        searchField1.onkeyup = function () {
            searchType = 'hike';
            searchRequest(searchField1, '');
            };

        var searchButton = document.getElementById("distance_search");
        searchButton.onclick = function () {
            searchType = 'miles';
            var searchField1 = document.getElementById("miles_search");
            var searchField2 = document.getElementById("zip_search");
            searchRequest(searchField1, searchField2);
            }

    }

    function getXmlHttpObject() {
        if (window.XMLHttpRequest) {
            return new XMLHttpRequest();
        }
        if (window.ActiveXObject) {
            return new ActiveXObject("Microsoft.XMLHTTP");
        }
        return null;
    }

    function searchRequest(searchField1, searchField2) {
//    console.log('keyup');
//    console.log(searchField);
        var search,
            search_text;
        if(searchType === 'hike') {
            search_text = searchField1.value;
            search = '/search/?search_text=' + encodeURI(search_text);
        }

        if(searchType === 'miles'){
            search_text = searchField1.value.concat('_', searchField2.value);
            search = '/search/distance/?search_text=' + encodeURI(search_text);
        }



        ajaxRequest.open('GET', search, true);
        ajaxRequest.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        ajaxRequest.send(search_text);
        ajaxRequest.onreadystatechange = stateChanged;
    }

    function stateChanged() {
        if (ajaxRequest.readyState == 4) {
            //use the info here that was returned
            console.log('ready state 4');
            if (ajaxRequest.status == 200) {
                console.log('status 200', ajaxRequest.responseText);
                var data = JSON.parse(ajaxRequest.responseText);
                if(searchType === 'hike') {
                    byNameResults(data);
                }
                if(searchType === 'miles') {
                    byDistanceResults(data);
                }
            }
        }
    }

    function byNameResults(data){
        var results,
            url,
            name,
            distance,
            difficulty,
            text;
        var output = [];
        results = document.getElementById("search-results");
        for(var i=0; i<data.length; i++) {
            url = data[i].hikeUrl;
            name = data[i].hike;
            distance = " | Length: " + data[i].distance;
            difficulty = " miles | Difficulty: " + data[i].difficulty;
            text = '<a href="' + url + '">'
                + name + '</a> ' + distance + difficulty;
            output.push(text);
        }
        results.innerHTML = "<li>" + output.join("</li><li>") + "</li>";

    }


    function byDistanceResults(data){
        var results,
            url,
            name,
            miles,
            difficulty,
            length,
            text;
        var output = [];
        results = document.getElementById("distance-results");
        for(var i=0; i<data.length; i++) {
            url = data[i].hike_url;
            name = data[i].hike;
            miles = " | Driving Miles: " + data[i].distance;
            difficulty = " miles | Difficulty: " + data[i].difficulty;
            length = " | Length " + data[i].length + ' miles';
            text = '<a href="' + url + '">'
                + name + '</a> ' + miles + difficulty + length;
            output.push(text);
        }
        console.log(ajaxRequest.responseText);
        results.innerHTML = "<li>" + output.join("</li><li>") + "</li>";

    }

    initSearch();
})();

//
//set header


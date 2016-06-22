    var map;
    var ajaxRequest;
    var plotlist;
    var plotlayers = [];

    function initmap() {
        // set up AJAX request
        ajaxRequest = getXmlHttpObject();
        if (ajaxRequest == null) {
            alert("This browser does not support HTTP Request");
            return;
        }

        // set up the map
        map = new L.Map('map');

        // create the tile layer with correct attribution
        var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        var osmAttrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
        var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 12, attribution: osmAttrib});

        // start the map
        map.setView(new L.LatLng(45.51830, -122.67600), 9);
        map.addLayer(osm);

    }

//mapModal.on('shown.bs.modal', function(){
//    setTimeout(function() {
//        map.invalidateSize();
//   }, 1);
//});

    function getXmlHttpObject() {
        if (window.XMLHttpRequest) {
            return new XMLHttpRequest();
        }
        if (window.ActiveXObject) {
            return new ActiveXObject("Microsoft.XMLHTTP");
        }
        return null;
    }

    function askForPlots(searchUrl) {
        // request the marker info with AJAX for the current bounds
        var bounds = map.getBounds();
        var minll = bounds.getSouthWest();
        var maxll = bounds.getNorthEast();
        ajaxRequest.onreadystatechange = stateChanged;
        ajaxRequest.open('GET', searchUrl, true);
        ajaxRequest.send(null);
    }

    function stateChanged() {
        var bounds = [];
        // if AJAX returned a list of markers, add them to the map
        if (ajaxRequest.readyState == 4) {
            //use the info here that was returned
            if (ajaxRequest.status == 200) {
                plotlist = eval("(" + ajaxRequest.responseText + ")");
                removeMarkers();
                for (var i = 0; i < plotlist.length; i++) {
                    var plotll = new L.LatLng(plotlist[i].lat, plotlist[i].lon, true);
                    bounds[bounds.length] = plotll;
                    var plotmark = new L.Marker(plotll);
                    plotmark.data = plotlist[i];
                    map.addLayer(plotmark);
                    plotmark.bindPopup("<a href='"
                        + plotlist[i].url + "'><h4>"
                        + plotlist[i].trailhead
                        + "</a></h4>Hikes starting here: "
                        + plotlist[i].num_hikes);
                    plotlayers.push(plotmark);
                }
                map.fitBounds(bounds)
            }
        }
    }

    function removeMarkers() {
        for (i = 0; i < plotlayers.length; i++) {
            map.removeLayer(plotlayers[i]);
        }
        plotlayers = [];
    }




// leaflet / mapquest code to produce directions.
window.onload = function() {
    var mapLayer = MQ.mapLayer();

    var map = L.map('map', {
        layers: mapLayer,
        center: [ 40.731701, -73.993411 ],
        minZoom: 8,
        maxZoom: 12,
        attribution: 'Map data &copy; <a href="http://www.mapquest.com/" target="_blank">MapQuest</a>'
    });

    L.control.layers({
        'Map': mapLayer,
        'Satellite': MQ.satelliteLayer(),
        'Hybrid': MQ.hybridLayer()
    }).addTo(map);
}


mapModal.on('shown.bs.modal', function(){
    setTimeout(function() {
        map.invalidateSize();
   }, 1);
});


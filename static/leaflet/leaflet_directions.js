// leaflet / mapquest code to produce directions.
var latitude;
var longitude;
var startingZip;


$('#mapModal').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget); // Button that triggered the modal
      latitude = button.data('lat'); // Extract info from data-* attributes
      longitude = button.data('lon');
      startingZip = button.data('hiker-location')

});

$('#mapModal').on('shown.bs.modal', function() {
        var map,
            dir;
        var mapLayer = MQ.mapLayer();
//        var latitude = 45.63621;
//        var longitude = -121.74248;
//        var startingZip = "97219";

        map = L.map('map', {
            layers: mapLayer,
            center: [ latitude, longitude ],
            zoom: 9,
            minZoom: 8,
            maxZoom: 12,
            attribution: 'Map data &copy; <a href="http://www.mapquest.com/" target="_blank">MapQuest</a>'
        });

        L.control.layers({
            'Map': mapLayer,
            'Satellite': MQ.satelliteLayer(),
            'Hybrid': MQ.hybridLayer()
        }).addTo(map);

        dir = MQ.routing.directions()
            .on('success', function(data) {
                var legs = data.route.legs,
                    html = '',
                    maneuvers,
                    i;

                if (legs && legs.length) {
                    maneuvers = legs[0].maneuvers;

                    for (i=0; i<maneuvers.length; i++) {
                        html += (i+1) + '. ';
                        html += maneuvers[i].narrative + '<br />';
                    }

                    L.DomUtil.get('route-narrative').innerHTML = html;
                }
            });

        dir.route({
            locations: [
                { postalCode: startingZip },
                { latLng: { lat: latitude, lng: longitude } }
               ]
        });

        map.addLayer(MQ.routing.routeLayer({
            directions: dir,
            fitBounds: true
        }));
    });

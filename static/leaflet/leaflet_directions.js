// leaflet / mapquest code to produce directions.

    $('#mapModal').on('shown.bs.modal', function() {
            var map,
                dir;
            var mapLayer = MQ.mapLayer();

            map = L.map('map', {
                layers: mapLayer,
                center: [ 40.045049, -105.961737 ],
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
                    '80217',
                    'steamboat springs co'
                ]
            });

            map.addLayer(MQ.routing.routeLayer({
                directions: dir,
                fitBounds: true
            }));
        });


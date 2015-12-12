/**
 * Skrypty do obsługi google maps API
 *
 * @author Adrian Michalik
 */
var polandLatLng = {lat: 51.919438, lng: 19.145135999};
var clickedLat = 0.0;
var clickedLng = 0.0;

function initMapCenter(position) {
    var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    var map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        scrollwheel: true,
        zoom: 10
    });
    google.maps.event.addListener(map, 'click', getCoords(event));
    createMarker(map, latlng, "Twoje położenie");
}

function getCoords(event) {
    clickedLat = event.latLng.lat();
    clickedLng = event.latLng.lng();
}

function initMapPoland() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: polandLatLng,
        scrollwheel: true,
        zoom: 6
    });
    google.maps.event.addListener(map, 'click', getCoords(event));
}

function createMarker(map, latlng, markerTitle) {
    var marker = new google.maps.Marker({
        map: map,
        position: latlng,
        title: markerTitle
    });
}

function addEventListenerToMarker(marker) {
    google.maps.event.addListener(marker, "click", function (event) {
        var latitude = event.latLng.lat();
        var longitude = event.latLng.lng();
        console.log( latitude + ', ' + longitude );

        radius = new google.maps.Circle({map: map,
            radius: 100,
            center: event.latLng,
            fillColor: '#777',
            fillOpacity: 0.1,
            strokeColor: '#AA0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            draggable: true,
            editable: true
        });
    });
}

$(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(initMapCenter)
    } else {
        initMapPoland();
    }
});
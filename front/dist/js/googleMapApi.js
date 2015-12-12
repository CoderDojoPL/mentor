/**
 * Skrypty do obsługi google maps API
 *
 * @author Adrian Michalik
 */
var polandLatLng = {lat: 51.919438, lng: 19.145135999};
var clickedLat = 0.0;
var clickedLng = 0.0;

function initMapCenter(userLat, userLng) {
    var centerLatLgn = {lat: userLat, lng: userLng};

    var map = new google.maps.Map(document.getElementById('map'), {
        center: centerLatLgn,
        scrollwheel: true,
        zoom: 4
    });
    google.maps.event.addListener(map, 'click', getCoords(event));
}

function getCoords(event) {
    clickedLat = event.latLng.lat();
    clickedLng = event.latLng.lng();
}

function initMapPoland() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: polandLatLng,
        scrollwheel: true,
        zoom: 4
    });
    google.maps.event.addListener(map, 'click', getCoords(event));
}

function createMarker(map, lat, lng) {
    var latLng = {lat: lat, lng: lng};
    var marker = new google.maps.Marker({
        map: map,
        position: latLng,
        title: 'CoderDojo Mentors'
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
            draggable: true,    // Dragable
            editable: true
        });
    });
}

$(function() {
/*    if (position.coords.latitude && position.coords.longitude) {
        initMapCenter(position.coords.latitude, position.coords.longitude);
    } else {*/
        initMapPoland();
/*    }*/
});
/**
 * Skrypty do obsługi google maps API
 *
 * @author Adrian Michalik
 */
var polandLatLng = {lat: 51.919438, lng: 19.145135999};
var clickedLat = 0.0;
var clickedLng = 0.0;
var map;

function initMapCenter(position) {
    var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    console.log(latlng);
    map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        scrollwheel: true,
        zoom: 10
    });
    createMarkerYourPosition(position);
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

function createMarkerYourPosition(position) {
    var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    var marker = new google.maps.Marker({
        setMap: map,
        position: latlng,
        title: 'Twoje położenie'
    });
}

$(function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(initMapCenter);
    } else {
        initMapPoland();
    }
});
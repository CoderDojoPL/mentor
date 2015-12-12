/**
 * Skrypty do obsługi google maps API
 *
 * @author Adrian Michalik
 */
var polandLatLng = {lat: 51.919438, lng: 19.145135999};

function initMapCenter(userLat, userLng) {
    var centerLatLgn = {lat: userLat, lng: userLng};

    var map = new google.maps.Map(document.getElementById('map'), {
        center: centerLatLgn,
        scrollwheel: true,
        zoom: 4
    });
}

function initMapPoland() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: polandLatLng,
        scrollwheel: true,
        zoom: 4
    });
}

function createMarker(map, lat, lng) {
    var latLng = {lat: lat, lng: lng};
    var marker = new google.maps.Marker({
        map: map,
        position: latLng,
        title: 'CoderDojo Mentors'
    });
}
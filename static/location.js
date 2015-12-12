
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
}
function showPosition(position) {

    $.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=" +position.coords.latitude + "," + position.coords.longitude + "&sensor=true,callback",
        function(results){
            console.log(results);
            c = getCountry(results.results[0].address_components);
            if(c){
                console.log(c);
                s = 'Jak podoba Ci się podoba ' + c + ' ?';
                $('#text').text(s);
            } else {
                console.log('unnamed address');
            }
        }
    );
}
function getCountry(addrComponents) {
    for (var i = 0; i < addrComponents.length; i++) {
        if (addrComponents[i].types[0] == "country") {
            return addrComponents[i].long_name;
        }
        if (addrComponents[i].types.length == 2) {
            if (addrComponents[i].types[0] == "political") {
                return addrComponents[i].long_name;
            }
        }
    }
    return false;
}



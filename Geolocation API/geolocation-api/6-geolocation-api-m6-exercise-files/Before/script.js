/* eslint-disable no-alert */
/* eslint-disable prefer-destructuring */
/* eslint-disable func-names */
let map;
let infoWindow;
const markers = [];

function createMarker(latLng) {
    const markerOptions = {
        position: latLng,
        map,
        clickable: true,
    };

    const marker = new window.google.maps.Marker(markerOptions);
    markers.push(marker);

    window.google.maps.event.addListener(marker, 'click', function(event) {
        infoWindow.setContent(
            `Location: ${event.latLng
                .lat()
                .toFixed(2)}, ${event.latLng.lng().toFixed(2)}`
        );
        infoWindow.open(map, marker);
    });
}

function showMap(coords) {
    const googleLatLong = new window.google.maps.LatLng(
        coords.latitude,
        coords.longitude
    );
    const mapOptions = {
        zoom: 11,
        center: googleLatLong,
        mapTypeId: window.google.maps.MapTypeId.ROADMAP,
    };

    const mapDiv = document.getElementById('map');
    map = new window.google.maps.Map(mapDiv, mapOptions);
    infoWindow = new window.google.maps.InfoWindow();

    window.google.maps.event.addListener(map, 'click', function(event) {
        const latitude = event.latLng.lat();
        const longitude = event.latLng.lng();

        const pLocation = document.getElementById('location');
        pLocation.innerHTML = `${latitude}, ${longitude}`;
        map.panTo(event.latLng);

        createMarker(event.latLng);
    });
}

function displayLocation(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    const pLocation = document.getElementById('location');
    pLocation.innerHTML = `${latitude}, ${longitude}`;

    showMap(position.coords);
}

function displayError(error) {
    const errors = [
        'Unknown error',
        'Permission denied by user',
        'Position not available',
        'Timeout error',
    ];
    const message = errors[error.code];
    console.warn(`Error in getting your location: ${message}`, error.message);
}

window.onload = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(displayLocation, displayError);
    } else {
        alert("Sorry, this browser doesn't support geolocation!");
    }
};

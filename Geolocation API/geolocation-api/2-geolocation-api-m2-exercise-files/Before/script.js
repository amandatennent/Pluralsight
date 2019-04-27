/* eslint-disable prefer-destructuring */
/* eslint-disable no-alert */

function displayLocation(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    const pLocation = document.getElementById('location');
    pLocation.innerHTML += `${latitude}, ${longitude}<br>`;
}

function displayError(error) {
    const pLocation = document.getElementById('location');
    pLocation.innerHTML += `Error message = ${error.message}`;
}

window.onload = function getStuff() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(displayLocation, displayError);
    } else {
        alert("Sorry, this browser doesn't support geolocation!");
    }
};

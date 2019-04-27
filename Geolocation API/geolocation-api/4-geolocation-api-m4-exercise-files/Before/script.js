/* eslint-disable no-alert */
/* eslint-disable func-names */
/* eslint-disable prefer-destructuring */
function displayLocation(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    const pLocation = document.getElementById('location');
    pLocation.innerHTML += `${latitude}, ${longitude}<br>`;

    const pInfo = document.getElementById('info');
    const date = new Date(position.timestamp);
    pInfo.innerHTML = `Location timestamp: ${date}<br>`;
    pInfo.innerHTML += `Accuracy of location: ${
        position.coords.accuracy
    } meters<br>`;

    if (position.coords.altitude) {
        pInfo.innerHTML += `Altitude: ${position.coords.altitude}`;
    } else {
        console.info('No altitude');
    }

    if (position.coords.altitudeAccuracy) {
        pInfo.innerHTML += ` with accuracy ${
            position.coords.altitudeAccuracy
        }???`;
    } else {
        console.info('No Altitude Accuracy');
    }
    pInfo.innerHTML += '<br>';

    if (position.coords.heading) {
        pInfo.innerHTML += `Heading: ${position.coords.heading}<br>`;
    } else {
        console.info('No heading');
    }

    if (position.coords.speed) {
        pInfo.innerHTML += `Speed: ${position.coords.speed}<br>`;
    } else {
        console.info('No Speed');
    }
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
        navigator.geolocation.getCurrentPosition(
            displayLocation,
            displayError,
            { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 }
        );
    } else {
        alert("Sorry, this browser doesn't support geolocation!");
    }
};

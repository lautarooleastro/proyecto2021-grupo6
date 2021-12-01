import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = document.getElementById('lat').getAttribute('value');
const initialLng = document.getElementById('lng').getAttribute('value');

const submitHandler = (event, map) => {
    if (!map.marker) {
        event.preventDefault();
        alert("Debe seleccionar un punto en el mapa.");
    } else {
        var latlng = map.marker.getLatLng();
        document.getElementById('lat').setAttribute('value', latlng.lat);
        document.getElementById('lng').setAttribute('value', latlng.lng);
    }
}

window.onload = () => {
    const map = new MapSingleMarker({
        selector: 'map',
        lat: initialLat,
        lng: initialLng,
        addSearch: true
    });

    const form = document.getElementById('edit-meeting-point-form');

    form.addEventListener('submit', (event) => submitHandler(event, map));
}

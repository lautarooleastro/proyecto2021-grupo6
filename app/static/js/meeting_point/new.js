import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

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
        addSearch: true,
        enableEdit: true
    });

    const form = document.getElementById('create-meeting-point-form');

    form.addEventListener('submit', (event) => submitHandler(event, map));
}

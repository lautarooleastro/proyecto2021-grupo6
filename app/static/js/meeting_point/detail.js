import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = document.getElementById('lat').getAttribute('value');
const initialLng = document.getElementById('lng').getAttribute('value');

window.onload = () => {

    const lat = document.querySelector('#lat').value;
    const lng = document.querySelector('#lng').value;

    const map = new MapSingleMarker({
        selector: 'map',
        lat: lat,
        lng: lng,
        addSearch: false,
        enableEdit: false
    });
}
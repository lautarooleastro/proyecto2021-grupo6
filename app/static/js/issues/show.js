import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = document.getElementById('latitude').getAttribute('value');
const initialLng = document.getElementById('longitude').getAttribute('value');

window.onload = () => {

    const lat = document.querySelector('#latitude').value;
    const lng = document.querySelector('#longitude').value;

    const map = new MapSingleMarker({
        selector: 'map',
        lat: lat,
        lng: lng,
        addSearch: false,
        enableEdit: false
    });
}
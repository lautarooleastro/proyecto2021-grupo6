import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = document.getElementById('latitude').getAttribute('value');
const initialLng = document.getElementById('longitude').getAttribute('value');

const submitHandler = (event, map) => {
    if (!map.marker) {
        event.preventDefault();
        alert("Debe seleccionar un punto en el mapa.");
    } else {
        var latlng = map.marker.getLatLng();
        document.getElementById('latitude').disabled=false;
        document.getElementById('longitude').disabled=false;
        document.getElementById('latitude').setAttribute('value', latlng.lat);
        document.getElementById('longitude').setAttribute('value', latlng.lng);
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

    document.getElementById('latitude').disabled=true;
    document.getElementById('longitude').disabled=true;

    const form = document.getElementById('edit_issue');

    form.addEventListener('submit', (event) => submitHandler(event, map));
}

import { MapSingleMarker } from "../MapSingleMarker.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

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

    document.getElementById('latitude').setAttribute('value', initialLat);
    document.getElementById('longitude').setAttribute('value', initialLng);
    document.getElementById('latitude').disabled=true;
    document.getElementById('longitude').disabled=true;

    const form = document.getElementById('nueva-denuncia');

    form.addEventListener('submit', (event) => submitHandler(event, map));
}

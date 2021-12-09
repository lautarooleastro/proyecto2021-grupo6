import { MapZone } from "../MapZone.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;
/*
const submitHandler = (event, map) => {
    event.preventDefault();
    //if (!map.hasValidZone()) {
    if (false) {
        alert('Debes dibujar una zona en el mapa con al menos 3 puntos');
    } else {
        const code = document.querySelector('#code').value;
        const name = document.querySelector('#name').value;
        const color = document.querySelector('#color').value;
        const status = document.querySelector('#status').value;
        const puntos = map.drawnLayers[0].getLatLngs().map(coordinate => {
            return { latitude: coordinate.lat, longitude: coordinate.lng }
        });

        var formData = new FormData();
        formData.append('code', code);
        formData.append('name', name);
        formData.append('color', color);
        formData.append('status', status);
        formData.append('puntos', JSON.stringify(puntos));

        fetch('/zonas_inundables/add', {
            method: 'POST',
            body: formData
        }).then((response) => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        });
    }
    */
}

window.onload = () => {
    const map = new MapZone({
        selector: 'map',
        lat: initialLat,
        lng: initialLng
    });
    /*
    const form = document.querySelector('#nueva-zona');
    form.addEventListener('submit', (event) => submitHandler(event, map));
    */
}
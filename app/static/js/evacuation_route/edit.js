import { MapPath } from "../MapPath.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

const submitHandler = (event, map) => {
    event.preventDefault();

    if (!map.hasValidZone()) {
        alert('Debes dibujar una zona en el mapa con al menos 3 puntos');
    } else {
        const name = document.querySelector('#name').value;
        const description = document.querySelector('#description').value;
        const coordinates = map.drawnLayers[0].getLatLngs().map(coordinate => {
            return { lat: coordinate.lat, lng: coordinate.lng }
        });
        console.log(JSON.stringify(coordinates));

        var formData = new FormData();
        formData.append('name', name);
        formData.append('description', description);
        formData.append('coordinates', JSON.stringify(coordinates));

        fetch('/recorrido_de_evacuacion/crear', {
            method: 'POST',
            body: formData
        }).then();
    }
}

window.onload = () => {
    const map = new MapPath({
        selector: 'map',
        lat: initialLat,
        lng: initialLng
    });

    const form = document.querySelector('#create-evacuation-route-form');
    form.addEventListener('submit', (event) => submitHandler(event, map));
}
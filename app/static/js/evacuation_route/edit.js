import { MapPath } from "../MapPath.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

const submitHandler = (event, map) => {
    event.preventDefault();

    if (!map.hasValidZone()) {
        alert('Debes dibujar una zona en el mapa con al menos 3 puntos');
    } else {
        const route_id = document.querySelector('#route-id').value;
        const name = document.querySelector('#name').value;
        const description = document.querySelector('#description').value;
        const coordinates = map.drawnLayers[0].getLatLngs().map(coordinate => {
            return { lat: coordinate.lat, lng: coordinate.lng }
        });

        var formData = new FormData();
        formData.append('name', name);
        formData.append('description', description);
        formData.append('coordinates', JSON.stringify(coordinates));

        fetch('/recorrido_de_evacuacion/actualizar/' + route_id, {
            method: 'POST',
            body: formData
        }).then((response) => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        });
    }
}

window.onload = () => {

    const points_data = JSON.parse(document.querySelector('#points').value);
    var latlngs = []
    points_data.forEach(point => {
        latlngs.push([point['lat'], point['lng']]);
    });

    const map = new MapPath({
        selector: 'map',
        lat: initialLat,
        lng: initialLng,
        initialLatLngs: latlngs,
        enableEdit: true
    });

    const form = document.querySelector('#edit-evacuation-route-form');
    form.addEventListener('submit', (event) => submitHandler(event, map));
}
import { MapZone } from "../MapZone.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

const submitHandler = (event, map) => {
    event.preventDefault();
    if (!map.hasValidZone()) {
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
        console.log(JSON.stringify(formData))
        
        fetch('/zonas_inundables/add', {
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
    const color = document.querySelector('#color').value;
    var latlngs = []
    points_data.forEach(point => {
        latlngs.push([point['lat'], point['lng']]);
    });
    points_data.length
    if (points_data.length>2){
        var initialLat = points_data[0]['lat'];
        var initialLng = points_data[0]['lng'];
    }else{
        var initialLat = -34.92053918330889;
        var initialLng = -57.9541949099075;
    }
    const map = new MapZone({
    selector: 'map',
    lat: initialLat,
    lng: initialLng,
    initialLatLngs: latlngs,
    enableEdit: false,
    colores: color
    });
    
    const form = document.querySelector('#edit');
    form.addEventListener('submit', (event) => submitHandler(event, map));
}
import { MapZone } from "../MapZone.js";

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
}
    

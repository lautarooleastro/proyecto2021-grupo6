import { MapPath } from "../MapPath.js";

const initialLat = -34.92053918330889;
const initialLng = -57.9541949099075;

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
        enableEdit: false
    });
}
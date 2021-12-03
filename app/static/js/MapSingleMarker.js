const mapLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

export function MapSingleMarker({ selector, addSearch, lat, lng }) {
    let marker;
    let map;

    initializeMap(selector, lat, lng);

    if (addSearch) {
        // addSearchControl();
    };

    map.addEventListener('click', (e) => { addMarker(e.latlng) });

    function initializeMap(selector, lat, lng) {
        map = L.map(selector).setView([lat, lng], 12);
        L.tileLayer(mapLayerUrl).addTo(map);
        marker = L.marker([lat, lng]).addTo(map);
    };

    function addMarker({ lat, lng }) {
        if (marker) {
            marker.remove();
        };
        marker = L.marker([lat, lng]).addTo(map);
    };

    // Plugin buscador
    //function addSearchControl() {
    //    L.control.scale().addTo(map);
    //    let searchControl = new L.esri.Controls.Geosearch().addTo(map);
    //
    //    let results = new L.LayerGroup().addTo(map);
    //
    //    searchControl.on('results', (data) => {
    //        results.clearLayers();
    //
    //        if (data.results.length > 0) {
    //            addMarker(data.results[0].latlng);
    //        }
    //    });
    //};

    return {
        get marker() { return marker },
        addMarker: addMarker
    };

}
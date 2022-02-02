const mapLayerUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';

export class MapZone {
    #drawnItems;

    constructor({ selector, lat, lng, initialLatLngs = null, enableEdit = true, colores = '#FF0000' }) {
        this.#drawnItems = new L.FeatureGroup();

        this.#initializeMap(selector, lat, lng, initialLatLngs, enableEdit, colores);

        this.map.on(L.Draw.Event.CREATED, (e) => {
            this.#createHandler(e, this.map, this.#drawnItems, this.editControls, this.createControls)
        });

        this.map.on('draw:deleted', () => {
            this.#deleteHandler(this.map, this.editControls, this.createControls)
        });
    }

    #initializeMap(selector, lat, lng, initialLatLngs, enableEdit, colores) {
        this.map = L.map(selector).setView([lat, lng], 13);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.map.addLayer(this.#drawnItems);
        if (enableEdit) {
            this.map.addControl(this.createControls);
        }

        if (initialLatLngs) {
            var polygon = L.polygon(initialLatLngs, { color: colores });
            if (enableEdit) {
                polygon.editing.enable();
                this.#drawnItems.addLayer(polygon);
                //this.editControls.addTo(map);
                this.createControls.remove();
            }
            else {
                this.#drawnItems.addLayer(polygon);
            }
        }
    }

    #createHandler(e, map, drawnItems, editControls, createControls) {
        const existingZone = Object.values(drawnItems._layers);

        if (existingZone.length == 0) {
            const type = e.layerType;
            const layer = e.layer;

            layer.editing.enable();
            drawnItems.addLayer(layer);
            editControls.addTo(map);
            createControls.remove();
        }
    }

    #deleteHandler(map, createControls, editControls) {
        createControls.addTo(map);
        editControls.remove();
    }

    hasValidZone() {
        return (this.drawnLayers.length === 1) && (this.drawnLayers[0].getLatLngs()[0].length >= 3);
    }

    get drawnLayers() {
        return Object.values(this.#drawnItems._layers);
    }

    get editControls() {
        return this.editControlsToolbar ||= new L.Control.Draw({
            draw: false,
            edit: {
                featureGroup: this.#drawnItems
            }
        });

    }

    get createControls() {
        return this.createControlsToolbar ||= new L.Control.Draw({
            draw: {
                circle: false,
                rectangle: false,
                marker: false,
                polyline: false,
                circlemarker: false
            }
        });
    }
}
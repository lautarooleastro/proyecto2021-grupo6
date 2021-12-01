const mapLayerUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';

export class MapPath {
    #drawnItems;

    constructor({ selector, lat, lng, initialLatLngs = null, enableEdit = true }) {
        this.#drawnItems = new L.FeatureGroup();
        if (initialLatLngs) {
            var polyline = L.polyline(initialLatLngs, { color: 'red' });
            this.#drawnItems.addLayer(polyline);
        }

        this.#initializeMap(selector, lat, lng, enableEdit);

        this.map.on(L.Draw.Event.CREATED, (e) => {
            this.#createHandler(e, this.map, this.#drawnItems, this.editControls, this.createControls)
        });

        this.map.on('draw:deleted', () => {
            this.#deleteHandler(this.map, this.editControls, this.createControls)
        });
    }

    #initializeMap(selector, lat, lng, enableEdit) {
        this.map = L.map(selector).setView([lat, lng], 12);
        L.tileLayer(mapLayerUrl).addTo(this.map);
        this.map.addLayer(this.#drawnItems);
        if (enableEdit) {
            this.map.addControl(this.createControls);
        }
    }

    #createHandler(e, map, drawnItems, editControls, createControls) {
        const existingPaths = Object.values(drawnItems._layers);

        if (existingPaths.length == 0) {
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
        return (this.drawnLayers.length === 1);
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
                polygon: false,
                circlemarker: false
            }
        });
    }
}
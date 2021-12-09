<template>
  <l-map style="height: 400px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <div v-for="(route, index) in routes" :key="routes - { index }">
      <l-polyline :lat-lngs="[route.coordinates]"></l-polyline>
    </div>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LPolyline } from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LPolyline,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.92053918330889, -57.9541949099075],
      routes: [],
    };
  },
  async created() {
    try {
      const response = await fetch(
        "http://127.0.0.1:5000/api/recorridos-evacuacion/"
      );
      const json = await response.json();
      this.routes = json.recorridos;
    } catch (e) {
      console.log(e);
    }
  },
};
</script>
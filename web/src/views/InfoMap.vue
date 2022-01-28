<template>
  <div>
    <h2>Recorridos de evacuación y Puntos de Encuentro</h2>
    <l-map style="height: 400px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="route in routes" :key="route">
        <l-polyline :lat-lngs="route.coordinates"></l-polyline>
      </div>
    </l-map>
    <div>
      <h3>Recorridos de evacuación</h3>
      <div v-for="route in routes" :key="route">
        <p>{{ route.name }}</p>
      </div>
    </div>
  </div>
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
  created() {
    fetch("http://127.0.0.1:5000/api/recorridos-evacuacion/")
      .then((response) => {
        //console.log(response);
        return response.json();
      })
      .then((json) => {
        //console.log(json.recorridos);
        this.routes = json.recorridos;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
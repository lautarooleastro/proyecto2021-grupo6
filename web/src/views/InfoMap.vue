<template>
  <div>
    <h2>Recorridos de evacuación y Puntos de Encuentro</h2>
    <l-map style="height: 400px" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <div v-for="route in routes" :key="route">
        <l-polyline :lat-lngs="route.coordinates"></l-polyline>
      </div>
      <div v-for="point in points" :key="point">
        <l-marker :lat-lng="point">
          <l-popup>
            <div class="col">
              <h6>{{ point.name }}</h6>
              <div>{{ point.adress }}</div>
              <div>{{ point.phone }}</div>
              <div>{{ point.email }}</div>
            </div>
          </l-popup>
        </l-marker>
      </div>
    </l-map>
    <div class="container mt-4">
      <div class="row">
        <div class="col text-start">
          <h3>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              class="bi bi-arrow-right-square-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"
              />
            </svg>
            Recorridos de evacuación
          </h3>
          <div v-for="route in routes" :key="route" class="container">
            <div class="row mt-4">
              <div class="fw-bold">{{ route.name }}</div>
              <div>{{ route.description }}</div>
            </div>
          </div>
        </div>
        <div class="col text-start">
          <h3>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              class="bi bi-geo-alt-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"
              />
            </svg>
            Puntos de encuentro
          </h3>
          <div v-for="point in points" :key="point" class="container">
            <div class="row mt-4">
              <div class="fw-bold">{{ point.name }}</div>
              <div>
                {{ point.adress }} - {{ point.phone }} - {{ point.email }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LPolyline,
  LMarker,
  LPopup,
} from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LPolyline,
    LMarker,
    LPopup,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.92053918330889, -57.9541949099075],
      routes: [],
      points: [],
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
    fetch("http://127.0.0.1:5000/api/puntos-encuentro/")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.points = json.puntos_encuentro;
        console.log(this.points);
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
// src/Map.js
import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';

const Map = () => {
  const [geoData, setGeoData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/geojson')
      .then(response => {
        setGeoData(response.data);
      })
      .catch(error => {
        console.error('Error fetching the GeoJSON data:', error);
      });
  }, []);

  return (
    <MapContainer center={[33.6, 89.0]} zoom={5} style={{ height: '100vh', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {geoData && <GeoJSON data={geoData} />}
    </MapContainer>
  );
};

export default Map;

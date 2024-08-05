// src/components/TrainSearch.js

import React, { useState } from 'react';
import axios from '../api/axios';
import './TrainSearch.css'; // Import the CSS file

function TrainSearch() {
  const [stations, setStations] = useState({ start: '', end: '' });
  const [trains, setTrains] = useState([]);

  const handleChange = (e) => {
    setStations({ ...stations, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Call API to get trains
    axios.get(`trains?start=${stations.start}&end=${stations.end}`)
      .then(response => setTrains(response.data))
      .catch(error => console.error(error));
  };

  return (
    <div className="train-search-container">
      <form className="train-search-form" onSubmit={handleSubmit}>
        <input name="start" value={stations.start} onChange={handleChange} placeholder="Start Station" />
        <input name="end" value={stations.end} onChange={handleChange} placeholder="End Station" />
        <button type="submit">Search Trains</button>
      </form>
      <ul className="train-list">
        {trains.map(train => (
          <li className="train-list-item" key={train.id}>
            <div className="train-number">{train.train_number}</div>
            <div className="train-route">{train.start_station} - {train.end_station}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TrainSearch;

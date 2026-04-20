import React, { useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function Dashboard({ stats }) {
  const [threshold, setThreshold] = useState(0.5);

  return (
    <div>
      <h1>Defect Statistics</h1>
      <BarChart data={stats}>
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        value={threshold}
        onChange={(e) => setThreshold(e.target.value)}
      />
      <p>Confidence Threshold: {threshold}</p>
    </div>
  );
}
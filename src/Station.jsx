import React from 'react';

function Station(props) {
  return (
    <div className="station">
        <svg height="50" width="50">
            <circle cx="25" cy="25" r="15" stroke="black" stroke-width="3" fill="black" />
        </svg>
        <h2 className="station-name">{props.name}</h2>
    </div>
  );
}

export default Station;

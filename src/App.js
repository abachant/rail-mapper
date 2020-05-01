import React from 'react';
import Station from './Station';
import Link from './Link';

function App() {
  return (
    <div className="App">
      <Station name="Park Street"/>
      <Link />
      <Station name="Tremont Street" />
      <Link />
      <Station name="Haymarket" />
    </div>
  );
}

export default App;

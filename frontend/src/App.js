import React, { useState } from 'react';
import './assets/css/App.css';
import './assets/css/buttons.css';
import './assets/css/pokemon-type-badge.css';
import openaiLogo from './assets/images/openai-logo.png';

function App() {
  const [loading, setLoading] = useState(false);

  const [pokemon1, setPokemon1] = useState(null);
  const [pokemon2, setPokemon2] = useState(null);
  const [battleResult, setBattleResult] = useState(null);

  const generateBattle = async () => {
    const response = await fetch('/generate_battle');
    const data = await response.json();
    setBattleResult(null);
    let url_pokemon = 'https://pokeapi.co/api/v2';

    // Get information according pokemon 1
    const pokemon1Response = await fetch(`${url_pokemon}/pokemon/${data.pokemon1_id}`);
    const pokemon1Data = await pokemon1Response.json();
    setPokemon1(pokemon1Data);

    // Get information according pokemon 2
    const pokemon2Response = await fetch(`${url_pokemon}/pokemon/${data.pokemon2_id}`);
    const pokemon2Data = await pokemon2Response.json();
    setPokemon2(pokemon2Data);
  };

  const getResultBattle = async () => {
    setLoading(true);
    // with pokemons get result from flask
    if (pokemon1 && pokemon2) {
      const response = await fetch(`/battle_result/${pokemon1.id}/${pokemon2.id}`);
      const data = await response.json();
      
      setLoading(false);
      setBattleResult(data);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Pokémon Battle Simulator</h1>
      <div className="button-container">
        <button onClick={generateBattle} className="button generate-button">+ New Battle</button>
      </div>
      <div className="pokemon-cards-container">
        {pokemon1 && (
          <div className={`pokemon-card ${battleResult && battleResult.winner === pokemon1.name ? 'winner' : ''}`}>
            <h3 className="pokemon-name">Pokémon 1: {pokemon1.name}</h3>
            <img className="pokemon-image" src={pokemon1.sprites.front_default} alt={pokemon1.name} />
            <p className="pokemon-type">Type: <span className={`pokemon-type-badge ${pokemon1.types[0].type.name}`}>{pokemon1.types[0].type.name}</span></p>
          </div>
        )}
        {pokemon2 && (
          <div className={`pokemon-card ${battleResult && battleResult.winner === pokemon2.name ? 'winner' : ''}`}>
            <h3 className="pokemon-name">Pokémon 2: {pokemon2.name}</h3>
            <img className="pokemon-image" src={pokemon2.sprites.front_default} alt={pokemon2.name} />
            <p className="pokemon-type">Type: <span className={`pokemon-type-badge ${pokemon2.types[0].type.name}`}>{pokemon2.types[0].type.name}</span></p>
          </div>
        )}
      </div>
      
      {pokemon1 && pokemon2 && (
        <div className="button-container">
          <button onClick={getResultBattle}  className="button result-button">Get Result</button>
        </div>
      )}

      {loading ? (
      <div className="loading">Waiting Open AI...</div>
      ) : (
        <div></div>
      )}

      {battleResult && (
        <div className="result-card">
          <h2>🏆 Winner: {battleResult.winner} 
          </h2>
          <small>generate by: </small><img src={openaiLogo} alt="Open AI Logo" style={{ width: 100 }} />
          <p>Explanation: {battleResult.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default App;

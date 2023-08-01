import React, { useState } from 'react';
import './App.css';
import './buttons.css';
import './pokemon-type-badge.css';

function App() {
  const [pokemon1, setPokemon1] = useState(null);
  const [pokemon2, setPokemon2] = useState(null);
  const [battleResult, setBattleResult] = useState(null);

  const gerarBatalha = async () => {
    const response = await fetch('/gerar_batalha');
    const data = await response.json();
    setBattleResult(null);

    // Obtém informações do primeiro Pokémon
    const pokemon1Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${data.pokemon1_id}`);
    const pokemon1Data = await pokemon1Response.json();
    setPokemon1(pokemon1Data);

    // Obtém informações do segundo Pokémon
    const pokemon2Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${data.pokemon2_id}`);
    const pokemon2Data = await pokemon2Response.json();
    setPokemon2(pokemon2Data);
  };

  const obterResultadoBatalha = async () => {
    // Implemente a lógica para enviar os IDs dos Pokémon ao servidor Flask
    // e obter o resultado da batalha e a explicação.
    // O código a seguir é apenas um esboço e precisa ser implementado.

    if (pokemon1 && pokemon2) {
      const response = await fetch(`/resultado_batalha/${pokemon1.id}/${pokemon2.id}`);
      const data = await response.json();
      setBattleResult(data);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Simulador de batalhas Pokémon</h1>
      <div className="button-container">
        <button onClick={gerarBatalha} className="button generate-button">+ Nova Batalha</button>
      </div>
      <div className="pokemon-cards-container">
        {pokemon1 && (
          <div className={`pokemon-card ${battleResult && battleResult.winner === pokemon1.name ? 'winner' : ''}`}>
            <h3 className="pokemon-name">Pokémon 1: {pokemon1.name}</h3>
            <img className="pokemon-image" src={pokemon1.sprites.front_default} alt={pokemon1.name} />
            <p className="pokemon-type">Tipo: <span className={`pokemon-type-badge ${pokemon1.types[0].type.name}`}>{pokemon1.types[0].type.name}</span></p>
          </div>
        )}
        {pokemon2 && (
          <div className={`pokemon-card ${battleResult && battleResult.winner === pokemon2.name ? 'winner' : ''}`}>
            <h3 className="pokemon-name">Pokémon 2: {pokemon2.name}</h3>
            <img className="pokemon-image" src={pokemon2.sprites.front_default} alt={pokemon2.name} />
            <p className="pokemon-type">Tipo: <span className={`pokemon-type-badge ${pokemon2.types[0].type.name}`}>{pokemon2.types[0].type.name}</span></p>
          </div>
        )}
      </div>
      
      {pokemon1 && pokemon2 && (
        <div className="button-container">
          <button onClick={obterResultadoBatalha}  className="button result-button">Obter Resultado</button>
        </div>
      )}

      {battleResult && (
        <div className="result-card">
          <h2>Vencedor: {battleResult.winner}</h2>
          <p>Explicação: {battleResult.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default App;

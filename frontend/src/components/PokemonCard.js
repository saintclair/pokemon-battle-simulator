// PokemonCard.js
import React from 'react';
import '../assets/css/pokemon-card.css';

const PokemonCard = ({ pokemon, isWinner }) => {
  return (
    <div className={`pokemon-card ${isWinner ? 'winner' : ''}`}>
      <h3 className="pokemon-name">Pokémon: {pokemon.name}</h3>
      <img className="pokemon-image" src={pokemon.sprites.front_default} alt={pokemon.name} />
      <p className="pokemon-type">Type: <span className={`pokemon-type-badge ${pokemon.types[0].type.name}`}>{pokemon.types[0].type.name}</span></p>
    </div>
  );
};

export default PokemonCard;
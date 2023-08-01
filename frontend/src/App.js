import React, { useState } from 'react';
import './assets/css/App.css';
import './assets/css/buttons.css';
import './assets/css/pokemon-type-badge.css';

import PokemonCard from './components/PokemonCard';
import BattleResultCard from './components/BattleResultCard';
import LoadingSpinner from './components/LoadingSpinner';

function App() {
    const [loading, setLoading] = useState(false);
    const [pokemon1, setPokemon1] = useState(null);
    const [pokemon2, setPokemon2] = useState(null);
    const [battleResult, setBattleResult] = useState(null);

    const generateBattle = async () => {
        setLoading(true); // Definir o loading para true ao iniciar a geração da batalha

        try {
          const response = await fetch('/generate_battle');
          const data = await response.json();
      
          // Obtendo informações do primeiro Pokémon
          const pokemon1Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${data.pokemon1_id}`);
          const pokemon1Data = await pokemon1Response.json();
          setPokemon1(pokemon1Data);
      
          // Obtendo informações do segundo Pokémon
          const pokemon2Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${data.pokemon2_id}`);
          const pokemon2Data = await pokemon2Response.json();
          setPokemon2(pokemon2Data);
      
          setLoading(false); // Definir o loading para false após obter os dados dos Pokémon
        } catch (error) {
          console.error('Ocorreu um erro ao gerar a batalha:', error);
          setLoading(false); // Definir o loading para false em caso de erro
        }
    };

    const getResultBattle = async () => {
        setLoading(true); // Definir o loading para true ao obter o resultado da batalha

        try {
          // Verificando se temos informações dos dois Pokémon necessárias para obter o resultado da batalha
          if (pokemon1 && pokemon2) {
            const response = await fetch(`/battle_result/${pokemon1.id}/${pokemon2.id}`);
            const data = await response.json();
      
            // Atualizar o estado do resultado da batalha
            setBattleResult(data);
      
            setLoading(false); // Definir o loading para false após obter o resultado da batalha
          } else {
            console.error('Não há informações suficientes para obter o resultado da batalha.');
            setLoading(false); // Definir o loading para false em caso de erro
          }
        } catch (error) {
          console.error('Ocorreu um erro ao obter o resultado da batalha:', error);
          setLoading(false); // Definir o loading para false em caso de erro
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
                    <PokemonCard
                        pokemon={pokemon1}
                        isWinner={battleResult && battleResult.winner === pokemon1.name}
                    />
                )}
                {pokemon2 && (
                    <PokemonCard
                        pokemon={pokemon2}
                        isWinner={battleResult && battleResult.winner === pokemon2.name}
                    />
                )}
            </div>

            {pokemon1 && pokemon2 && (
                <div className="button-container">
                    <button onClick={getResultBattle} className="button result-button">Get Result</button>
                </div>
            )}

            {loading ? <LoadingSpinner /> : null}

            {battleResult && (
                <BattleResultCard
                    winner={battleResult.winner}
                    explanation={battleResult.explanation}
                />
            )}
        </div>
    );
}

export default App;
import {useState} from "react"
// import Home from '../home/Home';


function Contador(){
  // Definindo um estado simples para um contador
  const [valor, setValor] = useState<number>(0);

  // Função para aumentar o contador
  function handleClick(){setValor(valor + 1);}
  return (
    <div>
      <h2>Componente Contador</h2>
      <p>O valor atual é: {valor}</p>
      <button onClick={handleClick}>Adicionar 1</button>
    </div>
  )
}
export default Contador

// import React, { useState } from 'react';
// import './App.css';
// import Home from './pages/home/Home';  // Certifique-se de que o caminho esteja correto

// const App: React.FC = () => {
//   // Definindo um estado simples para um contador
//   const [count, setCount] = useState<number>(0);

//   // Função para aumentar o contador
//   const increment = () => setCount(count + 1);

//   return (
//     <div className="App">
//       <h1>Contador: {count}</h1>
//       <button onClick={increment}>Incrementar</button>
//       <Home />
//     </div>
//   );
// }

// export default App;

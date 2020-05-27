import React from 'react';
import princesa from './princesa.png'
import nina from './nina.png'
import mascara from './mascara.png'
import toffee from './toffee.png'
import './App.css';


export default class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={princesa} className="App-logo" alt="logo" />
          <img src={nina} className="App-logo" alt="logo" />
          <img src={mascara} className="App-logo" alt="logo" />
          <img src={toffee} className="App-logo" alt="logo" />
        </header>
      </div>
    );
  }
}
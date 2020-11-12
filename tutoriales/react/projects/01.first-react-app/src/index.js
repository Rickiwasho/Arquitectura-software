import React from 'react';
import ReactDOM from 'react-dom';

const header = (
  <header>
      <h1>Bienvenido</h1>
      <h2>Iniciando el desarrollo con React</h2>
      <h3>Una librería de Javascript</h3>
  </header>
)
const main = (
  <main>
    <p>Prerequisitos para inciar con react.js</p>
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>Javascript</li>
    </ul>
  </main>
)
const footer = (
  <footer>
    <p>Copyright 2020</p>
  </footer>
)
const app = (
  <div>
    {header}
    {main}
    {footer}
  </div>

)
const rootElement = document.getElementById('root')

ReactDOM.render(app, rootElement)
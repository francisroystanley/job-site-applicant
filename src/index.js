// import "./wdyr";

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from "react-redux";

import Head from './Head';
import CSS from './Css';
import App from './App';
import store from "./Store";


ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <Head />
      <CSS />
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('react-root')
);

import { useState } from 'react';
import WOW from 'wowjs';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';

import NavBar from './Navbar';
import Footer from './Footer';
import ErrorPage from './features/error';
import { BlockUI } from './commons';
import CareerSearch from "./features/career/search";
import Home from "./features/home";


const App = () => {
  const wow = new WOW.WOW({
    live: false
  });
  wow.init();

  const [isBusy, setIsBusy] = useState(true);

  return (
    <>
      {/* {isBusy && <BlockUI />} */}
      <BrowserRouter>
        <NavBar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/career" component={CareerSearch} />
          {/* <Route exact path="/career">
            <Route component={CareerSearch} />
            <Redirect to="/career/search" />
          </Route> */}
          <Route exact path="/404" component={ErrorPage} />
          <Redirect to="/404" />
        </Switch>
        <Footer />
      </BrowserRouter>
    </>
  );
};

export default App;

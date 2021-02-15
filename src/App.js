import { useState, useEffect } from 'react';
import WOW from 'wowjs';
import { useDispatch, useSelector } from "react-redux";
import { BrowserRouter, Route } from 'react-router-dom';

import NavBar from './Navbar';
import Body from './Body';
import Footer from './Footer';
import { BlockUI } from './commons';
import { getBusinessUnit } from './slices/businessunit';


const App = () => {
  const dispatch = useDispatch();
  const businessunit = useSelector(state => state.businessunit);
  const wow = new WOW.WOW({
    live: false
  });
  wow.init();

  useEffect(() => {
    dispatch(getBusinessUnit()).then(entities => console.log(entities));
    // console.log("businessunit: ", test);
  }, []);

  const [isBusy, setIsBusy] = useState(true);

  return (
    <>
      {isBusy && <BlockUI />}
      <BrowserRouter>
        <NavBar />
        <Route exact path="/" component={Body} />
        <Route>404 not found!</Route>
        <Footer />
      </BrowserRouter>
    </>
  );
};

export default App;

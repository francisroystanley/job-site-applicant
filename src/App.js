import { useState } from 'react';
import WOW from 'wowjs';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';

import NavBar from './Navbar';
import Footer from './Footer';
import ErrorPage from './features/error';
import { BlockUI } from './commons';
import Career from "./features/career";
import Home from "./features/home";
import SignIn from "./features/signin";
import Register from "./features/register";
import ForgotPassword from "./features/forgot-password";
import PrivacyPolicy from "./features/privacy-policy";
import TermsCondition from "./features/terms-and-conditions";
import LegitimatePurpose from "./features/legitimate-purpose";


const App = () => {
  const wow = new WOW.WOW({
    live: false
  });
  wow.init();

  const [isBusy, setIsBusy] = useState(true);

  return (
    <>
      {/* {isBusy && <BlockUI />} */}
      <NavBar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/signin" component={SignIn} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/forgotpassword" component={ForgotPassword} />
        <Route exact path="/career" component={Career} />
        {/* <Route exact path="/career">
            <Route component={CareerSearch} />
            <Redirect to="/career/search" />
          </Route> */}
        <Route exact path="/privacy_policy" component={PrivacyPolicy} />
        <Route exact path="/terms_and_conditions" component={TermsCondition} />
        <Route exact path="/legitimate_purpose" component={LegitimatePurpose} />
        <Route exact path="/404" component={ErrorPage} />
        <Redirect to="/404" />
      </Switch>
      <Footer />
    </>
  );
};

export default App;

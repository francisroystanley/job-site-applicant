import { useEffect, useContext, memo } from "react";
import loadable from '@loadable/component';
import ReactDOM from 'react-dom';
import { createSelector } from "reselect";
import { useSelector } from "react-redux";



// const stateSelector = createSelector(getBusinessUnit, state => state);

const Footer = () => {
  let el = document.createElement('footer');
  el.className = 'footer dark-bg';
  const entities = [];
  // const entities = useSelector(stateSelector);
  // const entities = useContext(BusinessUnit);
  const env = process.env;
  const client_code = env.REACT_APP_CLIENT_CODE;
  let parentElem = document.body;

  const FooterComponent = loadable(() => import(`./custom/footer/${ client_code.toLowerCase() }`));

  useEffect(() => {
    parentElem.appendChild(el);
    return () => {
      parentElem.removeChild(el);
    };
  });

  return ReactDOM.createPortal(<FooterComponent entities={entities} />, el);
};

export default memo(Footer);

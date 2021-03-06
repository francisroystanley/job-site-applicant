import { useEffect, memo } from "react";
import loadable from '@loadable/component';
import ReactDOM from 'react-dom';
import { useSelector } from "react-redux";


const Footer = () => {
  let el = document.createElement('footer');
  el.className = 'footer dark-bg';
  let parentElem = document.body;

  const entities = useSelector(({ businessUnit }) => businessUnit);
  const env = useSelector(({ env }) => env);

  const FooterComponent = loadable(() => import(`./features/footer/${ env.client_code.toLowerCase() }`));

  useEffect(() => {
    parentElem.appendChild(el);
    return () => {
      parentElem.removeChild(el);
    };
  });

  return env.client_code ? ReactDOM.createPortal(<FooterComponent entities={entities} showConsent={env.showCookieConsent} />, el) : null;
};

export default memo(Footer);

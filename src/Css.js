import loadable from '@loadable/component';
import { useSelector } from "react-redux";

import "font-awesome/css/font-awesome.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "react-bootstrap-typeahead/css/Typeahead.css";
import "../src/assets/css/animate.css";
import "../src/assets/css/blockUI.css";
import "../src/assets/css/main.css";
import "../src/assets/css/style.css";


const CSS = () => {
  const env = useSelector(({ env }) => env);

  const CSSComponent = loadable(() => import(`./custom/css/${ env.client_code.toLowerCase() }`));

  return env.client_code ? <CSSComponent /> : null;
};

export default CSS;

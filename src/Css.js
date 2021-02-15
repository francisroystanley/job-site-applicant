import loadable from '@loadable/component';

import "font-awesome/css/font-awesome.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "react-bootstrap-typeahead/css/Typeahead.css";
import "../src/assets/css/animate.css";
import "../src/assets/css/blockUI.css";
import "../src/assets/css/main.css";
import "../src/assets/css/style.css";


const CSS = () => {
  const env = process.env;
  const client_code = env.REACT_APP_CLIENT_CODE;

  const CSSComponent = loadable(() => import(`./custom/css/${ client_code.toLowerCase() }`));

  return <CSSComponent />;
};

export default CSS;

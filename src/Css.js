import { memo } from "react";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { useSelector } from "react-redux";

import "font-awesome/css/font-awesome.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "react-bootstrap-typeahead/css/Typeahead.css";


const CSS = () => {
  const env = useSelector(({ env }) => env);

  return env.client_code ? (
    <>
      <HelmetProvider>
        <Helmet>
          <>
            <link rel="stylesheet" href="assets/css/animate.css" />
            <link rel="stylesheet" href="assets/css/blockUI.css" />
            <link rel="stylesheet" href="assets/css/main.css" />
            <link rel="stylesheet" href="assets/css/style.css" />
            <link rel="stylesheet" href={`assets/css/${ env.client_code.toLowerCase() }.css`} />
          </>
        </Helmet>
      </HelmetProvider>
    </>
  ) : null;
};

export default memo(CSS);

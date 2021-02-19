import { memo, useEffect } from "react";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { useDispatch, useSelector } from "react-redux";

import { getEnv } from "./slices/env";
import { getBusinessUnit, updateBusinessUnitList } from './slices/businessunit';

import "font-awesome/css/font-awesome.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "react-bootstrap-typeahead/css/Typeahead.css";


const CSS = () => {
  let banner_meta;
  const dispatch = useDispatch();
  const env = useSelector(({ env }) => env);
  let metaImage;
  let metaUrl = window.location.href.replace('http', 'https');

  // if (['PRIME', 'SMPRIME'].includes(banner_meta)) {
  //   metaImage = SMPRIME;
  //   metaUrl += banner_meta.toLowerCase();
  // } else if (['EDD', 'SMEDD'].includes(banner_meta)) {
  //   metaImage = SMEDD;
  //   metaUrl += banner_meta.toLowerCase();
  // } else if (banner_meta == 'SMDC') {
  //   metaImage = SMDC;
  //   metaUrl += banner_meta.toLowerCase();
  // } else if (banner_meta == 'SCMC') {
  //   metaImage = SCMC;
  //   metaUrl += 'smsupermalls';
  // } else if (banner_meta == 'SMC') {
  //   metaImage = SMC;
  //   metaUrl += 'smcinema';
  // } else if (banner_meta == 'SMLI') {
  //   metaImage = SMLI;
  //   metaUrl += 'smlifestyle';
  // } else {
  //   metaImage = ALLSM;
  // }

  useEffect(() => {
    dispatch(getEnv());
    dispatch(getBusinessUnit()).then(({ payload }) => dispatch(updateBusinessUnitList(payload)));
  }, []);

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

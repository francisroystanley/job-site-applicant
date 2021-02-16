import { memo, useEffect } from "react";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { useDispatch, useSelector } from "react-redux";

import { getEnv } from "./slices/env";
import { getBusinessUnit, updateBusinessUnitList } from './slices/businessunit';

import company_logo from "./assets/images/company-logo-SMPRIME.png";
import ALLSM from "./assets/images/ALLSM-527x273.jpg";
import SMPRIME from "./assets/images/SMPRIME-527x273.jpg";
import SMEDD from "./assets/images/SMEDD-527x273.jpg";
import SMDC from "./assets/images/SMDC-527x273.jpg";
import SCMC from "./assets/images/SCMC-527x273.jpg";
import SMC from "./assets/images/SMC-527x273.jpg";
import SMLI from "./assets/images/SMLI-527x273.jpg";


const Head = () => {
  console.log(arguments);
  let banner_meta;
  const dispatch = useDispatch();
  const env = useSelector(({ env }) => env);
  let metaImage;
  let metaUrl = window.location.href.replace('http', 'https');

  if (['PRIME', 'SMPRIME'].includes(banner_meta)) {
    metaImage = SMPRIME;
    metaUrl += banner_meta.toLowerCase();
  } else if (['EDD', 'SMEDD'].includes(banner_meta)) {
    metaImage = SMEDD;
    metaUrl += banner_meta.toLowerCase();
  } else if (banner_meta == 'SMDC') {
    metaImage = SMDC;
    metaUrl += banner_meta.toLowerCase();
  } else if (banner_meta == 'SCMC') {
    metaImage = SCMC;
    metaUrl += 'smsupermalls';
  } else if (banner_meta == 'SMC') {
    metaImage = SMC;
    metaUrl += 'smcinema';
  } else if (banner_meta == 'SMLI') {
    metaImage = SMLI;
    metaUrl += 'smlifestyle';
  } else {
    metaImage = ALLSM;
  }

  useEffect(() => {
    dispatch(getEnv());
    dispatch(getBusinessUnit()).then(({ payload }) => dispatch(updateBusinessUnitList(payload)));
  }, []);

  return (
    <>
      <HelmetProvider>
        <Helmet>
          <title>{`${ env.client_code } Careers`}</title>
          {env.client_code == 'SM' &&
            <>
              <link rel="apple-touch-icon" sizes="76x76" href={company_logo} />
              <meta property="og:site_name" content="www.smprimecareers.com" />
              <meta property="og:type" content="website" />
              <meta property="og:title" content="SM Careers" />
              <meta property="og:description" content="" />
              <meta property="og:image" content={metaImage} />
              <meta property="og:url" content={metaUrl} />
            </>
          }
          {env.client_code == 'TALENTMATCH' &&
            <>
              <meta property="og:site_name" content="beta.talentmatch.asia" />
              <meta property="og:type" content="website" />
              <meta property="og:title" content="Talenmatch" />
              <meta property="og:description" content="" />
            </>
          }
          {env.client_code == 'TITANIUM' &&
            <>
              <meta property="og:site_name" content="jobs.titanium.ph" />
              <meta property="og:type" content="website" />
              <meta property="og:title" content="Titanium Job site" />
              <meta property="og:description" content="" />
            </>
          }
        </Helmet>
      </HelmetProvider>
    </>
  );
};

export default memo(Head);

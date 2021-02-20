import { useDispatch } from "react-redux";
import { Link } from "react-router-dom";

import { updateEnvState } from "../../slices/env";


const Footer = ({ entities, showConsent }) => {
  const dispatch = useDispatch();

  const acceptCookieConsent = () => {
    // Insert code to read and insert cookies
    dispatch(updateEnvState({ showCookieConsent: false }));
  };

  return (
    <>
      <div className="footerBody">
        <div className="overlay">
          <div className="container">
            <div className="row">
              <div className="item col-md-4 my-3">
                <div className="gr-icon-top-text-style-1 text-center">
                  <div className="fs-35"><i className="fas fa-globe"></i></div>
                  <br />
                  <div className="text">
                    <ul className="pagesLinks">
                      <li><Link to="/home">Home</Link></li>
                      <li><Link to="/career">Careers</Link></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div className="item col-md-4 my-3">
                <div className="gr-icon-top-text-style-1 text-center">
                  <div className="fs-35"><i className="fas fa-link"></i></div>
                  <br />
                  <div className="text">
                    <ul className="pagesLinks">
                      <li>
                        {entities.map(entity =>
                          <Link key={entity.businessunit_code} to={`/${ entity.businessunit_code.toLowerCase() }`}
                          // ui-sref="landingpage_{{entity.code}}"
                          >{entity.businessunit_name}
                          </Link>
                        )}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <div className="col-md-4 my-3">
                <div className="gr-icon-top-text-style-1 text-center">
                  <div className="fs-35"><i className="fas fa-mobile-alt"></i></div>
                  <br />
                  <div className="text">
                    <ul className="pagesLinks">
                      <li className="m-15">
                        <a className="my-0 d-inline" target="_blank" href="https://www.ayalaland.com.ph/contact-us/">Ayala Land</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline" target="_blank" href="https://www.bpi.com.ph/contactus">BPI</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline" target="_blank" href="https://www.globe.com.ph/contact-us.html">Globe Telecom</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline" target="_blank" href="https://www.manilawater.com/customer/contact-us">Manila Water</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="footerBottom">
        <div className="container">
          <div className="row align-items-center">
            <div className="col-md-6 text-center text-md-left my-2">
              <ul className="pagesLinks d-flex flex-wrap justify-content-around">
                <li className="my-2 mx-3">
                  <Link to="/privacy_policy">Privacy Policy</Link>
                </li>
                <li className="my-2 mx-3">
                  <Link to="/terms_and_conditions">Terms and Condition</Link>
                </li>
                <li className="my-2 mx-3">
                  <Link to="/legitimate_purpose">Legitimate Purpose</Link>
                </li>
              </ul>
            </div>
            <div className="col-md-6 text-center text-md-right my-2">
              <p className="copyright"> All Rights Reserved. Copyright 2021 </p>
            </div>
          </div>
        </div>
      </div>
      {showConsent &&
        <div id="cookie_consent" className="row justify-content-around fixed-bottom mb-0 p-2 align-items-center" role="alert">
          <div className="mb-1 text-white">
            This website uses cookies to improve user experience. By using our website, you consent to all cookies in accordance with our Cookie Policy. <Link to="/privacy_policy"><u>Learn more.</u></Link>
          </div>
          <button className="mb-1 btn btn-secondary font-weight-bold" onClick={acceptCookieConsent}>Got it!</button>
        </div>
      }
    </>
  );
};

export default Footer;

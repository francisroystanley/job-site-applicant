const Footer = ({ entities }) => {
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
                      <li><a
                      // ui-sref="home"
                      >Home</a></li>
                      <li><a
                      // ui-sref="career.search"
                      >Careers</a></li>
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
                          <a key={entity.businessunit_code}
                          // ui-sref="landingpage_{{entity.code}}"
                          >{entity.businessunit_name}
                          </a>
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
                        <a className="my-0 d-inline">SM PRIME</a>
                        <a className="my-0 d-inline" href="tel:862-7973"> 8862-7973</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline">SCMC</a>
                        <a className="my-0 d-inline" href="tel:862-7150"> 8862-7150</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline">SMEDD</a>
                        <a className="my-0 d-inline" href="tel:862-7581"> 8862-7581</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline">SM CINEMA</a>
                        <a className="my-0 d-inline" href="tel:862-7654"> 8862-7654</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline">FECI & ARENA</a>
                        <a className="my-0 d-inline" href="tel:862-7714"> 8862-7714</a>
                      </li>
                      <li className="m-15">
                        <a className="my-0 d-inline">SMDC</a>
                        <a className="my-0 d-inline" href="tel:857-0100 Local 1579"> 8857-0100 Local 1579</a>
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
                <li className="my-2 mx-3"><a
                // ui-sref="privacy_policy"
                >Privacy Policy</a></li>
                <li className="my-2 mx-3"><a
                // ui-sref="terms_and_conditions"
                >Terms and Condition</a></li>
                <li className="my-2 mx-3"><a
                // ui-sref="legitimate_purpose"
                >Legitimate Purpose</a></li>
              </ul>
            </div>
            <div className="col-md-6 text-center text-md-right my-2">
              <p className="copyright"> All Rights Reserved. Copyright 2019 </p>
            </div>
          </div>
        </div>
      </div>
      <div id="cookie_consent" className="row justify-content-around fixed-bottom mb-0 p-2 align-items-center" role="alert"
      // ng-show="$root.showNotif"
      >
        <div className="mb-1">
          This website uses cookies to improve user experience. By using our website, you consent to all cookies in accordance with our Cookie Policy. < a
          // ui - sref="privacy_policy"
          ><u>Learn more.</u></a>
        </div >
        <button className="mb-1 btn btn-primary font-weight-bold"
        // ng-click="$root.changeCookieSetting(true)"
        >Got it!</button>
      </div >
    </>
  );
};

export default Footer;

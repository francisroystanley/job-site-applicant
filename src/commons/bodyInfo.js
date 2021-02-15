import bodyBottom from "../assets/images/body-bottom-graphic.png";
import PRIME from "../assets/images/company-logo-PRIME.png";
import EDD from "../assets/images/company-logo-EDD.png";
import SMC from "../assets/images/company-logo-SMC.png";
import SCMC from "../assets/images/company-logo-SCMC.png";
import FECI from "../assets/images/company-logo-FECI.png";
import SMLI from "../assets/images/company-logo-SMLI.png";
import SMDC from "../assets/images/company-logo-SMDC.png";


const BodyInfo = () => {
  return (
    <>
      <section className="bodyContents-section mt-3 mt-md-5 pb-0 text-center">
        <div className="container">
          <img src={bodyBottom} className="img-fluid wow fadeInUp" data-wow-delay="0s" />
        </div>
      </section>
      <section id="companiesLogos" className="companiesLogos bodyContents-section wow fadeInUp" data-wow-delay="0s">
        <div className="container">
          <div className="companiesLogos-list row">
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.1s" src={PRIME} alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.2s" src={EDD} alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.3s" src={SMC} alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.4s" src={SCMC} alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src={FECI} alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src={SMLI} alt="" />
            </div>
            <div className="agencyLogoWrap col-12 mt-md-4 mt-lg-0 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src={SMDC} alt="" />
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default BodyInfo;

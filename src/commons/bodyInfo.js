const BodyInfo = () => {
  return (
    <>
      <section className="bodyContents-section mt-3 mt-md-5 pb-0 text-center">
        <div className="container">
          <img src="/assets/images/body-bottom-graphic.png" className="img-fluid wow fadeInUp" data-wow-delay="0s" />
        </div>
      </section>
      <section id="companiesLogos" className="companiesLogos bodyContents-section wow fadeInUp" data-wow-delay="0s">
        <div className="container">
          <div className="companiesLogos-list row">
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.1s" src="/assets/images/company-logo-PRIME.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.2s" src="/assets/images/company-logo-EDD.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.3s" src="/assets/images/company-logo-SMC.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.4s" src="/assets/images/company-logo-SCMC.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src="/assets/images/company-logo-FECI.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-4 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src="/assets/images/company-logo-SMLI.png" alt="" />
            </div>
            <div className="agencyLogoWrap col-12 mt-md-4 mt-lg-0 col-md">
              <img className="agencyLogo wow fadeInUp" data-wow-delay="0.5s" src="/assets/images/company-logo-SMDC.png" alt="" />
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default BodyInfo;

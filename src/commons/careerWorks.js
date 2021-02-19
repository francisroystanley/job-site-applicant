const CareerWorks = () => {
  return (
    <section className="bodyContents-section">
      <div className="container">
        <div className="row">
          <div className="col-md-10 offset-md-1 text-center wow fadeInUp" data-wow-delay="0s">
            <h3 className="h3">How Ayala Career works?</h3>
            <p className="lead">
            </p>
          </div>
        </div>
        <div className="our-process row justify-content-center">
          <div className="singleProcess col-11 col-md-4 wow fadeInUp" data-wow-delay="0.1s">
            <div className="row align-items-center">
              <div className="col-3 col-md-12 pr-0">
                <img src="/assets/images/process-icon-1.png" className="processIcon img-fluid" />
              </div>
              <div className="col col-md-12 pr-0">
                <div>
                  <h5 className="mb-0">Create account</h5>
                </div>
              </div>
            </div>
          </div>
          <div className="singleProcess col-11 col-md-4 wow fadeInUp" data-wow-delay="0.2s">
            <div className="row align-items-center">
              <div className="col-3 col-md-12 pr-0">
                <img src="/assets/images/process-icon-2.png" className="processIcon img-fluid" />
              </div>
              <div className="col col-md-12 pr-0">
                <div>
                  <h5 className="mb-0">Apply</h5>
                </div>
              </div>
            </div>
          </div>
          <div className="singleProcess col-11 col-md-4 wow fadeInUp" data-wow-delay="0.3s">
            <div className="row align-items-center">
              <div className="col-3 col-md-12 pr-0">
                <img src="/assets/images/process-icon-3.png" className="processIcon img-fluid" />
              </div>
              <div className="col col-md-12 pr-0">
                <div>
                  <h5 className="mb-0">You're hired!</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CareerWorks;

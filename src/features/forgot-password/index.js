import { Link } from "react-router-dom";

import { BodyInfo, CareerWorks } from "../../commons";


const ForgotPassword = () => {
  return (
    <>
      <div className="bodyContents pt-0">
        <section className="bodyContents-section -bg-light py-6">
          <div className="container">
            <div className="row">
              <div className="col-md-6 order-2 wow fadeInUp" data-wow-delay="0s">
                <h3 className="h3">Forgot Password</h3>
                <div ng-show="!forgotpassword.showSuccessInfo">
                  <form autoComplete="off" name="forgotpassword.frmForgotPassword" className="wow fadeInUp" data-wow-delay="0s" ng-submit="forgotpassword.submit(forgotpassword.param)">
                    <div className="alert alert-{{forgotpassword.display.alert_type}}" ng-show="forgotpassword.display.status!=''">
                      <b><i ng-class="forgotpassword.display.icon"></i></b> <span ng-bind="forgotpassword.display.message"></span>
                    </div>
                    <hr className="my-4" />
                    <div className="m-input-container">
                      <input id="email" type="email" autoComplete="off" maxLength="50" className="input-text form-control" ng-model="forgotpassword.param.email" required />
                      <label className="label" htmlFor="email">Email Address</label>
                    </div>
                    <div className="d-flex justify-content-center my-4">
                      <div
                        // vc-recaptcha
                        theme="'light'" key="forgotpassword.key"
                      // on-create="forgotpassword.setWidgetId(widgetId)"
                      // on-success="forgotpassword.setResponse(response)"
                      // on-expire="forgotpassword.cbExpiration()"
                      ></div>
                    </div>
                    <input type="submit" className="btn btn-secondary  btn-lg btn-block" value="Submit" />
                  </form>
                </div>
                <div ng-show="forgotpassword.showSuccessInfo" className="col-md-12">
                  <div className="text-center">
                    <div className="content booking-box fc-gray-dark " style={{ 'padding': '10px' }}>
                      <h5 className="fw-600" style={{ 'color': 'green' }}>Forgot Password Successfully Reset!</h5>
                      <p>We have sent a temporary password to <b ng-bind="forgotpassword.param.email"></b>, for you to be able to logged on.</p>
                      <br />
                      <p className="mb-1"><Link to="/signin" style={{ 'fontSize': '1rem' }}>Click here to sign in.</Link></p>
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-6 order-1 d-flex align-items-center wow fadeInUp" data-wow-delay="0s">
                <img src="/assets/images/ayala/sign-in-image.png" alt="" className="img-fluid p-5" />
              </div>
            </div>
          </div>
        </section>
        <CareerWorks />
        <BodyInfo />
      </div>
      <div className="push"></div>
    </>
  );
};

export default ForgotPassword;

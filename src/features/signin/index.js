import { Link } from "react-router-dom";

import { BodyInfo, CareerWorks } from "../../commons";


const SignIn = () => {
  window.scrollTo(0, 0);

  return (
    <>
      <div className="bodyContents pt-0">
        <section className="bodyContents-section -bg-light py-6">
          <div className="container">
            <div className="row">
              <div className="col-md-6 order-2 wow fadeInUp" data-wow-delay="0.3s">
                <h3 className="h3">
                  Sign in to your <br />
                  Ayala Careers account
                </h3>
                <form autoComplete="off" name="signin.loginForm" className="wow fadeInUp" data-wow-delay="0s" ng-class="{'was-validated': signin.loginForm.$submitted}">
                  <div className="alert alert-{{signin.display.alert_type}}" ng-show="signin.display.status">
                    <b><i ng-class="signin.display.icon"></i></b> <span ng-bind="signin.display.message"></span>
                  </div>
                  <hr className="my-4" />
                  <div className="m-input-container">
                    <input id="emailnumber" type="text" autoComplete="off" className="input-text form-control" ng-model="signin.params.username" required />
                    <label className="label" htmlFor="emailnumber">Email Address</label>
                  </div>
                  <div className="m-input-container">
                    <input id="password" type="password" autoComplete="off" className="input-text form-control" ng-model="signin.params.password" required />
                    <label className="label" htmlFor="password">Password</label>
                  </div>
                  <p className="mb-1">
                    <small><Link to="/forgotpassword">Forgot password? Click here.</Link></small>
                  </p>
                  <input type="submit" className="btn btn-secondary btn-lg btn-block" value="Sign in" ng-click="signin.authenticate(signin.params)" />
                </form>
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

export default SignIn;

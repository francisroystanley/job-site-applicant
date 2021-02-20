import { Link } from "react-router-dom";


const ErrorPage = () => {
  window.scrollTo(0, 0);

  return (
    <>
      <section className="bodyContents-section">
        <div className="content">
          <div className="card-body">
            <div className="row">
              <div className="col-md-6 ml-auto mr-auto col-sm-12">
                <h4> <i className="far fa-frown-open" aria-hidden="true"></i> 404 Page Not Found</h4>
                <p>You seem to be lost. The page you are looking for does not exist or you do not have permission.</p>
                <p>Click <Link to="/">here</Link> to redirect to home page.</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <div className="push"></div>
    </>
  );
};

export default ErrorPage;

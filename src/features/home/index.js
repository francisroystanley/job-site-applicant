import { memo, useContext, useEffect, useState } from "react";
import PropTypes from "prop-types";
import { Carousel, Container } from "react-bootstrap";
import { createSelector } from "reselect";
import { useDispatch, useSelector } from "react-redux";

import { BodyInfo, BodyInfoVideo, JobCardsList, query, SearchEngine, timeAgo } from "../../commons";
// import { BusinessUnit } from "../../context";

import allSM from "../../assets/images/homepageCarousel/AllSM.jpg";
import processIcon1 from "../../assets/images/process-icon-1.png";
import processIcon2 from "../../assets/images/process-icon-2.png";
import processIcon3 from "../../assets/images/process-icon-3.png";
import SMCinema from "../../assets/images/homepageCarousel/SMCinema-home.jpg";
import SMDC from "../../assets/images/homepageCarousel/SMDC-home.jpg";
import EDD from "../../assets/images/homepageCarousel/SMEDD-home.jpg";
import SMLI from "../../assets/images/homepageCarousel/SMLEI-home.jpg";
import PRIME from "../../assets/images/homepageCarousel/SMPRIME-home.jpg";
import SCMC from "../../assets/images/homepageCarousel/Supermalls-home.jpg";
import emptyBanner from "../../assets/images/empty-banner.jpg";
import getBusinessUnit from "../../selectors";
import setBusinessUnit from "../../actions";


const stateSelector = createSelector(getBusinessUnit, state => state);

const actionDispatch = (dispatch) => ({
  setEntities: data => dispatch(setBusinessUnit(data))
});

const Home = () => {
  const jobLevel = [
    { code: 'FRESHGRAD_ENTRY', name: 'Fresh Graduate' },
    { code: 'RANK_FILE', name: 'Rank and File' },
    { code: 'TECH_STAFF_OFFCR', name: 'Technical Staff / Officer' },
    { code: 'ASSOC_SUPVR', name: 'Supervisor' },
    { code: 'MIDSR_MNGR', name: 'Manager' },
    { code: 'SR_MNGR', name: 'Senior Manager' },
    { code: 'DIR_EXEC', name: 'Executive' }
  ];

  // let entities = useContext(BusinessUnit);
  const entities = useSelector(stateSelector);
  const { setEntities } = actionDispatch(useDispatch());
  const [jobAd, setJobAd] = useState([]);
  const [jobClass, setJobClass] = useState([]);

  useEffect(async () => {
    getBusinessUnit();
    await getJobClass();
    await getJobAd();
  }, [entities]);

  const getBusinessUnit = () => {
    entities.forEach(entity => {
      entity.code = entity.businessunit_code;
      entity.name = entity.businessunit_name;
      if ("SMC".indexOf(entity.code) >= 0) {
        entity.home_image = SMCinema;
      } else if (entity.code.indexOf("SMDC") >= 0) {
        entity.home_image = SMDC;
      } else if (entity.code.indexOf("EDD") >= 0) {
        entity.home_image = EDD;
      } else if (entity.code.indexOf("SMLI") >= 0) {
        entity.home_image = SMLI;
      } else if (entity.code.indexOf("PRIME") >= 0) {
        entity.home_image = PRIME;
      } else if (entity.code.indexOf("SCMC") >= 0) {
        entity.home_image = SCMC;
      } else {
        entity.home_image = emptyBanner;
      }
    });
    // setEntities(entities);
  };

  const getJobAd = async () => {
    let jobad_data = {
      filter: {
        limit: 9,
        order_by: 'date_updated desc'
      },
      status: 'OPEN'
    };
    try {
      const res = await fetch("/api/job_ad" + query(jobad_data));
      let data = await res.json();
      if (data.status == "SUCCESS") {
        data.job_ad.forEach(jobad => {
          let date_posted = new Date(jobad.date_updated);
          jobad.postDate = timeAgo(date_posted);
          let filtered_job_level = jobLevel.filter(jlevel => jobad.job_level == jlevel.code)[0];
          if (filtered_job_level) {
            jobad.job_level_name = filtered_job_level.name;
          }
          let filtered_job_class = jobClass.filter(jclass => jobad.job_class == jclass.job_class_code)[0];
          if (filtered_job_class) {
            jobad.job_class_name = filtered_job_class.job_class_name;
          }
          let filtered_entity = entities.filter(entity => jobad.businessunit_id == entity.id)[0];
          if (filtered_entity) {
            jobad.businessunit = filtered_entity;
          }
        });
        setJobAd(data.job_ad);
      } else {
        showOkModal("Error", "Something went wrong");
      }
      return;
    } catch (err) {
      showOkModal("Error", "Something went wrong");
      return;
    }
  };

  const getJobClass = async () => {
    try {
      const res = await fetch("/api/job_class");
      const data = await res.json();
      if (data.status == "SUCCESS") {
        setJobClass(data.job_class);
      } else {
        console.log(err);
        showOkModal("Error", "Something went wrong");
      }
      return;
    } catch (err) {
      showOkModal("Error", "Something went wrong");
      return;
    }
  };

  return (
    <>
      <header className="main-header dark-bg">
        <div className="headerContents mb-0 pb-0">
          <Container>
            <Carousel id="homepageCarousel" interval={3000} className="pb-4 mb-0">
              <Carousel.Item>
                <a>
                  <img className="d-block mx-auto w-90" src={allSM} alt="SM Cinema" />
                </a>
              </Carousel.Item>
              {entities.map((entity, idx) => (
                <Carousel.Item key={idx}>
                  <a>
                    <img className="d-block mx-auto w-90" src={entity.home_image} alt={entity.businessunit_name} />
                  </a>
                </Carousel.Item>
              ))}
            </Carousel>
          </Container>
        </div>
        <div className="container-fluid mt-0 mt-md-2 px-md-2 px-lg-5 px-xl-5">
          <SearchEngine />
        </div>
      </header>
      <div className="bodyContents">
        <section className="bodyContents-section">
          <div className="container">
            <div className="row">
              <div className="col-md-10 offset-md-1 text-center wow fadeInUp" data-wow-delay="0s">
                <h3 className="h3">How SM career works?</h3>
                <p className="lead">
                </p>
              </div>
            </div>
            <div className="our-process row justify-content-center">
              <div className="singleProcess col-11 col-md-4 wow fadeInUp" data-wow-delay="0.1s">
                <div className="row align-items-center">
                  <div className="col-3 col-md-12 pr-0">
                    <img src={processIcon1} className="processIcon img-fluid" />
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
                    <img src={processIcon2} className="processIcon img-fluid" />
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
                    <img src={processIcon3} className="processIcon img-fluid" />
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
        <section className="bodyContents-section">
          <div id="jobCards" className="jobCards container">
            <div className="d-flex flex-wrap justify-content-between align-items-center wow fadeInUp" data-wow-delay="0s">
              <div className="my-1 mr-5">
                <h3 className="h3 mb-0">Latest careers</h3>
              </div>
              <div className="my-1">
                <a className="d-block withIcon viewAll bg-transparent">View all jobs<i className="fa fa-angle-right ml-19" aria-hidden="true"></i></a>
              </div>
            </div>
            <JobCardsList list={jobAd} />
          </div>
        </section>
        <BodyInfoVideo />
        <BodyInfo />
      </div>
      <div className="push"></div>
    </>
  );
};

Home.propTypes = {};

export default memo(Home);

import { memo, useEffect, useState } from "react";
import PropTypes from "prop-types";
import { Container } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { BodyInfo, CareerWorks, JobCardsList, SearchEngine } from "../../../commons";
import { getJobAd } from "../../../slices/jobAd";
import { timeAgo, titlecase } from "../../../functions";


const AyalaLand = ({ location }) => {
  const dispatch = useDispatch();
  const entities = useSelector(({ businessUnit }) => businessUnit);
  const entity = titlecase(location.pathname.split('/')[2].split('-').join(' '));
  const entity_photo = [
    '/assets/images/ayala/ayala-land-1.jpg',
    '/assets/images/ayala/ayala-land-2.jpg',
    '/assets/images/ayala/ayala-land-3.jpg',
    '/assets/images/ayala/ayala-land-4.png'
  ];
  const env = useSelector(({ env }) => env);
  const [jobAd, setJobAd] = useState([]);
  const jobClass = useSelector(({ jobClass }) => jobClass);
  const jobLevel = useSelector(({ jobLevel }) => jobLevel);
  const provinces = useSelector(({ province }) => province);

  useEffect(async () => {
    window.scrollTo(0, 0);
    getAds();
  }, [provinces, entities, jobClass]);

  const getAds = async () => {
    let jobad_data = {
      filter: {
        limit: 9,
        order_by: 'date_updated desc'
      },
      status: 'OPEN'
    };
    dispatch(getJobAd(jobad_data)).then(({ payload }) => {
      payload.forEach(jobad => {
        let date_posted = new Date(jobad.date_updated);
        jobad.postDate = timeAgo(date_posted);
        jobad.randNum = 0;
        let filtered_province = provinces.filter(prov => jobad.province_code == prov.province_code)[0];
        if (filtered_province) {
          jobad.province = filtered_province;
        }
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
      setJobAd(payload);
    });
  };

  return (
    <>
      <header className="main-header dark-bg">
        <Container>
          <h3 className="pt-4 mb-0 page-title wow fadeInUp" data-wow-delay="0.15s">{entity}</h3>
        </Container>
        <div className="companyPageBanner mt-4 mt-md-4">
          <Container>
            {env.slides && <img src={env.slides[0].image} alt="" className="img-fluid wow fadeInUp" data-wow-delay="0.1s" />}
          </Container>
        </div>
        <div className="container-fluid mt-0 mt-md-2 px-md-2 px-lg-5 px-xl-5">
          <SearchEngine />
        </div>
      </header>
      <div className="bodyContents">
        <CareerWorks />
        <section className="bodyContents-section">
          <div id="jobCards" className="jobCards container">
            <div className="d-flex flex-wrap justify-content-between align-items-center wow fadeInUp" data-wow-delay="0s">
              <div className="my-1 mr-5">
                <h3 className="h3 mb-0">Latest Ayala Land Jobs</h3>
              </div>
              <div className="my-1">
                <Link to="/career" className="d-block withIcon viewAll bg-transparent">View all jobs<i className="fa fa-angle-right ml-19" aria-hidden="true"></i></Link>
              </div>
            </div>
            <JobCardsList list={jobAd} />
          </div>
        </section>
        <section className="bodyContents-section mb-5">
          <div className="container">
            <div className="row">
              <div className="col-lg-5 wow fadeInUp" data-wow-delay="0s">
                <h3>About <span>{entity}</span></h3>
                <div>
                  <p className="lead font-weight-normal">
                    Ayala Land, Inc. was the real estate division of Ayala Corporation until it fully branched out on its own in 1988. Its beginnings are anchored on the development of Makati. Having seen the potential in a large, uncharted land known as Hacienda Makati. The company then created a unique masterplan for the area, which has now evolved into the leading financial and central business district in the Philippines.
                  </p>
                  <p className="lead font-weight-normal">
                    Ayala Land became publicly listed through an offering of its primary and secondary shares on the Makati and Manila Stock Exchanges in July of 1991. The company also offers services in property management and construction while its core businesses are rooted in strategic landbank management, residential development, retail shopping centers, offices, and hotels & resorts.
                  </p>
                </div>
              </div>
              <div className="col-lg-7 about-us wow fadeInUp" data-wow-delay="0.1s">
                <div class="row no-gutters justify-content-center about-us-5">
                  {entity_photo.map(photo => <img src={photo} />)}
                </div>
              </div>
            </div>
          </div>
        </section>
        <BodyInfo />
      </div>
      <div className="push"></div>
    </>
  );
};

AyalaLand.propTypes = {};

export default AyalaLand;

import { memo, useEffect, useState } from "react";
import PropTypes from "prop-types";
import { Carousel, Container } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { BodyInfo, BodyInfoVideo, CareerWorks, JobCardsList, SearchEngine } from "../../commons";
import { getJobAd } from "../../slices/jobAd";
import { timeAgo } from '../../functions';


const Home = () => {
  const dispatch = useDispatch();
  const env = useSelector(({ env }) => env);
  const entities = useSelector(({ businessUnit }) => businessUnit);
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
        jobad.randNum = Math.floor(Math.random() * 4);
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
        <div className="headerContents mb-0 pb-0">
          <Container>
            <Carousel id="homepageCarousel" interval={2500} className="pb-4 mb-0">
              {env.slides && env.slides.map((entity, idx) => (
                <Carousel.Item key={idx} style={{ 'maxHeight': '600px' }}>
                  <img className="d-block mx-auto w-90" src={entity.image} alt={entity.name} />
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
        <CareerWorks />
        <section className="bodyContents-section">
          <div id="jobCards" className="jobCards container">
            <div className="d-flex flex-wrap justify-content-between align-items-center wow fadeInUp" data-wow-delay="0s">
              <div className="my-1 mr-5">
                <h3 className="h3 mb-0">Latest Jobs</h3>
              </div>
              <div className="my-1">
                <Link to="/career" className="d-block withIcon viewAll bg-transparent">View all jobs<i className="fa fa-angle-right ml-19" aria-hidden="true"></i></Link>
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

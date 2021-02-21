import PropTypes from 'prop-types';


const JobCardsList = ({ list }) => {
  const bu = [
    { name: 'Ayala Land', logo: '/assets/images/ayala/ayala-land.svg' },
    { name: 'BPI', logo: '/assets/images/ayala/bpi.svg' },
    { name: 'Globe Telecom', logo: '/assets/images/ayala/globe-telecom.svg' },
    { name: 'Manila Water', logo: '/assets/images/ayala/manila-water.svg' }
  ];

  return (
    <ul className="jobCards-list row">
      {list.map((jobad, idx) => (
        <li className="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.1s" key={idx}>
          <div className="jobCard-body">
            <div className="meta d-flex justify-content-between">
              <span className="status">Trending now</span>
              <span className="postDate">{jobad.postDate}</span>
            </div>
            <div className="company">
              <div className="agencyLogo">
                {/* {jobad.businessunit && <img src={jobad.businessunit.logo_image} />} */}
                <img src={bu[jobad.randNum].logo} />
              </div>
              {/* {jobad.businessunit && <h4 className="h4 agencyName">{jobad.businessunit.businessunit_name}</h4>} */}
              {<h4 className="h4 agencyName">{bu[jobad.randNum].name}</h4>}
            </div>
            <div className="details row">
              <div className="col-12 mb-2 positionTitle visible d-flex justify-content-center align-items-center" id="jobad_jobtitle">
                <span className="line-clamp text-break">{jobad.job_title}</span>
              </div>
              {jobad.province && <div className="location col-12">{jobad.province.province_name + ', PHILIPPINES'}</div>}
              <ul className="description col-12 row justify-content-center align-items-center" id="jobad_description">
                {jobad.job_level_name && <li className="mb-0 col-12">{jobad.job_level_name}</li>}
                {jobad.job_class_name && <li className="mb-0 col-12">{jobad.job_class_name}</li>}
              </ul>
            </div>
            <div className="links d-flex justify-content-between">
              <a href="">Learn more</a>
              <a href="" className="btn btn-lg btn-outline-primary">Apply now!</a>
            </div>
          </div>
        </li>
      ))}
    </ul>
  );
};

JobCardsList.propTypes = {
  list: PropTypes.array
};

JobCardsList.defaultProps = {
  list: []
};

export default JobCardsList;

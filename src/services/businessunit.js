import Axios from "axios";


const BusinessUnitSrvc = () => {
  const get = data => Axios.get('/api/businessunit', { params: data });
  const getPhoto = data => Axios.get(`/api/businessunit/${ data.businessunit_id }/photo`, { params: data });

  return {
    get,
    getPhoto
  };

};

export default BusinessUnitSrvc();

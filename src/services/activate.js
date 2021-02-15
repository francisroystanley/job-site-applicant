import Axios from "axios";


const ActivateSrvc = () => {
  return {
    activate: activate
  };

  const activate = data => Axios.post('/api/activate', data);
};

export default ActivateSrvc;

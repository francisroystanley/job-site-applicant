import ActionType from './home.constants';


const setBusinessUnit = (bu) => (
  {
    type: ActionType.SET_BUSINESSUNIT,
    payload: bu
  }
);

export default setBusinessUnit;

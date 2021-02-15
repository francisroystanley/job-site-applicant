import ActionType from './home.constants';


const defaultState = {
  env: {},
  jobClass: [],
  businessUnit: [],
  jobAds: []
};

const homeReducer = (state = defaultState, action) => {
  switch (action.type) {
    case ActionType.SET_BUSINESSUNIT:
      return { ...state, businessunit: action.payload };
    default:
      return state;
  }
};

export default homeReducer;

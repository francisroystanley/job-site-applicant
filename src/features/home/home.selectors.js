import { createSelector } from "reselect";


const home = (state) => state.homeReducer;
const makeSelectBusinessUnit = createSelector(home, home => home.businessUnit);

export default makeSelectBusinessUnit;

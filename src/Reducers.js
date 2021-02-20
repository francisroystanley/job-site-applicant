import businessUnitSlice from './slices/businessUnit';
import envSlice from "./slices/env";
import jobClassSlice from "./slices/jobClass";


const reducer = {
  businessUnit: businessUnitSlice.reducer,
  env: envSlice.reducer,
  jobClass: jobClassSlice.reducer
};

export default reducer;

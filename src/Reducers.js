import businessUnitSlice from './slices/businessUnit';
import envSlice from "./slices/env";
import jobClassSlice from "./slices/jobClass";
import jobLevelSlice from "./slices/jobLevel";
import provinceSlice from "./slices/province";


const reducer = {
  businessUnit: businessUnitSlice.reducer,
  env: envSlice.reducer,
  jobClass: jobClassSlice.reducer,
  jobLevel: jobLevelSlice.reducer,
  province: provinceSlice.reducer
};

export default reducer;

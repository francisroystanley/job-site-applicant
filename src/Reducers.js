import businessunitSlice from './slices/businessunit';
import envSlice from "./slices/env";


const reducer = {
  businessunit: businessunitSlice.reducer,
  env: envSlice.reducer
};

export default reducer;

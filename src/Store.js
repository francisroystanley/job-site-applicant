import { configureStore } from '@reduxjs/toolkit';
import reducer from './Reducers';


const store = configureStore({
  reducer
});

export default store;

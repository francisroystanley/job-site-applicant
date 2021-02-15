import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import Axios from "axios";


export const getBusinessUnit = createAsyncThunk('businessunit/get', (data) =>
  Axios.get('/api/businessunit', { params: data })
    .then(res => res.data.businessunit)
    .catch(err => {
      console.log("ERROR: ", err);
      throw new Error(err);
    })
);

const businessunitSlice = createSlice({
  name: 'businessunit',
  initialState: [],
  reducers: {
    // add: (state, { payload }) => console.log(state, payload),
    // get: async (state, { payload }) => {
    //   const response = await Axios.get('/api/businessunit', { params: payload });
    //   return response;
    // },
    // getPhoto: (state, { payload }) => {
    //   const getPhoto = data => Axios.get(`/api/businessunit/${ payload.businessunit_id }/photo`, { params: payload });
    // },
    // remove: (state, { payload }) => console.log(state, payload),
    getList: (state, { payload }) => console.log(state, payload),
    updateList: (state, { payload }) => payload
  },
  extraReducers: {
    // [getBusinessUnit.pending]: (state, action) => {
    // },
    // [getBusinessUnit.fulfilled]: (state, { payload }) => state,
    [getBusinessUnit.rejected]: (state, action) => {
      console.log("rejected: ", action);
    }
  }
});

export const {
  //   add: addBusinessUnit,
  //   getPhoto: getBusinessUnitPhoto,
  //   remove: removeBusinessUnit,
  updateList: updateBusinessUnitList
} = businessunitSlice.actions;

export default businessunitSlice;

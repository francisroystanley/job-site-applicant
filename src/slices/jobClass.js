import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import Axios from "axios";


export const getJobClass = createAsyncThunk('jobclass/get', (data) =>
  Axios.get('/api/job_class', { params: data })
    .then(res => res.data.job_class)
    .catch(err => {
      console.log("ERROR: ", err);
      throw new Error(err);
    })
);

const jobClassSlice = createSlice({
  name: 'jobclass',
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
    // getList: (state, { payload }) => console.log(state, payload),
    updateList: (state, { payload }) => payload
  },
  extraReducers: {
    [getJobClass.fulfilled]: (state, { payload }) => payload,
    [getJobClass.rejected]: (state, action) => {
      console.log("rejected: ", action);
    }
  }
});

export const {
  //   add: addBusinessUnit,
  //   getPhoto: getBusinessUnitPhoto,
  //   remove: removeBusinessUnit,
  updateList: updateJobClass
} = jobClassSlice.actions;

export default jobClassSlice;

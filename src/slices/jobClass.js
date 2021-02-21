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
  reducers: {},
  extraReducers: {
    [getJobClass.fulfilled]: (state, { payload }) => payload,
    [getJobClass.rejected]: (state, action) => {
      console.log("rejected: ", action);
    }
  }
});

export default jobClassSlice;

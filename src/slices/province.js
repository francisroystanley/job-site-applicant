import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import Axios from "axios";


export const getProvince = createAsyncThunk('province/get', (data) =>
  Axios.get('/api/province', { params: data })
    .then(res => res.data.provinces)
    .catch(err => {
      console.log("ERROR: ", err);
      throw new Error(err);
    })
);

const provinceSlice = createSlice({
  name: 'province',
  initialState: [],
  reducers: {},
  extraReducers: {
    [getProvince.fulfilled]: (state, { payload }) => payload,
    [getProvince.rejected]: (state, action) => {
      console.log("rejected: ", action);
    }
  }
});

export default provinceSlice;

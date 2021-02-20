import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import Axios from "axios";


export const getEnv = createAsyncThunk('env/get', data =>
  Axios.get('/api/env', { params: data })
    .then(res => res.data.env)
    .catch(err => {
      console.log("ERROR: ", err);
      throw new Error(err);
    })
);

const envSlice = createSlice({
  name: 'env',
  initialState: { showCookieConsent: true },
  reducers: {
    updateState: (state, { payload }) => ({ ...state, ...payload })
  },
  extraReducers: {
    [getEnv.fulfilled]: (state, { payload }) => ({ ...state, ...payload }),
    [getEnv.rejected]: (state, action) => {
      console.log("rejected: ", action);
    }
  }
});

export const {
  updateState: updateEnvState
} = envSlice.actions;

export default envSlice;

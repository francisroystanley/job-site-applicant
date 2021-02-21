import { memo, useEffect } from "react";
import { useDispatch } from "react-redux";

import { getBusinessUnit, updateBusinessUnitList } from './slices/businessUnit';
import { getEnv } from "./slices/env";
import { getJobClass } from "./slices/jobClass";
import { getProvince } from "./slices/province";


const InitState = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getEnv());
    dispatch(getBusinessUnit()).then(({ payload }) => dispatch(updateBusinessUnitList(payload)));
    dispatch(getJobClass());
    dispatch(getProvince());
  }, []);

  return null;
};

export default memo(InitState);

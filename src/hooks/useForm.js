import { useState } from "react";

const useForm = initVal => {
  const [values, setValues] = useState(initVal);

  return [values, e => setValues({ ...values, [e.target.name]: e.target.value })];
};

export default useForm;

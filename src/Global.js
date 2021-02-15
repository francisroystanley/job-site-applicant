const client_code = process.env.REACT_APP_CLIENT_CODE;

const getEnv = async () => {
  const data = await import(`./custom/js/${ client_code.toLowerCase() }`);
  return data.default;
};

export default getEnv;

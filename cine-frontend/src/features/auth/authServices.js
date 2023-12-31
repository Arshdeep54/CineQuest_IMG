import axios from 'axios';
import 'dotenv/config';
const BACKEND_URL = ' ${process.env.REACT_APP_API_URL}';
const REGISTER_URL = 'auth/user/register';
const LOGIN_URL = 'auth/user/login';

const register = async (userData) => {
  const config = {
    headers: {
      'Content-type': 'application/json',
    },
  };
  const response = await axios.post(REGISTER_URL, userData, config);
  return response.data;
};

const login = async (loginData) => {
  const config = {
    headers: {
      'Content-type': 'application/json',
    },
  };
  const response = await axios.post(REGISTER_URL, loginData, config);
  return response.data;
};

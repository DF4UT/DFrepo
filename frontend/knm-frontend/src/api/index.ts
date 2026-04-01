import axios from 'axios'

const api = axios.create({
    timeout: 10000,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
  baseURL: '/api',
})
export default api
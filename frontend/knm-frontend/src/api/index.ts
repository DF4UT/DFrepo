import axios from 'axios'

const api = axios.create({
    timeout: 10000,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
  baseURL: '/api',
})

const apiGet = (url: string) => {
  api.get(url).then((response) => {
    console.log(response.data)
  }).catch((error) => {
    console.error(error)
  }
}

const apiPost = (url: string, data: any) => {
  api.post(url, data).then((response) => {
    console.log(response.data)
  }).catch((error) => {
    console.error(error)
  }
}

export default api
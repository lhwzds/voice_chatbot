import axios from 'axios';

const Axios = axios.create({
    baseURL: '',
    timeout: 100000,
    headers: { 
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    withCredentials: true
});

Axios.interceptors.request.use(req => {
    return req; 
}, err => {
    console.log('request发生error,', err);
    return Promise.reject(err);
})

Axios.interceptors.response.use(res => {
    return res.data;
}, error => {
    const err = error.toString();
    switch (true) {
        case err.indexOf('Network') !== -1:
            console.log('response为Network error,', err);
            break;
        case err.indexOf('timeout') !== -1:
            console.log('response为Timeout error,', err);
            break;
    }
    return Promise.reject(error);
})
export default Axios;
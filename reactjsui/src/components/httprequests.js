import axios from 'axios';


const headerData = {
    header: {
        'Content-Type': 'application/json'
    }
}
const bodyData = {}

export const httprequestPostRequst = async (url, body = bodyData, header = headerData) => {
    let urlsss = `http://127.0.0.1:8000/api/${url}`
    try {
        const { data } = await axios.post(urlsss, body, header)
        console.log("httprequest=+++>", data);
        return data;
    } catch (e) {
        console.log(e);
    }
}

export const httprequestGetRequst = async (url, body = bodyData, header = headerData) => {
    let urlsss = `http://127.0.0.1:8000/api/${url}`
    try {
        const { data } = await axios.get(urlsss, body, header)
        console.log("httprequest=+++>", data);
        return data;
    } catch (e) {
        console.log(e);
    }
}
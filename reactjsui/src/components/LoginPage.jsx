import React, { useState } from 'react'
import { httprequestPostRequst } from './httprequests'
import cookie from 'react-cookies'
import { State } from '../GlobalState/StateProvider'

const LoginPage = () => {
    const [{ }, dispatch] = State();
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const body = {
        "username": username,
        "password": password
    }
    const header = {
        header: {
            'Content-Type': 'application/json'
        }
    }

    const loginNow = async (e) => {
        e.preventDefault();
        const data = await httprequestPostRequst('login/', body, header)
        if (data) {
            cookie.save('userToken', data?.token)
            console.log("Login======>", data);
            dispatch({
                type: "SET_TOKEN",
                token: cookie.load('userToken')
            });
        }
        else {
            alert("Invalid Data")
        }
    }

    return (
        <div className="container">
            <div className="row mt-5 justify-content-center">
                <div className="col-md-4">
                    <div className="form-group">
                        <label for="exampleInputEmail1">Username</label>
                        <input onChange={(e) => setUsername(e.target.value)} type="text" className="form-control" id="exampleInputEmail1" placeholder="Enter Username" />
                    </div>
                    <div className="form-group">
                        <label for="exampleInputPassword1">Password</label>
                        <input onChange={(e) => setPassword(e.target.value)} type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" />
                    </div>
                    <button onClick={loginNow} className="btn btn-primary">Login</button>
                    <div>
                        <h2>{username}</h2>
                        <h2>{password}</h2>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default LoginPage

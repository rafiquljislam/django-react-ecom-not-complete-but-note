import axios from 'axios';
import React, { useEffect } from 'react'
import { State } from '../GlobalState/StateProvider';

const Profile = () => {

    const [{ profile, user }, dispatch] = State()

    useEffect(() => {
        const fatchdata = async () => {
            const { data } = await axios.get(`http://127.0.0.1:8000/api/customer/`, {
                headers: {
                    'Authorization': `token 1ad4f0e25579b5f45af26629a932a7472682eb49`
                }
            });
            console.log(data);
            dispatch({
                type: "SET_PROFILE",
                profile: data
            })
        };
        const fatchuser = async () => {
            const { data } = await axios.get(`http://127.0.0.1:8000/api/user/`, {
                headers: {
                    'Authorization': `token 1ad4f0e25579b5f45af26629a932a7472682eb49`
                }
            });
            console.log(data);
            dispatch({
                type: "SET_USER",
                user: data
            })
        };
        fatchdata();
        fatchuser();
    }, [])

    return (
        <div className="container" >
            {
                profile != null & user != null ? (
                    <>
                        <img src={`http://127.0.0.1:8000${profile.image}`} alt="" />
                        <h2>username=={user.username}</h2>
                        <h2>email=={user.email}</h2>
                        <h2>first_name=={user.first_name}</h2>
                        <h2>last_name=={user.last_name}</h2>
                    </>
                ) : (
                        <p>Loding....</p>
                    )
            }
        </div>
    )
}

export default Profile

import Axios from 'axios';
import React, { useEffect } from 'react'
import { State } from '../GlobalState/StateProvider';

const Carts = () => {

    const [{ cart }, dispatch] = State()


    useEffect(() => {
        const fatchdata = async () => {
            const { data } = await Axios.get('http://127.0.0.1:8000/api/cart/', {
                headers: {
                    'Authorization': `token 1ad4f0e25579b5f45af26629a932a7472682eb49`
                }
            });
            console.log(data);
            dispatch({
                type: 'SET_CART',
                cart: data
            })
        };
        fatchdata();
    }, [])


    return (
        <div className="container">
            <div className="row">
                {
                    cart?.map((data, i) => (
                        <div key={i} className="col-md-6">
                            <p>creted at : {data.credted_at}</p>
                            <p>id : {data.id}</p>
                            <h2>total : {data.total}</h2>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default Carts

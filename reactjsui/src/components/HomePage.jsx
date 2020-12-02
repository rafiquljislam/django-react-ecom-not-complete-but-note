import React, { useEffect } from 'react'
import { Link } from 'react-router-dom';
import { State } from '../GlobalState/StateProvider';
import { httprequestGetRequst } from './httprequests'

const HomePage = () => {

    const [{ products }, dispatch] = State();


    useEffect(() => {
        const fatchdata = async () => {
            const data = await httprequestGetRequst('products/',);
            dispatch({
                type: "SET_PRODUCT",
                products: data
            })
        };
        fatchdata()
    }, [])






    console.log(products);
    return (
        <div className="container">
            <div className="row my-3">
                {
                    products?.map((data, i) => (
                        <div className="col-md-4 mt-1 " >
                            <div key={i} className="card" >
                                <img className="card-img-top home__cart_image" src={data.image} alt="Card image cap" />
                                <div className="card-body">
                                    <h5 className="card-title">{data.title}</h5>
                                </div>
                                <div className="card-footer text-muted">
                                    <Link className="btn btn-outline-info mx-2" to={`/${data.slug}/${data.id}`}>details</Link>
                                    <Link className="btn btn-outline-info" to="">Add to cart</Link>
                                </div>
                            </div>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default HomePage

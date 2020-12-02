import React, { useEffect, useState } from 'react'
import { httprequestGetRequst } from './httprequests'

const ProductDetail = (props) => {
    const prodid = props.match.params.id
    const [product, setProduct] = useState({});
    const [catagory, setcatagory] = useState({});

    useEffect(() => {
        const fatchdata = async () => {
            const data = await httprequestGetRequst(`products/${prodid}`);
            setProduct(data)
        };
        fatchdata()
    }, [])

    useEffect(() => {
        const fatchdata = async () => {
            const data = await httprequestGetRequst(`catagorys/${product?.catagory}/`);
            // const data = await httprequestGetRequst(`catagorys/${product.catagory}/`);
            setcatagory(data)
        };
        fatchdata()
    }, [])

    return (
        <div className="container">
            <div className="card my-3">
                <img className="card-img-top carddetails__image" src={product.image} alt="Card image cap" />
                <div className="card-body">
                    <h5 className="card-title">title=={product.title}</h5>
                    <p className="card-text">description=={product.description}</p>
                    <p className="card-text"><small className="text-muted">pub_date=={product.pub_date}</small></p>
                    <p className="card-text"> <del>marcked_price=={product.marcked_price}</del> </p>
                    <p className="card-text">selling_price== {product.selling_price}</p>
                    <p className="card-text">warranty == {product.warranty} </p>
                    <p className="card-text">return_policy== {product.return_policy} </p>
                    <p className="card-text">catagory== {catagory?.title} </p>
                </div>
                <div className="card-footer">
                    <button className="btn btn-info">Ordernow now</button>
                </div>
            </div>
        </div>
    )
}

export default ProductDetail

import React from 'react'
import { State } from '../GlobalState/StateProvider'
import { Link } from 'react-router-dom'
import cookie from 'react-cookies'

const Navbar = () => {
    const [{ token, cart }, dispatch] = State()

    const logoutFunction = (e) => {
        e.preventDefault();
        cookie.remove('userToken');
        dispatch({
            type: "SET_TOKEN",
            token: null
        });
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <Link className="navbar-brand" to="/">Navbar</Link>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div className="navbar-nav">
                    <Link className="nav-link" to="#">Features</Link>
                    <Link className="nav-link" to="#">Pricing</Link>
                </div>
                <div className="navbar-nav ml-auto">
                    {
                        token != null ? (
                            <>
                                <Link className="nav-link" to="/cart">Cart({cart?.length ?? 0})</Link>
                                <Link className="nav-link" to="/profile">Profile</Link>
                                <Link className="nav-link" onClick={logoutFunction} >Logout</Link>
                            </>
                        ) : (
                                <>
                                    <Link className="nav-link" to="/">Login</Link>
                                    <Link className="nav-link" to="#">Register</Link>
                                </>
                            )
                    }
                </div>
            </div>
        </nav>
    )
}

export default Navbar

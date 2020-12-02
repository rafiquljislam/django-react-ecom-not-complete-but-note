import { State } from './GlobalState/StateProvider';
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Navbar from './components/Navbar';
import LoginPage from './components/LoginPage';
import HomePage from './components/HomePage';
import { useEffect } from 'react';
import cookie from 'react-cookies'
import ProductDetail from './components/ProductDetail';
import Profile from './components/Profile';
import Carts from './components/Carts';



function App() {
  const [{ token }, dispatch] = State();

  useEffect(() => {
    dispatch({
      type: "SET_TOKEN",
      token: cookie.load('userToken')
    });
  }, [])


  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Switch>
          {
            token != null ?
              (
                <Route exact path="/" component={HomePage} />
              )
              :
              (
                <Route exact path="/" component={LoginPage} />
              )
          }
          <Route exact path="/:slug/:id" component={ProductDetail} />
          <Route exact path="/profile" component={Profile} />
          <Route exact path="/cart" component={Carts} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;

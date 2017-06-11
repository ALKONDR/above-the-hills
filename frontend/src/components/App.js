import React from 'react';
import Nav from './presentations/Nav';
import Header from './presentations/Header';
import CategoriesContainer from './containers/CategoriesContainer';
import CategoryShares from './containers/CategoryShares';

const Router = require('react-router-dom').BrowserRouter;
const Route = require('react-router-dom').Route;
const Switch = require('react-router-dom').Switch;

class App extends React.PureComponent {
  render() {
    return (
      <div className="container">
        <Nav />
        <Header />
        <Router>
          <Switch>
            <Route exact path="/" component={CategoriesContainer} />
            <Route exact path="/categories/:category" component={CategoryShares} />
          </Switch>
        </Router>
      </div>
    );
  }
}

module.exports = App;

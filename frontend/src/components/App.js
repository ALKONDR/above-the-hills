import React from 'react';
import Nav from './presentations/Nav';
import Header from './presentations/Header';
import CategoriesContainer from './containers/CategoriesContainer';

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
          </Switch>
        </Router>
      </div>
    );
  }
}

module.exports = App;

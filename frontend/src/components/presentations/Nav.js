import React from 'react';

// const NavLink = require('react-router-dom').NavLink;

class Nav extends React.PureComponent {
  render() {
    const navElements = {
      main: 'Главная',
      categories: 'Категории',
      education: 'Обучение',
      test: 'Тест',
    };

    return (
      <div className="navContainer">
        <ul className="nav">
          {Object.keys(navElements).map(element => (
            <li key={element} className="navEl">
              {navElements[element]}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

module.exports = Nav;

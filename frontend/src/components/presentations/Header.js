import React from 'react';
import Title from './Title';

class Header extends React.PureComponent {
  render() {
    return (
      <div className="headerContainer">
        <div className="projectTitle">
          <Title>
            Above the hill
          </Title>
        </div>
        <div className="login">
          <Title>
            Войти/Регистрация
          </Title>
        </div>
      </div>
    );
  }
}

module.exports = Header;

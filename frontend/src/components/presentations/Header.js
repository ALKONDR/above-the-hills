import React from 'react';
import Title from './Title';

class Header extends React.PureComponent {
  render() {
    return (
      <div className="headerContainer nav-wrapper">
        <div className="projectTitle">
          <Title>
            Above the hill
          </Title>
        </div>
        <div className="login">
          <a href="https://oauth.vk.com/authorize?client_id=6069231&redirect_uri=http://membrain.ru">
            <Title>
              Войти через vK
            </Title>
          </a>
        </div>
      </div>
    );
  }
}

module.exports = Header;

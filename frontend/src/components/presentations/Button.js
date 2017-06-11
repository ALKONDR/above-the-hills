import React from 'react';
import PropTypes from 'prop-types';

class Button extends React.PureComponent {
  render() {
    return (
      <button className={this.props.cssClass} onClick={this.props.listener}>
        {this.props.children}
      </button>
    );
  }
}

Button.propTypes = {
  cssClass: PropTypes.string.isRequired,
  listener: PropTypes.func.isRequired,
  children: PropTypes.string.isRequired,
};

module.exports = Button;

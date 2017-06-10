import React from 'react';
import PropTypes from 'prop-types';

class Title extends React.PureComponent {
  render() {
    return (
      <h2 className="title">
        {this.props.children}
      </h2>
    );
  }
}

Title.propTypes = {
  children: PropTypes.string.isRequired,
};

module.exports = Title;

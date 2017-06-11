import React from 'react';
import PropTypes from 'prop-types';
import LineGraph from './LineGraph';
import Title from '../presentations/Title';
import SharesController from './SharesController';

class CategoryShares extends React.PureComponent {
  render() {
    return (
      <div className="categorySharesContainer">
        <div className="memeAndLogo">
          <Title>
            {this.props.match.params.category}
          </Title>
        </div>
        <LineGraph />
        <SharesController />
      </div>
    );
  }
}

CategoryShares.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.shape({
      category: PropTypes.string.isRequired,
    }).isRequired,
  }).isRequired,
};

module.exports = CategoryShares;

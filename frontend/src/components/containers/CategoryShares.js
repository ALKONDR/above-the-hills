import React from 'react';
import PropTypes from 'prop-types';
import LineGraph from './LineGraph';
import Title from '../presentations/Title';
import SharesController from './SharesController';
import api from '../utils/api';

class CategoryShares extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      data: [],
    };

    this.setState = this.setState.bind(this);
  }

  componentWillMount() {
    api.getCategory(this.props.match.params)
      .then((response) => {
        if (response.status >= 200 && response.status < 300) {
          this.setState({
            data: response.data.points,
          });
        }
      });
  }

  render() {
    return (
      <div className="categorySharesContainer">
        <div className="memeAndLogo">
          <Title>
            {this.props.match.params.category}
          </Title>
        </div>
        <LineGraph {...this.state.data} />
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

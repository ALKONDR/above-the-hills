import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

class Category extends React.PureComponent {
  render() {
    return (
      <div className="previewContainer card-panel">
        <Link to={`/categories/${this.props.category}`}>
          <h3 className="categoryName">
            {this.props.category}
          </h3>
        </Link>
        <div className="previewNumbers">
          <h3 className="sharesValue">
            {this.props.value}
          </h3>
          <h5 className="sharesDifference">
            {this.props.difference}
          </h5>
        </div>
      </div>
    );
  }
}

Category.propTypes = {
  category: PropTypes.string.isRequired,
  value: PropTypes.number.isRequired,
  difference: PropTypes.number.isRequired,
};

module.exports = Category;
